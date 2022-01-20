from dataclasses import dataclass


@dataclass()
class EnquiryDetailsDTO:
    enquiry_id: str
    username: str
    email: str
    phone_number: str
    country_code: str
    course_name: str
    submitted_at: str
