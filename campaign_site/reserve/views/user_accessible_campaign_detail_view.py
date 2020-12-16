from typing import List

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from commons.views.basic_view import BasicView
from commons.views.payload_param_name import PayloadParamName
from reserve.models.campaign_entity import CampaignEntity
from identity.models import UserEntity
from reserve.serializers.camp_detail_sreializer import CampsDetailsSerializer


class CampDetails(BasicView, APIView):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def _get_object(self, id):
        try:
            return CampaignEntity.objects.get(id=id)
        except CampaignEntity.DoesNotExist:
            return JsonResponse(data={
                "message": "campaign does not exists!",
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, *args, **kwargs):
        # todo add permissions here
        camp_id = kwargs.get(PayloadParamName.camp_id)
        camp_entity = self._get_object(camp_id)
        camp_serializer = CampsDetailsSerializer(camp_entity, context={
            PayloadParamName.user_id: self.user.id,
        })

        return Response(data=camp_serializer.data, status=status.HTTP_200_OK)
