from crm.interactors.storage_interfaces.storage_interface import StorageInterface
from crm.interactors.dtos import EnquiryDetailsDTO
from crm.exceptions import custom_exceptions
from crm.models import *


class StorageImplementation(StorageInterface):

    def get_user_password(self, username: str) -> str:
        try:
            user_account = UserAccount.objects.get(username=username)
        except UserAccount.DoesNotExist:
            raise custom_exceptions.UserDoesNotExistException()

        return user_account.password

    def create_enquiry_details(
            self, enquiry_details: EnquiryDetailsDTO):
        EnquiryDetails.objects.create(
            username=enquiry_details.username,
            email=enquiry_details.email,
            phone_number=enquiry_details.phone_number,
            country_code=enquiry_details.country_code,
            course_name=enquiry_details.course_name)

    def check_is_enquiry_details_already_exists(
            self, enquiry_details: EnquiryDetailsDTO) -> bool:
        is_enquiry_details_already_exists = EnquiryDetails.objects.filter(
            username=enquiry_details.username,
            email=enquiry_details.email,
            phone_number=enquiry_details.phone_number,
            country_code=enquiry_details.country_code,
            course_name=enquiry_details.course_name).exists()

        return is_enquiry_details_already_exists
