import typing


class SendSMSInteractor:

    def send_sms(self, phone_numbers: typing.List[str], text: str):
        from sms_provider.services.twillio_service import TwilioService

        twilio_service = TwilioService()
        for each_phone_number in phone_numbers:
            response = twilio_service.send_message(
                phone_number=each_phone_number, message=text)
            if response.status_code == 200:
                pass
            else:
                pass

    @staticmethod
    def _validate_phone_numbers(phone_numbers: typing.List[str]) -> None:
        import re

        invalid_phone_numbers = []
        validate_phone_number_pattern = "^\\+?[1-9][0-9]{7,14}$"
        for each_phone_number in phone_numbers:
            if not re.match(validate_phone_number_pattern, each_phone_number):
                invalid_phone_numbers.append(each_phone_number)

        if invalid_phone_numbers:
            from sms_provider.exceptions.custom_exceptions \
                import InvalidPhoneNumbersException
            raise InvalidPhoneNumbersException(invalid_phone_numbers=invalid_phone_numbers)

