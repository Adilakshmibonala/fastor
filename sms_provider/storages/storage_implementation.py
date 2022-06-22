from sms_provider.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from sms_provider.exceptions import custom_exceptions
from sms_provider.models.sms_details import *


class StorageImplementation(StorageInterface):

    def get_user_password(self, email: str) -> str:
        try:
            user_account = UserAccount.objects.get(email=email)
        except UserAccount.DoesNotExist:
            raise custom_exceptions.UserDoesNotExistException()

        return user_account.password

