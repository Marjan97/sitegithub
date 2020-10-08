from django.contrib.auth import login
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.urls import reverse
from django.shortcuts import render
from identity.models import UserEntity
from identity import forms, helper_send_otp
from identity.serializers.mobile_login_serializers import mobileloginserializer


# Create your views here.
# @api_view(['POST'])
class mobile_phone_login(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, request):
        Users = UserEntity.objects.all()
        userserializer = mobileloginserializer(Users, many=True)
        return Response(userserializer.data)

    def post(self, request, *args, **kwargs):
        mobile_phone_number = request.data.get("mobile_phone_number")
        user_entity = get_object_or_404(UserEntity, mobile_phone_number=mobile_phone_number)
        otp = helper_send_otp.get_random_otp()  # create otp
        helper_send_otp.send_otp_soap(mobile_phone_number, otp)
        user_entity.otp = otp  # send otp
        user_entity.save()

        return JsonResponse(data={"mobile_phone_number": mobile_phone_number}, status=status.HTTP_200_OK)


def verify_otp_login(request):
    mobile = request.session.get('user_mobile')
    return render(request, 'verify_otp_login.html', {'mobile': mobile})


def dashboard(request):
    return render(request, 'dashboard.html')
