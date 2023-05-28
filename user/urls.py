from rest_framework import routers
from user.views.login import LoginViewSet
from user.views.logout import LogoutViewSet
from user.views.register_user import UserSignUpViewSet
from user.views.resend_otp import ResendOTPView
from user.views.verify_otp import VerifyOTPView

router = routers.DefaultRouter()
router.register(prefix=r'signup', viewset=UserSignUpViewSet, basename="UserSignUp")
router.register(prefix=r'login', viewset=LoginViewSet, basename="UserLogin")
router.register(prefix=r'logout', viewset=LogoutViewSet, basename="UserLogout")
router.register(prefix=r'otp/verify', viewset=VerifyOTPView, basename="VerifyOTP")
router.register(prefix=r'otp/resend', viewset=ResendOTPView, basename="ResendOTP")
