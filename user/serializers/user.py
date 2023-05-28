from rest_framework import serializers
from user.constants.enums import Gender
from django.contrib.auth import get_user_model


class RegisterUserRequestValidationSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    gender = serializers.ChoiceField(required=True, choices=Gender.get_list_of_tuples())
    email = serializers.EmailField(required=True)
    phone_number = serializers.IntegerField(required=True)

    class Meta:
        fields = "__all__"


class LoginUserRequestValidationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    class Meta:
        fields = "__all__"


class VerifyOTPRequestValidationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    otp = serializers.IntegerField(required=True)

    class Meta:
        fields = "__all__"


class ResendOTPRequestValidationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    class Meta:
        fields = "__all__"
