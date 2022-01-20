import abc


class StorageInterface:

    @abc.abstractmethod
    def get_user_password(self, username: str) -> str:
        pass

