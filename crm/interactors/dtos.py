from dataclasses import dataclass


@dataclass()
class TokenDetailsDTO:
    access_token: str
    refresh_token: str


@dataclass()
class EnquiryDetailsDTO:
    username: str
    email: str
    phone_number: str
    country_code: str
    course_name: str
