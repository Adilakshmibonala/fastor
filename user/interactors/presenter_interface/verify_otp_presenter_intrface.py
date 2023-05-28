import abc

from user.interactors.dtos import TokenDetailsDTO


class VerifyOTPPresenterInterface:

    @abc.abstractmethod
    def raise_user_does_not_exists_exception(self):
        pass

    @abc.abstractmethod
    def raise_invalid_otp_exception(self):
        pass

    @abc.abstractmethod
    def success_response(self, token_details: TokenDetailsDTO):
        pass
