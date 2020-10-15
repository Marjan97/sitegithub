from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from commons.views.basic_view import BasicView
from identity.models import UserEntity
from identity.serializers.user_info_serializer import UserInfoSerializer


class UserInfo(BasicView, APIView):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def get(self, request):
        user_entity = get_object_or_404(UserEntity, student_code=self.user.student_code)
        user_serializer = UserInfoSerializer(user_entity)

        return Response(user_serializer.data, status=status.HTTP_200_OK)
