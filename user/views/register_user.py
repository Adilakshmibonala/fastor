from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from user.serializers.register_user import \
    RegisterUserRequestValidationSerializer, RegisterUserSerializer


class UserSignUpViewSet(viewsets.GenericViewSet):
    serializer_class = RegisterUserRequestValidationSerializer

    def create(self, request):
        request_data = request.data
        register_user_validation_serializer = \
            RegisterUserRequestValidationSerializer(data=request_data)
        register_user_validation_serializer.is_valid(raise_exception=True)

        register_user_serializer = RegisterUserSerializer(data=request_data)
        user = register_user_serializer.save()

        return Response(data={"id": user.id}, status=status.HTTP_201_CREATED)
