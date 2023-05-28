from dataclasses import dataclass

from user.constants.enums import Gender


@dataclass()
class RegisterUserDetailsDTO:
    first_name: str
    last_name: str
    gender: Gender
    email: str
    phone_number: int


@dataclass()
class TokenDetailsDTO:
    access_token: str
    refresh_token: str
