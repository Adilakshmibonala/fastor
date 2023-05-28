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

        phone_number = self.storage.get_user_phone_number(email=email)
        account_sid = os.environ["ACCOUNT_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        client = Client(account_sid, auth_token)
        otp = self.generate_otp(length=6)
        client.messages.create(
            body="{otp} is your Panorbit verification OTP. Please do not share it with anyone.".format(otp=otp),
            from_=os.environ["TWILIO_PHONE_NUMBER"],
            to="+91{phone_number}".format(phone_number=phone_number))
        self.storage.create_user_otp(user_id=1, otp=otp)

    @staticmethod
    def generate_otp(length: int):
        return 0
