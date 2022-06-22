import pytest


class TestSendSMSInteractor:

    @pytest.fixture()
    def storage(self):
        from crm.interactors.storage_interfaces. \
            storage_interface import StorageInterface

        from unittest.mock import create_autospec
        return create_autospec(StorageInterface)

