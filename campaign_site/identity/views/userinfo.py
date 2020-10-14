from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.urls import reverse
from django.shortcuts import render
from commons.views.basic_view import BasicView
from identity.models import UserEntity
from identity.serializers.userifo_serializer import UserInfoSerializer


class UserInfo(BasicView, APIView):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, request):
        # User = get_object_or_404(UserEntity,student_code=request.data.get("student_code"))
        # student_code = request.data.get("student_code")
        User =get_object_or_404(UserEntity, student_code=self.user.student_code)
        userserializer = UserInfoSerializer(User)
        return Response(userserializer.data)

