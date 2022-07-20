from sms_provider.utils.base_enum import BaseEnum


class SMSProvider(BaseEnum):
    AIRTEL = "AIRTEL"
    JIO = "JIO"
    TWILIO = "TWILIO"


class SMSStatus(BaseEnum):
    SENT = "SENT"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
