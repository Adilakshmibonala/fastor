from django.urls import path
from crm.views.login import LoginView
from crm.views.get_enquiry_details import GetEnquiryDetailsView


urlpatterns = [
    path('login/v1/', LoginView.as_view(), name='login'),
    path('enquiries/v1/', GetEnquiryDetailsView.as_view(), name='get_enquiry_details'),
]
