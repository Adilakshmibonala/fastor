class IncorrectPasswordException(Exception):
    pass


class UserDoesNotExistException(Exception):
    pass


class UnexpectedErrorOccurredToGetTokenDetailsException(Exception):
    pass


class GivenEnquiryDetailsAlreadyExistsException(Exception):
    pass
