from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render
from commons.views.basic_view import BasicView
from reserve.models.campaign_entity import CampaignEntity
from identity.models import UserEntity
from reserve.serializers.camp_create_serializer import CampsCreateFormSerializer


class CampCreate(BasicView, APIView):
    http_method_names = ['post']
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def post(self, request):
        camp_object = CampsCreateFormSerializer(data=request.data)
        if camp_object.is_valid():
            camp_object.save()
            return JsonResponse(data={"message": 'camp created'}, status=status.HTTP_201_CREATED)
        return JsonResponse(camp_object.errors, status=status.HTTP_400_BAD_REQUEST)
