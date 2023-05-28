from user.interactors.dtos import RegisterUserDetailsDTO
from user.interactors.storage_interface.storage_interface import StorageInterface
from user.models import User, UserOTP


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

    def get_user_phone_number(self, email: str):
        from user.exceptions.custom_exceptions import UserDoesNotExistsException
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExists:
            raise UserDoesNotExistsException()
        return user.phone_number

    def create_user_otp(self, user_id: int, otp: str):
        from django.utils import timezone
        expiration_time = timezone.now() + timezone.timedelta(minutes=5)
        UserOTP.objects.update_or_create(user_id=user_id, otp=otp, expiration_time=expiration_time)

    def validate_otp(self, email: str, otp: int):
        from django.utils import timezone
        from user.exceptions.custom_exceptions import InvalidOTPException

        try:
            UserOTP.objects.get(
                user__email=email, otp=otp, expiration_time__gte=timezone.now())
        except UserOTP.DoesNotExists:
            raise InvalidOTPException()
