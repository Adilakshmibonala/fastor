from django.urls import path
from crm.views.login import LoginView
from crm.views.get_enquiry_details import GetEnquiryDetailsView
from crm.views.create_enquiry_details import CreateEquityDetailsView
from crm.views.claim_enquiry_details import ClaimEnquiryDetailsView


urlpatterns = [
    path('login/v1/', LoginView.as_view(), name='login'),
    path('enquiries/v1/', GetEnquiryDetailsView.as_view(), name='get_enquiry_details'),
    path('enquiry/create/v1/', CreateEquityDetailsView.as_view(), name='create_enquiry_details'),
    path('enquiry/claim/v1/', ClaimEnquiryDetailsView.as_view(), name='claim_enquiry_details'),
]
