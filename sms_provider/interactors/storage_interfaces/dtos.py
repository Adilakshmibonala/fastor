from dataclasses import dataclass


@dataclass()
class SMSProviderDetailsDTO:
    id: str
    sms_provider: str
    throughput: str
