from django.urls import path
from identity.views.otp_mobile_phone_login import MobilePhoneLogin, dashboard
from identity.views.verify_otp_login import verify

urlpatterns = [
    # path('login/', mobile_login, name='mobile_login'),
    path('register/', MobilePhoneLogin.as_view(), name='mobile_phone_login'),
    path('verify/', verify.as_view(), name='verify_otp_login'),
    path('dashboard/', dashboard, name='dashboard'),
]
