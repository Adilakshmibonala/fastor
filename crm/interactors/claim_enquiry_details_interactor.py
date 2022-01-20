from crm.exceptions.custom_exceptions import InvalidEnquiryDetailsIdException, \
    CanNotClaimAlreadyClaimedEnquiredDetailsException
from crm.interactors.presenter_interfaces.claim_enquiry_details_presenter_interface import \
    ClaimEnquiryDetailsPresenterInterface
from crm.interactors.storage_interfaces.storage_interface import StorageInterface


class ClaimEnquiryDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def claim_enquiry_details_wrapper(
            self, user_id: str, enquiry_details_id: str,
            presenter: ClaimEnquiryDetailsPresenterInterface):
        try:
            self.claim_enquiry_details(
                user_id=user_id, enquiry_details_id=enquiry_details_id)
        except InvalidEnquiryDetailsIdException:
            return presenter.raise_invalid_enquiry_details_id_exception()
        except CanNotClaimAlreadyClaimedEnquiredDetailsException:
            return presenter.raise_can_not_claim_already_claimed_enquiry_details_exception()

    def claim_enquiry_details(
            self, user_id: str, enquiry_details_id: str):
        enquiry_details = self.storage. \
            get_enquiry_details(enquiry_details_id=enquiry_details_id)
        if not enquiry_details.is_public_enquiry:
            raise CanNotClaimAlreadyClaimedEnquiredDetailsException()

        self.storage.create_user_enquiry_details(
            user_id=user_id, enquiry_details_id=enquiry_details_id)
        self.storage.update_equity_details_as_private(
            enquiry_details_id=enquiry_details_id,
            is_public_enquiry=False)
