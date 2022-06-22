import abc
import typing

from sms_provider.interactors.storage_interfaces.dtos import SMSProviderDetailsDTO


class StorageInterface:

    @abc.abstractmethod
    def get_user_password(self, email: str) -> str:
        pass

    @abc.abstractmethod
    def create_sms_status_details(self):
        pass

    @abc.abstractmethod
    def get_sms_provider_details(
            self, is_active: bool) -> typing.List[SMSProviderDetailsDTO]:
        pass
