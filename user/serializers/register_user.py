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


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'gender', 'email', 'phone_number']

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
