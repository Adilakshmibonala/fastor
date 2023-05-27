from rest_framework import routers
from user.views.register_user import UserSignUpViewSet

router = routers.DefaultRouter()
router.register(prefix=r'signup', viewset=UserSignUpViewSet, basename="UserSignUp")
