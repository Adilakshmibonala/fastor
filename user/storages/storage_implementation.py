from user.interactors.dtos import RegisterUserDetailsDTO
from user.interactors.storage_interface.storage_interface import StorageInterface
from user.models import User


class StorageImplementation(StorageInterface):

    def check_is_user_already_registered(self, email: str) -> bool:
        return User.objects.filter(email=email).exists()

    def register_user(self, register_user_details_dto: RegisterUserDetailsDTO) -> int:
        user_obj = User.objects.create(
            first_name=register_user_details_dto.first_name,
            last_name=register_user_details_dto.last_name,
            gender=register_user_details_dto.gender,
            email=register_user_details_dto.email,
            phone_number=register_user_details_dto.phone_number)
        return user_obj.id
