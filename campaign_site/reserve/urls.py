from django.urls import path
from reserve.views.show_home_camps import ShowHomeCamps
from reserve.views.camp_detail import CampDetails

urlpatterns = [

    path('home/camps/', ShowHomeCamps.as_view(), name='ShowHomeCamps'),
    path('camp/detail/<int:id>/', CampDetails.as_view(), name='CampDetails'),

]
