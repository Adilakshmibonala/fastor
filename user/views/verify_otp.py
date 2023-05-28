
from rest_framework import viewsets
from user.interactors.login_interactor import LoginInteractor
from user.serializers.user import VerifyOTPRequestValidationSerializer


class VerifyOTPView(viewsets.GenericViewSet):
    serializer_class = VerifyOTPRequestValidationSerializer

    def create(self, request):
        request_data = request.data
        serializer = VerifyOTPRequestValidationSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)

        pass
