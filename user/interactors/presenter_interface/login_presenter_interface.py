import abc


class LoginPresenterInterface:

    @abc.abstractmethod
    def raise_user_does_not_exists_exception(self):
        pass

    @abc.abstractmethod
    def success_response(self):
        pass
