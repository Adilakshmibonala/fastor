import json

from rest_framework.views import APIView
from django.http import HttpResponse

from authentication.serializers.login_serializer import \
    LoginSerializer


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        from authentication.interactors.login_interactor import LoginInteractor
        from authentication.storages.storage_implementation import StorageImplementation
        from authentication.presenters.login_presenter_implementation import LoginPresenterImplementation

        try:
            request_body = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(status=400, content="InvalidRequestData")

        storage = StorageImplementation()
        interactor = LoginInteractor(storage=storage)
        response = interactor.login_wrapper(
            email=request_body["email"], password=request_body["password"],
            presenter=LoginPresenterImplementation())

        return response
