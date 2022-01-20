import abc

from django.http.response import HttpResponse
from crm.interactors.dtos import AllEnquiryDetailsDTO


class GetEnquiryDetailsPresenterInterface:

    @abc.abstractmethod
    def get_response_for_get_enquiry_details(
            self, enquiry_details: AllEnquiryDetailsDTO) -> HttpResponse:
        pass
