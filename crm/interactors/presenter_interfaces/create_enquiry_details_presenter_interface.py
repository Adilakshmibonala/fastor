import abc

from django.http.response import HttpResponse


class CreateEquityDetailsPresenterInterface:

    @abc.abstractmethod
    def raise_given_enquiry_details_already_exists_exception(self) -> HttpResponse:
        pass
