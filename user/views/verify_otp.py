from rest_framework import viewsets
from user.serializers.user import VerifyOTPRequestValidationSerializer


class VerifyOTPView(viewsets.GenericViewSet):
    serializer_class = VerifyOTPRequestValidationSerializer

    def create(self, request):
        request_data = request.data
        serializer = VerifyOTPRequestValidationSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)

        from user.interactors.verify_otp_interactor import VerifyOTPInteractor
        from user.storages.storage_implementation import StorageImplementation
        from user.presenters.verify_otp_presenter_implementation import VerifyOTPPresenterImplementation

        interactor = VerifyOTPInteractor(storage=StorageImplementation())
        response = interactor.verify_otp_wrapper(
            email=request_data["email"], otp=request_data["otp"],
            presenter=VerifyOTPPresenterImplementation())

        return response
