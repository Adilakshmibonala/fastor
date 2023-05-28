from user.exceptions.custom_exceptions import UserDoesNotExistsException, InvalidOTPException
from user.interactors.presenter_interface.verify_otp_presenter_intrface import VerifyOTPPresenterInterface
from user.interactors.storage_interface.storage_interface import StorageInterface


class VerifyOTPInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def verify_otp_wrapper(self, email: str, otp: int, presenter: VerifyOTPPresenterInterface):
        try:
            self.verify_otp(email=email, otp=otp)
        except UserDoesNotExistsException:
            return presenter.raise_user_does_not_exists_exception()
        except InvalidOTPException:
            return presenter.raise_invalid_otp_exception()
        return presenter.success_response()

    def verify_otp(self, email: str, otp: int):
        is_user_already_registered = self.storage.check_is_user_already_registered(
            email=email)
        if not is_user_already_registered:
            raise UserDoesNotExistsException()

        self.storage.validate_otp(email=email, otp=otp)


