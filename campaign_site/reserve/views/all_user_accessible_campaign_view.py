from datetime import datetime
from typing import List, Dict

from django.http import JsonResponse
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render
from commons.views.basic_view import BasicView
from commons.views.payload_param_name import PayloadParamName
from reserve.models import campaign_entity, registered_users, CampaignEntity
from identity.models import UserEntity
from reserve.serializers.camp_detail_sreializer import CampsDetailsSerializer


class ShowHomeCamps(BasicView, APIView):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        user_registered_and_unregistered_accessible_camps = CampaignEntity.objects.filter(
            gender=self.user.gender,
            year_of_entry__contains=self.user.year_of_entry,
            is_verified=1,
            capacity__gt=0,
            # execution_time__lt=datetime.now(),
        )

        # todo which camp is registered by user
        camps_serializer = CampsDetailsSerializer(user_registered_and_unregistered_accessible_camps, many=True,
                                                  context={
                                                      PayloadParamName.user_id: self.user.id,
                                                  })

        response_dict: Dict = {
            PayloadParamName.result: camps_serializer.data,
            PayloadParamName.count: len(camps_serializer.data),
        }

        return Response(data=response_dict, status=status.HTTP_200_OK)
