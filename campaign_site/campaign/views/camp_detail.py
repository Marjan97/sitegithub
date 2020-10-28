from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render
from commons.views.basic_view import BasicView
from campaign.models.campaign_entity import CampaignEntity
from identity.models import UserEntity
from campaign.serializers.camp_detail_sreializer import CampsDetailsSerializer


class CampDetails(BasicView, APIView):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def get_obj(self, id):
        try:
            return CampaignEntity.objects.get(id=id)
        except CampaignEntity.DoesNotExist:
            return JsonResponse(data={"message": 'Camp DoesNotExist '}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        camp_entity = self.get_obj(id)
        camp_serializer = CampsDetailsSerializer(camp_entity)
        return JsonResponse(camp_serializer.data, status=status.HTTP_200_OK)
