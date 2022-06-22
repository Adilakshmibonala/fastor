import typing

from sms_provider.interactors.storage_interfaces.storage_interface import StorageInterface


class SendSMSInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def send_sms(self, phone_numbers: typing.List[str], text: str):
        from sms_provider.services.twillio_service import TwilioService
        from collections import defaultdict

        sms_provider_details = self.storage.get_sms_provider_details(
            is_active=True)
        if not sms_provider_details:
            pass

        sms_provider_details = sorted(sms_provider_details, key=lambda k: k.throughput)
        min_throughput = sms_provider_details[0].throughput
        provider_wise_throughput = defaultdict()
        for each in sms_provider_details:
            provider_wise_throughput[each.sms_provider] = each.throughput

        sms_provider_wise_messages = defaultdict(int)
        batch_wise_msgs = self._get_batch_wise_objects(
            objects=phone_numbers, number_of_elements_per_batch=min_throughput)
        for batch_msgs in batch_wise_msgs:
            pass

        for sms_provider, phone_numbers in sms_provider_wise_messages.items():
            pass
            # TODO: Create an async task for each provider.

        twilio_service = TwilioService()
        for each_phone_number in phone_numbers:
            response = twilio_service.send_message(
                phone_number=each_phone_number, message=text)
            if response.status_code == 200:
                pass
            else:
                pass

    @staticmethod
    def _get_batch_wise_objects(objects, number_of_elements_per_batch):
        batch_wise_users = [
            objects[i:i + number_of_elements_per_batch]
            for i in range(0, len(objects), number_of_elements_per_batch)
        ]
        return batch_wise_users

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

