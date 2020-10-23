from identity.models import UserEntity
from django.http import JsonResponse
from identity.manager.send_otp_helper import SendOTPHelper
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from commons.views.basic_view import BasicView


class verify(BasicView,APIView):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def post(self,request):

        mobile = request.data.get("mobile_phone_number")
        user = get_object_or_404(UserEntity, mobile_phone_number=mobile)


        # check otp expiration
        if not SendOTPHelper.check_otp_expiration(user.mobile_phone_number):
            return JsonResponse(data={"message": "OTP is expired"}, status=status.HTTP_200_OK)
        # check value of otp
        if user.otp != int(request.data.get("otp")):
            return JsonResponse(data={"message": "OTP is not correct"}, status=status.HTTP_200_OK)

        user.is_active = True
        user.save()
        return JsonResponse(data={"message":"OTP is correct"}, status=status.HTTP_200_OK)



