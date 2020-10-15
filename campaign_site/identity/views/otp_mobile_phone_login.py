from django.http import JsonResponse
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render

from commons.views.basic_view import BasicView
from identity.models import UserEntity
from identity.manager import helper_send_otp
from identity.serializers.mobile_login_serializers import mobileloginserializer


# Create your views here.
# @api_view(['POST'])
class MobilePhoneLogin(BasicView, APIView):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, request):
        Users = UserEntity.objects.all()
        userserializer = mobileloginserializer(Users, many=True)
        return Response(userserializer.data)

    def post(self, request, *args, **kwargs):
        
        mobile_phone_number = request.data.get("mobile_phone_number")
        user_entity = get_object_or_404(UserEntity, mobile_phone_number=mobile_phone_number)
        # todo change mobile to code
        otp = helper_send_otp.get_random_otp()  # create otp
        helper_send_otp.send_otp_soap(mobile_phone_number, otp)
        user_entity.otp = otp
        user_entity.set_password(otp)
        user_entity.save()
        return JsonResponse(data={"mobile_phone_number": mobile_phone_number, "message": 'otp sent'},
                            status=status.HTTP_200_OK)


def dashboard(request):
    return render(request, 'dashboard.html')
