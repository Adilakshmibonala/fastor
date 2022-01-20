import pytest

from unittest.mock import Mock


class TestGetEnquiryDetailsInteractor:

    @pytest.fixture()
    def storage(self):
        from crm.interactors.storage_interfaces. \
            storage_interface import StorageInterface

        from unittest.mock import create_autospec
        return create_autospec(StorageInterface)

    @pytest.fixture()
    def presenter(self):
        from crm.interactors.presenter_interfaces.\
            get_enquiry_details_presenter_interface import \
            GetEnquiryDetailsPresenterInterface

        from unittest.mock import create_autospec
        return create_autospec(GetEnquiryDetailsPresenterInterface)

    @pytest.fixture()
    def interactor(self, storage):
        from crm.interactors.get_enquiry_details_interactor \
            import GetEnquiryDetailsInteractor
        interactor = GetEnquiryDetailsInteractor(storage=storage)
        return interactor

    def test_given_valid_details_return_enquiry_details(
            self, interactor, storage, presenter):
        # Arrange
        from crm.interactors.dtos import AllEnquiryDetailsDTO

        expected_response = Mock()
        user_id = "user_id"
        public_enquiry_details = []
        user_claimed_enquiry_details = []

        enquiry_details = AllEnquiryDetailsDTO(
            public_enquiry_details=public_enquiry_details,
            user_claimed_enquiry_details=user_claimed_enquiry_details)

        presenter.get_response_for_get_enquiry_details.return_value = expected_response
        storage.get_all_enquiry_details.return_value = public_enquiry_details
        storage.get_user_claimed_enquiry_details.return_value = user_claimed_enquiry_details

        # Act
        actual_response = interactor.get_enquiry_details_wrapper(
            user_id=user_id, presenter=presenter)

        # Assert
        assert actual_response == expected_response
        presenter.get_response_for_get_enquiry_details.assert_called_once_with(
            enquiry_details=enquiry_details)
        storage.get_all_enquiry_details.assert_called_once_with(
            is_public_enquiry=True)
        storage.get_user_claimed_enquiry_details.assert_called_once_with(
            user_id=user_id)
