import abc

from crm.interactors.dtos import EnquiryDetailsDTO


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

