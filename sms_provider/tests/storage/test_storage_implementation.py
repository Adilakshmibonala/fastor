import pytest

from sms_provider.constants.enums import SMSStatus
from sms_provider.interactors.storage_interfaces import dtos as storage_dtos
from sms_provider.models.sms_details import *


@pytest.mark.django_db
class TestStorageImplementation:

    @pytest.fixture()
    def storage(self):
        from sms_provider.storages.storage_implementation \
            import StorageImplementation

        return StorageImplementation()

    def test_create_sms_status_details(self, storage):
        # Arrange
        sms_provider = SMSProviderConfig.objects.create(
            sms_provider=SMSProvider.JIO.value)
        sms_status_details = storage_dtos.SMSStatusDetailsDTO(
            sms_provider_id=str(sms_provider.id),
            phone_number="9988776655",
            status=SMSStatus.SENT.value)

        # Act
        storage.create_sms_status_details(sms_status_details=sms_status_details)

        # Assert
        sms_status = SMSStatusDetails.objects.get(sms_provider_id=str(sms_provider.id))
        assert sms_status.phone_number == sms_status_details.phone_number
        assert sms_status.status == sms_status_details.status
