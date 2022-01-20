import json

from rest_framework.views import APIView
from django.http import HttpResponse


class LoginView(APIView):

    def post(self, request):
        from crm.interactors.login_interactor import LoginInteractor
        from crm.storages.storage_implementation import StorageImplementation
        from crm.presenters.login_presenter_implementation import LoginPresenterImplementation

        try:
            request_body = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(status=400, content="InvalidRequestData")

        storage = StorageImplementation()
        interactor = LoginInteractor(storage=storage)
        response = interactor.login_wrapper(
            username=request_body["username"], password=request_body["password"],
            presenter=LoginPresenterImplementation())

        return response
