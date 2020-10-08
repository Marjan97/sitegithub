from django.contrib.auth import login
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.urls import reverse
from django.shortcuts import render
from identity.models import UserEntity
from identity import forms,helper_send_otp
from identity.serializers.mobile_login_serializers import mobileloginserializer



# Create your views here.
# @api_view(['POST'])
class mobile_phone_login(APIView):
    # def get (self,request):
    #     Users = UserEntity.objects.all()
    #     userserializer = mobileloginserializer(Users, many=True)
    #     return Response(userserializer.data)

    def post(self, request):


            userserializer=mobileloginserializer(mobile_phone_number=request.data)
            # print ('error')

            otp = helper_send_otp.get_random_otp() # create otp
            helper_send_otp.send_otp_soap(userserializer.mobile_phone_number, otp)
            userserializer.otp = otp# send otp
            if userserializer.is_valid():
             userserializer.save()
             print (otp)  # check value of otp
             # request.session['user_mobile'] = user.mobile_phone_number
             return Response(userserializer.mobile_phone_number)
            return JsonResponse(userserializer.errors, status=status.HTTP_400_BAD_REQUEST)








def verify_otp_login(request):

    mobile = request.session.get('user_mobile')
    return render (request,'verify_otp_login.html',{'mobile':mobile})




def dashboard(request):
    return render (request , 'dashboard.html')


