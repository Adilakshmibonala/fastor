import pytest


class TestSendSMSInteractor:

    @pytest.fixture()
    def storage(self):
        from sms_provider.interactors.storage_interfaces. \
            storage_interface import StorageInterface

        from unittest.mock import create_autospec
        return create_autospec(StorageInterface)

    @pytest.fixture()
    def interactor(self, storage):
        from sms_provider.interactors.send_sms_interactor \
            import SendSMSInteractor

        return SendSMSInteractor(storage=storage)

    @pytest.fixture()
    def presenter(self):
        from unittest.mock import create_autospec
        from sms_provider.interactors.presenter_interfaces.send_sms_presenter_interface\
            import SendSMSPresenterInterface

        return create_autospec(SendSMSPresenterInterface)

    def test_given_invalid_phone_numbers_then_raise_exception(
            self, interactor, presenter):
        # Arrange
        from unittest.mock import Mock

        phone_numbers = ["9949856434", "333"]
        text = "Hi, Nice to see you here!!"
        expected_response = Mock()

        presenter.raise_invalid_phone_number_exception.return_value = expected_response

        # Act
        actual_response = interactor.send_sms_wrapper(
            phone_numbers=phone_numbers, text=text, presenter=presenter)

        # Assert
        assert actual_response == expected_response
        presenter.raise_invalid_phone_number_exception.assert_called_once_with(
            phone_number=["333"])

    def test_no_sms_provider_configs_exists_then_raise_exception(
            self, interactor, presenter, storage):
        # Arrange
        from unittest.mock import Mock

        phone_numbers = ["9949856434", "9949856434"]
        text = "Hi, Nice to see you here!!"
        expected_response = Mock()
        sms_provider_details = []

        presenter.raise_no_sms_provider_configs_exists_exception.\
            return_value = expected_response
        storage.get_sms_provider_configs.return_value = sms_provider_details

        # Act
        actual_response = interactor.send_sms_wrapper(
            phone_numbers=phone_numbers, text=text, presenter=presenter)

        # Assert
        assert actual_response == expected_response
        presenter.raise_no_sms_provider_configs_exists_exception.\
            assert_called_once()
        storage.get_sms_provider_configs.assert_called_once_with(is_active=True)

    @pytest.fixture()
    def sms_provider_mock(self, storage):
        from sms_provider.interactors.sms_provider_interactor \
            import SMSProviderInteractor
        from unittest.mock import create_autospec

        return SMSProviderInteractor(storage=storage)

    def test_given_valid_details_then_send_sms(
            self, interactor, storage, presenter):
        # Arrange
        from unittest.mock import Mock
        from sms_provider.interactors.storage_interfaces.dtos import SMSProviderConfigDTO
        from sms_provider.constants.enums import SMSProvider

        phone_numbers = ["9949856434", "9941856434", "9949856435", "9949856436",
                         "9949856437", "9949856438", "9949856439", "9949156434",
                         "9949836434", "9949855434", "9949856734", "9949856834"]
        text = "Hi, Nice to see you here!!"
        expected_response = Mock()
        sms_provider_details = [
            SMSProviderConfigDTO(
                id="123e4567-e89b-12d3-a456-426614174000",
                sms_provider=SMSProvider.TWILIO.value,
                throughput=5),
            SMSProviderConfigDTO(
                id="123e4567-e89b-12d3-a456-426614174000",
                sms_provider=SMSProvider.JIO.value,
                throughput=6),
            SMSProviderConfigDTO(
                id="123e4567-e89b-12d3-a456-426614174000",
                sms_provider=SMSProvider.AIRTEL.value,
                throughput=8)
        ]

        storage.get_sms_provider_configs.return_value = sms_provider_details

        # Act
        actual_response = interactor.send_sms_wrapper(
            phone_numbers=phone_numbers, text=text, presenter=presenter)

        # Assert
        assert actual_response == expected_response
        storage.get_sms_provider_configs.assert_called_once_with(is_active=True)
