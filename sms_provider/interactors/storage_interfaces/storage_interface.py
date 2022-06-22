import abc
import typing

from sms_provider.interactors.storage_interfaces import dtos as storage_dtos


class StorageInterface:

    @abc.abstractmethod
    def get_user_password(self, email: str) -> str:
        pass

    @abc.abstractmethod
    def create_sms_status_details(
            self, sms_status_details: storage_dtos.SMSStatusDetailsDTO):
        pass

    @abc.abstractmethod
    def get_sms_provider_details(
            self, is_active: bool) -> typing.List[storage_dtos.SMSProviderDetailsDTO]:
        pass
