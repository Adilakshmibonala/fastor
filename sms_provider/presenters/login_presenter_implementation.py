from sms_provider.interactors.presenter_interfaces.\
    login_presenter_interface import LoginPresenterInterface
from django.http.response import HttpResponse
from sms_provider.presenters.mixins.get_error_response_object import GetErrorResponseObject
from sms_provider.interactors.dtos import TokenDetailsDTO


class LoginPresenterImplementation(
        LoginPresenterInterface, GetErrorResponseObject):

    def raise_incorrect_password_exception(self) -> HttpResponse:
        from sms_provider.constants.exception_messages \
            import INCORRECT_PASSWORD_EXCEPTION
        return self.get_error_response_object(
            error_constant=INCORRECT_PASSWORD_EXCEPTION)

    def get_response_for_login(
            self, token_details: TokenDetailsDTO) -> HttpResponse:
        import json
        data = {
            "access_token": token_details.access_token,
            "refresh_token": token_details.refresh_token
        }
        return HttpResponse(content=json.dumps(data), status=200)

    def raise_user_does_not_exist_exception(self) -> HttpResponse:
        from sms_provider.constants.exception_messages \
            import USER_DOES_NOT_EXISTS_EXCEPTION
        return self.get_error_response_object(
            error_constant=USER_DOES_NOT_EXISTS_EXCEPTION)

    def raise_unexpected_error_occurred_to_get_token_details_exception(self)\
            -> HttpResponse:
        from sms_provider.constants.exception_messages \
            import UNEXPECTED_ERROR_OCCURRED_TO_GET_TOKEN_DETAILS_EXCEPTION
        return self.get_error_response_object(
            error_constant=UNEXPECTED_ERROR_OCCURRED_TO_GET_TOKEN_DETAILS_EXCEPTION)
