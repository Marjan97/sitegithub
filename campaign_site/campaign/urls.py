from django.urls import path
from campaign.views.show_home_camps import ShowHomeCamps
from campaign.views.camp_detail import CampDetails
from campaign.views.camp_create import CampCreate


urlpatterns = [

    path('home/camps/', ShowHomeCamps.as_view(), name='ShowHomeCamps'),
    path('camp/detail/<int:id>/', CampDetails.as_view(), name='CampDetails'),
    path('camp_create/', CampCreate.as_view(), name='CampCreate'),

]