from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4

from crm.constants.enums import UserType


class UserAccount(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True)
    user_type = models.CharField(max_length=50, choices=UserType.get_list_of_tuples())
    created_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return "%s %s" % (str(self.id), self.user_type)


class EnquiryDetails(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    username = models.CharField(max_length=256)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    country_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=256)
    is_public_enquiry = models.BooleanField(default=True)
    submitted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (str(self.id), self.username)


class UserEnquiryDetails(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    enquiry_details = models.OneToOneField(EnquiryDetails, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (str(self.id))
