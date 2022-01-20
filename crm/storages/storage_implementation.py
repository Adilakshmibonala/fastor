import typing

from crm.interactors.storage_interfaces import dtos as storage_dtos
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

    def get_all_enquiry_details(
            self, is_public_enquiry: bool) -> typing.List[storage_dtos.EnquiryDetailsDTO]:
        enquiry_details = EnquiryDetails.objects.filter(
            is_public_enquiry=is_public_enquiry)

        return [
            self._prepare_enquiry_details_dto(
                enquiry_details=each_enquiry_details)
            for each_enquiry_details in enquiry_details
        ]

    @staticmethod
    def _prepare_enquiry_details_dto(enquiry_details: EnquiryDetails):
        return storage_dtos.EnquiryDetailsDTO(
            enquiry_id=str(enquiry_details.id),
            username=enquiry_details.username,
            email=enquiry_details.email,
            phone_number=enquiry_details.phone_number,
            country_code=enquiry_details.country_code,
            course_name=enquiry_details.course_name,
            submitted_at=str(enquiry_details.submitted_at),
            is_public_enquiry=enquiry_details.is_public_enquiry)

    def get_user_claimed_enquiry_details(
            self, user_id) -> typing.List[storage_dtos.EnquiryDetailsDTO]:
        enquiry_details_ids = list(UserEnquiryDetails.objects.filter(
            user_id=user_id).values_list("enquiry_details_id", flat=True))
        enquiry_details = EnquiryDetails.objects.filter(
            id__in=enquiry_details_ids)

        return [
            self._prepare_enquiry_details_dto(
                enquiry_details=each_enquiry_details)
            for each_enquiry_details in enquiry_details
        ]

    def get_enquiry_details(
            self, enquiry_details_id: str) -> storage_dtos.EnquiryDetailsDTO:
        try:
            enquiry_details = EnquiryDetails.objects.get(
                id=enquiry_details_id)
        except EnquiryDetails.DoesNotExist:
            raise custom_exceptions.InvalidEnquiryDetailsIdException()

        return self._prepare_enquiry_details_dto(
            enquiry_details=enquiry_details)

    def create_user_enquiry_details(
            self, enquiry_details_id: str, user_id: str):
        UserEnquiryDetails.objects.create(
            user_id=user_id, enquiry_details_id=enquiry_details_id)

    def update_equity_details_as_private(
            self, enquiry_details_id: str, is_public_enquiry: bool):
        enquiry_details = EnquiryDetails.objects.select_for_update().get(
            id=enquiry_details_id)
        enquiry_details.is_public_enquiry = is_public_enquiry
        enquiry_details.save()
