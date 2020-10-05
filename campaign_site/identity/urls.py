from django.urls import path
from identity.views.otp_mobile_phone_login import *


urlpatterns = [
    # path('login/', mobile_login, name='mobile_login'),
    path('register', mobile_phone_login, name='mobile_phone_login'),
    path('verify/', verify_otp_login, name='verify_otp_login'),
    path('dashboard/', dashboard, name='dashboard'),
]
