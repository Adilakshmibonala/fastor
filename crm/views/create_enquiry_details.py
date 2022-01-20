import json

from rest_framework.views import APIView
from django.http import HttpResponse


class CreateEquityDetailsView(APIView):

    def post(self, request):
        from crm.interactors.create_enquiry_details_interactor import CreateEquityDetailsInteractor
        from crm.storages.storage_implementation import StorageImplementation
        from crm.interactors.dtos import EnquiryDetailsDTO
        from crm.presenters.create_enquiry_details_presenter_implementation import \
            CreateEquityDetailsPresenterImplementation

        try:
            request_body = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(status=400, content="InvalidRequestData")

        storage = StorageImplementation()
        interactor = CreateEquityDetailsInteractor(storage=storage)
        presenter = CreateEquityDetailsPresenterImplementation()
        enquiry_details = EnquiryDetailsDTO(
            username=request_body["username"],
            email=request_body["email"],
            phone_number=request_body["phone_number"],
            country_code=request_body["country_code"],
            course_name=request_body["course_name"])
        response = interactor.create_enquiry_details_wrapper(
            enquiry_details=enquiry_details, presenter=presenter)

        if response is None:
            response = HttpResponse(status=200, content="SuccessResponse")

        return response
