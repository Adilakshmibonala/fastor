import abc
import typing

from django.http.response import HttpResponse


class SendSMSPresenterInterface:

    @abc.abstractmethod
    def raise_invalid_phone_number_exception(
            self, phone_number: typing.List[str]) -> HttpResponse:
        pass

