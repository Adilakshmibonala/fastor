import typing

from sms_provider.interactors.storage_interfaces.storage_interface \
    import StorageInterface


class SendSMSInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def send_sms(self, phone_numbers: typing.List[str], text: str):
        from sms_provider.interactors.sms_provider_interactor \
            import SMSProviderInteractor

        sms_provider_details = self.storage.get_sms_provider_details(
            is_active=True)
        if not sms_provider_details:
            pass
        total_throughput = 0
        for each in sms_provider_details:
            total_throughput += each.throughput
        multiplier = total_throughput / len(phone_numbers)

        interactor = SMSProviderInteractor(storage=self.storage)
        messages_count = 0
        for each in sms_provider_details:
            msg_size = each.throughput * multiplier
            phone_numbers_for_provider = phone_numbers[messages_count:msg_size]
            interactor.sms_provider(
                sms_provider_details=each, text=text,
                phone_numbers=phone_numbers_for_provider)
            messages_count += msg_size

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

