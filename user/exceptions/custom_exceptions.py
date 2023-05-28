class UserAlreadyRegisteredException(Exception):
    pass


class UserDoesNotExistsException(Exception):
    pass


class InvalidOTPException(Exception):
    pass


class UnexpectedErrorOccurredToGetTokenDetailsException(Exception):
    pass
