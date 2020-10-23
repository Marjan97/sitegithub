from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render
from commons.views.basic_view import BasicView
from reserve.models import campaign_entity
from identity.models import UserEntity
from reserve.serializers.camp_detail_sreializer import CampsDetailsSerializer


class CampDetails(BasicView, APIView):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def get_obj(self,id):
        try:
           return campaign_entity.objects.get(id=id)
        except campaign_entity.DoesNotExist:
            return JsonResponse(data={"message": 'Camp DoesNotExist '},status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        camp_id=self.get_obj(id)
        camp_serializer = CampsDetailsSerializer(camp_id)
        return JsonResponse(camp_serializer.data, status=status.HTTP_200_OK)


