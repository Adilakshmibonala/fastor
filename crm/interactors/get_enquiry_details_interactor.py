from crm.interactors.presenter_interfaces.get_enquiry_details_presenter_interface import \
    GetEnquiryDetailsPresenterInterface
from crm.interactors.storage_interfaces.storage_interface import StorageInterface
from crm.interactors.dtos import AllEnquiryDetailsDTO


class GetEnquiryDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_enquiry_details_wrapper(
            self, user_id: str, presenter: GetEnquiryDetailsPresenterInterface):
        enquiry_details = self.get_enquiry_details(
            user_id=user_id)
        return presenter.get_response_for_get_enquiry_details(
            enquiry_details=enquiry_details)

    def get_enquiry_details(self, user_id: str):
        public_enquiry_details = self.storage.get_all_enquiry_details(
            is_public_enquiry=True)
        user_claimed_enquiry_details = self.storage.\
            get_user_claimed_enquiry_details(user_id=user_id)

        return AllEnquiryDetailsDTO(
            public_enquiry_details=public_enquiry_details,
            user_claimed_enquiry_details=user_claimed_enquiry_details)