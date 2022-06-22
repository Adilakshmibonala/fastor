from dataclasses import dataclass


@dataclass()
class SMSProviderDetailsDTO:
    id: str
    sms_provider: str
    throughput: str


@dataclass()
class SMSStatusDetailsDTO:
    sms_provider_id: str
    phone_number: str
    status: str