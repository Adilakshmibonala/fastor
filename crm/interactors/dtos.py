import typing

from dataclasses import dataclass
from crm.interactors.storage_interfaces import dtos as storage_dtos


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


@dataclass()
class AllEnquiryDetailsDTO:
    public_enquiry_details: typing.List[storage_dtos.EnquiryDetailsDTO]
    user_claimed_enquiry_details: typing.List[storage_dtos.EnquiryDetailsDTO]
