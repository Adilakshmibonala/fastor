from user.interactors.presenter_interface.login_presenter_interface import LoginPresenterInterface
from user.presenters.mixins.get_error_response_object import GetErrorResponseObject


class LoginPresenterImplementation(LoginPresenterInterface, GetErrorResponseObject):

    def raise_user_does_not_exists_exception(self):
        from user.constants.exception_messages \
            import USER_DOES_NOT_EXISTS_EXCEPTION
        return self.get_error_response_object(
            error_constant=USER_DOES_NOT_EXISTS_EXCEPTION)

    def success_response(self):
        from django.http.response import HttpResponse

        return HttpResponse(status=200)
