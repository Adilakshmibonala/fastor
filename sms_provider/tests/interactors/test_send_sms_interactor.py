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


