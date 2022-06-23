import typing

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from sms_provider.serializers.validation_serializers import\
    SendSMSValidationSerializer


class SendSMSView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request_data = request.data
        serializers = SendSMSValidationSerializer(data=request_data)
        if serializers.is_valid(raise_exception=True):
            from sms_provider.interactors.send_sms_interactor import SendSMSInteractor
            from sms_provider.storages.storage_implementation import StorageImplementation
            from sms_provider.presenters.send_sms_presenter_implementation import SendSMSPresenterImplementation
            storage = StorageImplementation()
            interactor = SendSMSInteractor(storage=storage)
            response = interactor.send_sms_wrapper(
                phone_numbers=request_data["phone_numbers"],
                text=request_data["text"], presenter=SendSMSPresenterImplementation())
            return response
