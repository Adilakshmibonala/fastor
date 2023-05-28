import abc


class RegisterUserPresenterInterface:

    @abc.abstractmethod
    def raise_user_already_registered_exception(self):
        pass

    @abc.abstractmethod
    def success_response(self, user_id: int):
        pass
