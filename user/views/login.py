from rest_framework import viewsets
from user.interactors.login_interactor import LoginInteractor
from user.serializers.user import LoginUserRequestValidationSerializer


class LoginViewSet(viewsets.GenericViewSet):
    serializer_class = LoginUserRequestValidationSerializer

    def create(self, request):
        from user.storages.storage_implementation import StorageImplementation
        from user.presenters.login_presenter_implementation import LoginPresenterImplementation

        request_data = request.data
        serializer = LoginUserRequestValidationSerializer()
        serializer.is_valid(raise_exception=True)

        email = request_data["email"]
        interactor = LoginInteractor(storage=StorageImplementation())
        response = interactor.login_user_wrapper(
            email=email, presenter=LoginPresenterImplementation())

        return response
