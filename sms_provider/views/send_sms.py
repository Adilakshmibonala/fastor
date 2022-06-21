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
            phone_numbers = request_data["phone_numbers"]
            self._validate_phone_numbers(phone_numbers=phone_numbers)

    @staticmethod
    def _validate_phone_numbers(phone_numbers: typing.List[str]) -> None:
        import re

        invalid_phone_numbers = []
        validate_phone_number_pattern = "^\\+?[1-9][0-9]{7,14}$"
        for each_phone_number in phone_numbers:
            if not re.match(validate_phone_number_pattern, "+12223334444"):
                invalid_phone_numbers.append(each_phone_number)

        if invalid_phone_numbers:
            from sms_provider.exceptions.custom_exceptions \
                import InvalidPhoneNumbersException
            raise InvalidPhoneNumbersException(invalid_phone_numbers=invalid_phone_numbers)

