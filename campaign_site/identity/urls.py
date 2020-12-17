from django.urls import path
from rest_framework import routers

from identity.views.main_login import main_login
from identity.views.update_profile_view import UserProfileViewViewSet
from identity.views.user_info_view import UserInfo
from identity.views.verify_otp_login import verify

router = routers.DefaultRouter()
# router.register('profile_update', UserProfileViewViewSet, basename='profile_update')

urlpatterns = [
    # path('login/', mobile_login, name='mobile_login'),
    path('user_info/', UserInfo.as_view(), name='UserInfo'),
    path('login/', main_login.as_view(), name='main_login'),
    path('verify/', verify.as_view(), name='verify_otp_login'),
    path('profile/update/', UserProfileViewViewSet.as_view(), name='update_profile'),

]

urlpatterns += router.urls
