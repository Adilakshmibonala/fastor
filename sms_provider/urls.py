from django.urls import path
from sms_provider.views.login import LoginView
from sms_provider.views.send_sms import SendSMSView


urlpatterns = [
    path('login/v1/', LoginView.as_view(), name='login'),
    path('send_sms/v1/', SendSMSView.as_view(), name='send_sms')
]