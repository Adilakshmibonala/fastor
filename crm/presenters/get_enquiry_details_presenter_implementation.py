import typing

from crm.interactors.presenter_interfaces.get_enquiry_details_presenter_interface import \
    GetEnquiryDetailsPresenterInterface
from django.http.response import HttpResponse
from crm.interactors.dtos import AllEnquiryDetailsDTO, EnquiryDetailsDTO
from crm.interactors.storage_interfaces.dtos import EnquiryDetailsDTO


class GetEnquiryDetailsPresenterImplementation(GetEnquiryDetailsPresenterInterface):

    def get_response_for_get_enquiry_details(
            self, enquiry_details: AllEnquiryDetailsDTO) -> HttpResponse:
        import json

        public_enquiry_details = enquiry_details.public_enquiry_details
        user_claimed_enquiry_details = enquiry_details.user_claimed_enquiry_details

        data = [
            {
                "public_enquiry_details": self._get_enquiry_details(
                    enquiry_details=public_enquiry_details),
                "user_claimed_enquiry_details": self._get_enquiry_details(
                    enquiry_details=user_claimed_enquiry_details),
            }
        ]
        return HttpResponse(content=json.dumps(data), status=200)

    @staticmethod
    def _get_enquiry_details(enquiry_details: typing.List[EnquiryDetailsDTO]):
        return [
            {
                "enquiry_id": each_enquiry_details.enquiry_id,
                "username": each_enquiry_details.username,
                "email": each_enquiry_details.email,
                "phone_number": each_enquiry_details.phone_number,
                "country_code": each_enquiry_details.country_code,
                "course_name": each_enquiry_details.course_name,
                "submitted_at": each_enquiry_details.submitted_at
            }
            for each_enquiry_details in enquiry_details
        ]
