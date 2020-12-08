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

from reserve.serializers.camps_home_serializer import CampsHomeSerializer


class ShowHomeCamps(BasicView, APIView):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def get(self, request):
        user_registered_and_unregistered_accessible_camps = CampaignEntity.objects.filter(
            gender=self.user.gender,
            year_of_entry__contains=self.user.year_of_entry,
            is_verified=1,
            capacity__gt=0,
        )

        user_registered_accessible_camp_ids = user_registered_and_unregistered_accessible_camps.filter(
            registered_users__user_id=self.user.id).values_list(PayloadParamName.id, flat=True)

        result: List = []

        for user_registered_and_unregistered_accessible_camp_elem in user_registered_and_unregistered_accessible_camps:
            camp_dict: Dict = {
                PayloadParamName.id: user_registered_and_unregistered_accessible_camp_elem.id,
                PayloadParamName.name: user_registered_and_unregistered_accessible_camp_elem.name,
                PayloadParamName.description: user_registered_and_unregistered_accessible_camp_elem.description,
                PayloadParamName.is_registered: True if user_registered_and_unregistered_accessible_camp_elem.id in user_registered_accessible_camp_ids else False,
            }

            result.append(camp_dict)
        # user_registered_accessible_campaigns = accessible_camps.filter(
        #     registered_users__user_id=self.user.id).values_list(PayloadParamName.id, flat=True)

        # todo which camp is registered by user
        # camps_serializer = CampsHomeSerializer(accessible_camps, many=True)

        response_dict: Dict = {
            PayloadParamName.result: result,
        }

        return Response(data=response_dict, status=status.HTTP_200_OK)
