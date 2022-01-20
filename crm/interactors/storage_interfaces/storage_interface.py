import abc
import typing

from crm.interactors.dtos import EnquiryDetailsDTO
from crm.interactors.storage_interfaces import dtos as storage_dtos


class StorageInterface:

    @abc.abstractmethod
    def get_user_password(self, username: str) -> str:
        pass

    @abc.abstractmethod
    def create_enquiry_details(
            self, enquiry_details: EnquiryDetailsDTO):
        pass

    @abc.abstractmethod
    def check_is_enquiry_details_already_exists(
            self, enquiry_details: EnquiryDetailsDTO) -> bool:
        pass

    @abc.abstractmethod
    def get_all_enquiry_details(
            self, is_public_enquiry: bool) \
            -> typing.List[storage_dtos.EnquiryDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_user_claimed_enquiry_details(
            self, user_id) -> typing.List[storage_dtos.EnquiryDetailsDTO]:
        pass
