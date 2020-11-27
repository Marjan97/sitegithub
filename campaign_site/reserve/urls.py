from django.urls import path

from reserve.views.camp_create import CampCreate
from reserve.views.show_home_camps import ShowHomeCamps
from reserve.views.camp_detail import CampDetails

urlpatterns = [

    path('home/camps/', ShowHomeCamps.as_view(), name='ShowHomeCamps'),
    path('camp/detail/<int:id>/', CampDetails.as_view(), name='CampDetails'),
    path('camp_create/', CampCreate.as_view(), name='CampCreate'),

]
