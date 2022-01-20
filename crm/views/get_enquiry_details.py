from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class GetEnquiryDetailsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        from crm.interactors.get_enquiry_details_interactor import GetEnquiryDetailsInteractor
        from crm.storages.storage_implementation import StorageImplementation
        from crm.presenters.get_enquiry_details_presenter_implementation \
            import GetEnquiryDetailsPresenterImplementation

        user_id = str(request.user.id)
        storage = StorageImplementation()
        presenter = GetEnquiryDetailsPresenterImplementation()
        interactor = GetEnquiryDetailsInteractor(storage=storage)
        response = interactor.get_enquiry_details_wrapper(
            user_id=user_id, presenter=presenter)

        return response
