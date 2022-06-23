import typing

from sms_provider.constants.enums import SMSProvider, SMSStatus
from sms_provider.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from sms_provider.interactors.storage_interfaces.dtos import \
    SMSProviderConfigDTO, SMSStatusDetailsDTO


class SMSProviderInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def sms_provider(
            self, sms_provider_details: SMSProviderConfigDTO,
            phone_numbers: typing.List[str], text: str):
        if sms_provider_details.sms_provider == SMSProvider.TWILIO.value:
            send_sms_using_twilio_service(
                sms_provider_details=sms_provider_details,
                phone_numbers=phone_numbers, text=text)
        elif sms_provider_details.sms_provider == SMSProvider.JIO.value:
            send_sms_using_twilio_service(
                sms_provider_details=sms_provider_details,
                phone_numbers=phone_numbers, text=text)


# TODO: make this as async task.
def send_sms_using_twilio_service(
        sms_provider_details: SMSProviderConfigDTO,
        phone_numbers: typing.List[str], text: str):

    from sms_provider.services.twillio_service import TwilioService
    from sms_provider.storages.storage_implementation \
        import StorageImplementation

    storage = StorageImplementation()
    twilio_service = TwilioService()
    for each_phone_number in phone_numbers:
        response = twilio_service.send_message(
            phone_number=each_phone_number, message=text)
        if response.status_code == 200:
            sms_status_details = SMSStatusDetailsDTO(
                sms_provider_id=sms_provider_details.id,
                phone_number=each_phone_number,
                status=SMSStatus.SENT.value)
        else:
            sms_status_details = SMSStatusDetailsDTO(
                sms_provider_id=sms_provider_details.id,
                phone_number=each_phone_number,
                status=SMSStatus.FAILED.value)

        storage.create_sms_status_details(
            sms_status_details=sms_status_details)
