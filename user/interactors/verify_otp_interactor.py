from user.exceptions.custom_exceptions import UserDoesNotExistsException, InvalidOTPException, \
    UnexpectedErrorOccurredToGetTokenDetailsException
from user.interactors.presenter_interface.verify_otp_presenter_intrface import VerifyOTPPresenterInterface
from user.interactors.storage_interface.storage_interface import StorageInterface
from user.interactors.dtos import TokenDetailsDTO


class VerifyOTPInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def verify_otp_wrapper(self, email: str, otp: int, presenter: VerifyOTPPresenterInterface):
        try:
            token_details = self.verify_otp(email=email, otp=otp)
        except UserDoesNotExistsException:
            return presenter.raise_user_does_not_exists_exception()
        except InvalidOTPException:
            return presenter.raise_invalid_otp_exception()
        return presenter.success_response(token_details=token_details)

    def verify_otp(self, email: str, otp: int):
        is_user_already_registered = self.storage.check_is_user_already_registered(
            email=email)
        if not is_user_already_registered:
            raise UserDoesNotExistsException()

        self.storage.validate_otp(email=email, otp=otp)
        self._get_token_details(email=email)

    @staticmethod
    def _get_token_details(email: str) -> TokenDetailsDTO:
        import requests
        import json
        import os

        base_url = os.environ["SERVER_BASE_URL"]
        end_point = '/api/token/'
        url = base_url + end_point
        data = {"username": email}
        headers = {
            "Content-Type": "application/json"
        }
        try:
            response = requests.post(
                url=url, data=json.dumps(data), headers=headers)
            token_details_dict = json.loads(response.content)
        except Exception:
            raise UnexpectedErrorOccurredToGetTokenDetailsException()
        from user.interactors.dtos import TokenDetailsDTO
        token_details_dto = TokenDetailsDTO(
            access_token=token_details_dict["access"],
            refresh_token=token_details_dict["refresh"])

        return token_details_dto
