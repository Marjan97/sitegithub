from django.urls import path
from identity.views.otp_mobile_phone_sms import *


urlpatterns = [
    # path('login/', mobile_login, name='mobile_login'),
    path('', register_view, name='register_view'),
    path('verify/', verify, name='verify'),

    path('dashboard/', dashboard, name='dashboard'),
]
