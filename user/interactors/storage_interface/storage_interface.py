import abc

from user.interactors.dtos import RegisterUserDetailsDTO


class StorageInterface:

    @abc.abstractmethod
    def register_user(self, register_user_details_dto: RegisterUserDetailsDTO) -> int:
        pass

    @abc.abstractmethod
    def check_is_user_already_registered(self, email: str) -> bool:
        pass
