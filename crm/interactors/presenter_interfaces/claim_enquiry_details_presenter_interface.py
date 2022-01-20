import abc

from django.http.response import HttpResponse


class ClaimEnquiryDetailsPresenterInterface:

    @abc.abstractmethod
    def raise_invalid_enquiry_details_id_exception(self) -> HttpResponse:
        pass

    @abc.abstractmethod
    def raise_can_not_claim_already_claimed_enquiry_details_exception(self) -> HttpResponse:
        pass
