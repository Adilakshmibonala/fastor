class InvalidPhoneNumbersException(Exception):

    def __init__(self, invalid_phone_numbers):
        self.invalid_phone_numbers = invalid_phone_numbers
