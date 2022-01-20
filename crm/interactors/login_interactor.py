from crm.exceptions.custom_exceptions import \
    IncorrectPasswordException, UserDoesNotExistException, \
    UnexpectedErrorOccurredToGetTokenDetailsException
from crm.interactors.presenter_interfaces.login_presenter_interface\
    import LoginPresenterInterface
from crm.interactors.storage_interfaces.storage_interface import StorageInterface
from crm.interactors.dtos import TokenDetailsDTO


class LoginInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def login_wrapper(
            self, username: str, password: str,
            presenter: LoginPresenterInterface):
        try:
            token_details = self.login(username=username, password=password)
        except IncorrectPasswordException:
            return presenter.raise_incorrect_password_exception()
        except UserDoesNotExistException:
            return presenter.raise_user_does_not_exist_exception()
        except UnexpectedErrorOccurredToGetTokenDetailsException:
            return presenter.raise_unexpected_error_occurred_to_get_token_details_exception()

        return presenter.get_response_for_login(token_details=token_details)

    def login(self, username: str, password: str) -> TokenDetailsDTO:
        from django.contrib.auth.hashers import check_password

        existing_encrypted_password = self.storage.get_user_password(
            username=username)
        is_valid_password = check_password(
            password, existing_encrypted_password)
        if not is_valid_password:
            raise IncorrectPasswordException()

        token_details = self._get_token_details(
            username=username, password=password)
        return token_details

    @staticmethod
    def _get_token_details(username: str, password: str) -> TokenDetailsDTO:
        import requests
        import json
        import os

        base_url = os.environ["SERVER_BASE_URL"]
        end_point = '/api/token/'
        url = base_url + end_point
        data = {
            "username": username, "password": password
        }
        headers = {
            "Content-Type": "application/json"
        }
        try:
            response = requests.post(
                url=url, data=json.dumps(data), headers=headers)
            token_details_dict = json.loads(response.content)
        except Exception:
            raise UnexpectedErrorOccurredToGetTokenDetailsException()
        token_details_dto = TokenDetailsDTO(
            access_token=token_details_dict["access"],
            refresh_token=token_details_dict["refresh"])

        return token_details_dto
