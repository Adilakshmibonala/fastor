from user.interactors.presenter_interface.register_user_presenter_interface\
    import RegisterUserPresenterInterface
from user.presenters.mixins.get_error_response_object import GetErrorResponseObject


class RegisterUserPresenterImplementation(
        RegisterUserPresenterInterface, GetErrorResponseObject):

    def raise_user_already_registered_exception(self):
        from user.constants.exception_messages \
            import USER_ALREADY_REGISTERED_EXCEPTION
        return self.get_error_response_object(
            error_constant=USER_ALREADY_REGISTERED_EXCEPTION)

    def success_response(self, user_id: int):
        import json
        from django.http.response import HttpResponse

        data = {"user_id": user_id}
        return HttpResponse(content=json.dumps(data), status=200)
