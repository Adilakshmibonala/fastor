import abc

from django.http.response import HttpResponse
from crm.interactors.dtos import TokenDetailsDTO


class LoginPresenterInterface:

    @abc.abstractmethod
    def raise_incorrect_password_exception(self) -> HttpResponse:
        pass

    @abc.abstractmethod
    def get_response_for_login(self, token_details: TokenDetailsDTO) -> HttpResponse:
        pass

    @abc.abstractmethod
    def user_does_not_exist_exception(self) -> HttpResponse:
        pass

    @abc.abstractmethod
    def raise_unexpected_error_occurred_to_get_token_details_exception(self) -> HttpResponse:
        pass
