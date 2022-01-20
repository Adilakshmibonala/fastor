from django.urls import path
from crm.views.login import LoginView


urlpatterns = [
    path('login/v1/', LoginView.as_view(), name='login'),
]
