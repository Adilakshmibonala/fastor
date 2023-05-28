from user.interactors.presenter_interface.verify_otp_presenter_intrface import VerifyOTPPresenterInterface
from user.presenters.mixins.get_error_response_object import GetErrorResponseObject


class VerifyOTPPresenterImplementation(VerifyOTPPresenterInterface, GetErrorResponseObject):

    def raise_user_does_not_exists_exception(self):
        from user.constants.exception_messages \
            import USER_DOES_NOT_EXISTS_EXCEPTION
        return self.get_error_response_object(
            error_constant=USER_DOES_NOT_EXISTS_EXCEPTION)

    def success_response(self):
        from django.http.response import HttpResponse

        return HttpResponse(status=200)

    def raise_invalid_otp_exception(self):
        from user.constants.exception_messages \
            import INVALID_OTP_EXCEPTION
        return self.get_error_response_object(
            error_constant=INVALID_OTP_EXCEPTION)
