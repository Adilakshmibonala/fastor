from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from user.constants.enums import Gender


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have a email')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=200, unique=True)
    phone_number = models.IntegerField(max_length=10)
    gender = models.CharField(max_length=10, choices=Gender.get_list_of_tuples())
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return "User - %s %s" % (self.email, self.gender)


class UserOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    expiration_time = models.DateTimeField()

    def __str__(self):
        return "OTP - %s %s" % (self.user, self.otp)
