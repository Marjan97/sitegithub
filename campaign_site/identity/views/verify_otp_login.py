from identity.models import UserEntity
from django.contrib.auth import login
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from rest_framework.response import Response
from django.urls import reverse
from django.shortcuts import render
from identity import helper_send_otp
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class verify(APIView):
    def post(self,request):

        mobile = request.data.get("mobile_phone_number")
        user = get_object_or_404(UserEntity, mobile_phone_number=mobile)


        # check otp expiration
        if not helper_send_otp.check_otp_expiration(user.mobile_phone_number):
            return JsonResponse(data={"message": "OTP is expired"}, status=status.HTTP_200_OK)
        # check value of otp
        if user.otp != int(request.data.get("otp")):
            return JsonResponse(data={"message": "OTP is not correct"}, status=status.HTTP_200_OK)

        user.is_active = True
        user.save()
        return JsonResponse(data={"message":"OTP is correct"}, status=status.HTTP_200_OK)



