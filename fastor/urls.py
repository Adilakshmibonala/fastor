"""fastor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from apscheduler.schedulers.background import BackgroundScheduler
from sms_provider.schedulers import retrigger_falied_msgs
from django.conf import settings

api = []
apps = ["crm", "sms_provider"]

for app_name in apps:
    try:
        api.append(url(r'^' + app_name + '/', include(app_name + '.urls')))
    except ImportError:
        pass

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api)),
    path('api/token/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]

scheduler = BackgroundScheduler()
scheduler.add_job(retrigger_falied_msgs.re_trigger_failed_msgs,
                  trigger='cron', hour=settings.TASK_RUNNER_HOURS,
                  minute=settings.TASK_RUNNER_MINUTES, max_instances=1)
scheduler.start()
