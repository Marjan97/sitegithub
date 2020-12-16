from django.urls import path

from reserve.views.camp_create import CampCreate
from reserve.views.all_user_accessible_campaign_view import ShowHomeCamps
from reserve.views.user_accessible_campaign_detail_view import CampDetails

urlpatterns = [

    path('camp/detail/', ShowHomeCamps.as_view(), name='ShowHomeCamps'),
    path('camp/detail/<int:camp_id>/', CampDetails.as_view(), name='CampDetails'),
    path('camp_create/', CampCreate.as_view(), name='CampCreate'),

]
