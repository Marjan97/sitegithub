from django.urls import path
from identity.views.otp_mobile_phone_login import MobilePhoneLogin
from identity.views.verify_otp_login import verify
from identity.views.user_info_view import UserInfo

urlpatterns = [
    # path('login/', mobile_login, name='mobile_login'),
    path('user_info/', UserInfo.as_view(), name='UserInfo'),
    path('register/', MobilePhoneLogin.as_view(), name='MobilePhoneLogin'),
    path('verify/', verify.as_view(), name='verify_otp_login'),
]
