from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from commons.views.basic_view import BasicView
from identity.models import UserEntity


class UserInfo(BasicView, APIView):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def get(self, request):
        user_entity = get_object_or_404(UserEntity, student_code=self.user.student_code)
        mobile = request.data.get("mobile_phone_number")
        account_number = request.data.get("account_number")
        user_entity.mobile_phone_number=mobile
        user_entity.account_number=account_number
        user_entity.save()



        return JsonResponse(data={"message":"Data added."}, status=status.HTTP_200_OK)
