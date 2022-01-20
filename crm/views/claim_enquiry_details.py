import json
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from django.http import HttpResponse


class ClaimEnquiryDetailsView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        from crm.interactors.claim_enquiry_details_interactor import ClaimEnquiryDetailsInteractor
        from crm.presenters.claim_enquiry_details_presenter_implementation import \
            ClaimEnquiryDetailsPresenterImplementation
        from crm.storages.storage_implementation import StorageImplementation

        try:
            request_body = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(status=400, content="InvalidRequestData")

        user_id = str(request.user.id)
        storage = StorageImplementation()
        presenter = ClaimEnquiryDetailsPresenterImplementation()
        interactor = ClaimEnquiryDetailsInteractor(storage=storage)
        response = interactor.claim_enquiry_details_wrapper(
            user_id=user_id, enquiry_details_id=request_body["enquiry_details_id"],
            presenter=presenter)

        if response is None:
            response = HttpResponse(status=200, content="SuccessResponse")

        return response
