from rest_framework import viewsets
from user.interactors.register_user_interactor import RegisterUserInteractor
from user.serializers.user import \
    RegisterUserRequestValidationSerializer


class UserSignUpViewSet(viewsets.GenericViewSet):
    serializer_class = RegisterUserRequestValidationSerializer

    def create(self, request):
        from user.storages.storage_implementation import StorageImplementation
        from user.interactors.dtos import RegisterUserDetailsDTO
        from user.presenters.register_user_presenter_implementation import \
            RegisterUserPresenterImplementation

        request_data = request.data
        register_user_validation_serializer = \
            RegisterUserRequestValidationSerializer(data=request_data)
        register_user_validation_serializer.is_valid(raise_exception=True)

        interactor = RegisterUserInteractor(storage=StorageImplementation())
        response = interactor.register_user_wrapper(
            presenter=RegisterUserPresenterImplementation(),
            register_user_details_dto=RegisterUserDetailsDTO(**request_data))

        return response
