from user.exceptions.custom_exceptions import UserDoesNotExistsException
from user.interactors.presenter_interface.login_presenter_interface import LoginPresenterInterface
from user.interactors.storage_interface.storage_interface import StorageInterface


class VerifyOTPInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def verify_otp_wrapper(self, email: str, otp: int, presenter: LoginPresenterInterface):
        try:
            self.verify_otp(email=email, otp=otp)
        except UserDoesNotExistsException:
            return presenter.raise_user_does_not_exists_exception()
        return presenter.success_response()

    def verify_otp(self, email: str, otp: int):
        pass


