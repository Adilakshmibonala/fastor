from user.exceptions.custom_exceptions import UserAlreadyRegisteredException
from user.interactors.dtos import RegisterUserDetailsDTO
from user.interactors.presenter_interface.register_user_presenter_interface import RegisterUserPresenterInterface
from user.interactors.storage_interface.storage_interface import StorageInterface


class RegisterUserInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def register_user_wrapper(
            self, presenter: RegisterUserPresenterInterface,
            register_user_details_dto: RegisterUserDetailsDTO):
        try:
            user_id = self.register_user(
                register_user_details_dto=register_user_details_dto)
        except UserAlreadyRegisteredException:
            return presenter.raise_user_already_registered_exception()
        return presenter.success_response(user_id=user_id)

    def register_user(
            self, register_user_details_dto: RegisterUserDetailsDTO) -> int:
        is_user_already_registered = self.storage.check_is_user_already_registered(
            email=register_user_details_dto.email)
        if is_user_already_registered:
            raise UserAlreadyRegisteredException()
        user_id = self.storage.register_user(
            register_user_details_dto=register_user_details_dto)

        return user_id
