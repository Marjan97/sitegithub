from django.urls import path
from identity.views.main_login import main_login
from identity.views.verify_otp_login import verify
from identity.views.user_info_view import UserInfo
from identity.views.otp_mobile_phone_login import MobilePhoneLogin


urlpatterns = [
    # path('login/', mobile_login, name='mobile_login'),
    path('user_info/', UserInfo.as_view(), name='UserInfo'),
    path('login/', main_login.as_view(), name='main_login'),
    path('verify/', verify.as_view(), name='verify_otp_login'),

]
