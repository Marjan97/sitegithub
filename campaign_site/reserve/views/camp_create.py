from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from commons.views.basic_view import BasicView
from reserve.serializers.camp_create_serializer import CampsCreateFormSerializer


class CampCreate(BasicView, CreateAPIView):
    http_method_names = ['post']
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        camp_object = CampsCreateFormSerializer(data=request.data)
        if camp_object.is_valid():
            camp_object.save()
            return Response(data=camp_object.data, status=status.HTTP_201_CREATED)
        return JsonResponse(camp_object.errors, status=status.HTTP_400_BAD_REQUEST)
