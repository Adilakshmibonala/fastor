from crm.interactors.presenter_interfaces.claim_enquiry_details_presenter_interface import \
    ClaimEnquiryDetailsPresenterInterface
from django.http.response import HttpResponse
from crm.presenters.mixins.get_error_response_object import GetErrorResponseObject


class ClaimEnquiryDetailsPresenterImplementation(
        ClaimEnquiryDetailsPresenterInterface, GetErrorResponseObject):

    def raise_invalid_enquiry_details_id_exception(self) -> HttpResponse:
        from crm.constants.exception_messages \
            import INVALID_ENQUIRY_DETAILS_ID_EXCEPTION
        return self.get_error_response_object(
            error_constant=INVALID_ENQUIRY_DETAILS_ID_EXCEPTION)

    def raise_can_not_claim_already_claimed_enquiry_details_exception(self) -> HttpResponse:
        from crm.constants.exception_messages \
            import CAN_NOT_CLAIM_ALREADY_CLAIMED_ENQUIRY_DETAILS_EXCEPTION
        return self.get_error_response_object(
            error_constant=CAN_NOT_CLAIM_ALREADY_CLAIMED_ENQUIRY_DETAILS_EXCEPTION)

