from user.exceptions.custom_exceptions import UserDoesNotExistsException
from user.interactors.presenter_interface.login_presenter_interface import LoginPresenterInterface
from user.interactors.storage_interface.storage_interface import StorageInterface


class LoginInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def login_user_wrapper(self, email: str, presenter: LoginPresenterInterface):
        try:
            self.login_user(email=email)
        except UserDoesNotExistsException:
            return presenter.raise_user_does_not_exists_exception()
        return presenter.success_response()

    def login_user(self, email: str):
        import os
        from twilio.rest import Client
        from django.template.loader import render_to_string

        phone_number = self.storage.get_user_phone_number(email=email)
        account_sid = os.environ["ACCOUNT_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        client = Client(account_sid, auth_token)
        otp = self.generate_otp(length=6)
        client.messages.create(
            body="{otp} is your Panorbit verification OTP. Please do not share it with anyone.".format(otp=otp),
            from_=os.environ["TWILIO_PHONE_NUMBER"],
            to="+91{phone_number}".format(phone_number=phone_number))

        subject = render_to_string('templates/send_otp/subject.txt')
        message = render_to_string('templates/join_nie/body.html', {'otp': otp})
        self._send_notification(subject=subject, message=message, email=email)
        self.storage.create_user_otp(user_id=1, otp=otp)

    @staticmethod
    def _send_notification(subject: str, message: str, email: str):
        from django.core.mail import send_mail
        from django.utils.html import strip_tags

        send_mail(
            subject=subject, message=strip_tags(message),
            from_email="FROM_EMAIL", recipient_list=[email],
            fail_silently=False, html_message=message)

    @staticmethod
    def generate_otp(length: int):
        return 0
