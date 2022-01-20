from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4

from crm.constants.enums import UserType


class UserAccount(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True)
    user_type = models.CharField(max_length=50, choices=UserType.get_list_of_tuples())

