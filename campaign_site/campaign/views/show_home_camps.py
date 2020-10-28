from django.http import JsonResponse
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render
from commons.views.basic_view import BasicView
from campaign.models import campaign_entity,registered_users
from identity.models import UserEntity

from campaign.serializers.camps_home_serializer import CampsHomeSerializer


class ShowHomeCamps(BasicView, APIView):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def get(self, request):
        user_entity = get_object_or_404(UserEntity, student_code=self.user.student_code)
        accessible_camps = campaign_entity.objects.filter(gender=user_entity.gender,year_of_entry=user_entity.year_of_entry,
                                                          is_verified=1)
        #todo which camp is registered by user
        camps_serializer=CampsHomeSerializer(accessible_camps,many=True)

        return Response(camps_serializer.data, status=status.HTTP_200_OK)