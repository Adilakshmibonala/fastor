from user.exceptions.custom_exceptions import UserDoesNotExistsException
from user.interactors.presenter_interface.login_presenter_interface import LoginPresenterInterface
from user.interactors.storage_interface.storage_interface import StorageInterface


class LoginInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def login_user_wrapper(self, email: str, presenter: LoginPresenterInterface):
        try:
            self.login_user(email=email)
        except UserDoesNotExistsException:
            return presenter.raise_user_does_not_exists_exception()
        return presenter.success_response()

    def login_user(self, email: str):
        from user.interactors.send_otp_interactor import SendOTPInteractor
        interactor = SendOTPInteractor(storage=self.storage)
        return interactor.send_otp(email=email)
