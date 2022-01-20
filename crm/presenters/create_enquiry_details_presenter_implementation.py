from crm.interactors.presenter_interfaces.create_enquiry_details_presenter_interface import \
    CreateEquityDetailsPresenterInterface
from django.http.response import HttpResponse
from crm.presenters.mixins.get_error_response_object import GetErrorResponseObject


class CreateEquityDetailsPresenterImplementation(
        CreateEquityDetailsPresenterInterface, GetErrorResponseObject):

    def raise_given_enquiry_details_already_exists_exception(self) -> HttpResponse:
        from crm.constants.exception_messages \
            import GIVEN_ENQUIRY_DETAILS_ALREADY_EXISTS_EXCEPTION
        return self.get_error_response_object(
            error_constant=GIVEN_ENQUIRY_DETAILS_ALREADY_EXISTS_EXCEPTION)
