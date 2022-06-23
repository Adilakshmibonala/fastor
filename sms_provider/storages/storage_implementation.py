import typing

from sms_provider.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from sms_provider.exceptions import custom_exceptions
from sms_provider.models.sms_details import *
from sms_provider.interactors.storage_interfaces import dtos as storage_dtos


class StorageImplementation(StorageInterface):

    def get_user_password(self, email: str) -> str:
        try:
            user_account = UserAccount.objects.get(email=email)
        except UserAccount.DoesNotExist:
            raise custom_exceptions.UserDoesNotExistException()

        return user_account.password

    def create_sms_status_details(
            self, sms_status_details: storage_dtos.SMSStatusDetailsDTO):
        SMSStatusDetails.objects.create(
            sms_provider=sms_status_details.sms_provider_id,
            phone_number=sms_status_details.phone_number,
            status=sms_status_details.status)

    def get_sms_provider_configs(
            self, is_active: bool) -> typing.List[storage_dtos.SMSProviderConfigDTO]:
        sms_provider_configs = SMSProviderConfig.objects.filter(
            is_active=is_active)
        return [
            storage_dtos.SMSProviderConfigDTO(
                id=str(sms_provider_config.id),
                sms_provider=sms_provider_config.sms_provider,
                throughput=sms_provider_config.throughput)
            for sms_provider_config in sms_provider_configs
        ]
