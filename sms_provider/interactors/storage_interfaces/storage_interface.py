import abc
import typing


class StorageInterface:

    @abc.abstractmethod
    def get_user_password(self, email: str) -> str:
        pass
