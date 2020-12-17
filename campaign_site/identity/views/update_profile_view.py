from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from commons.models import BaseEntity
from commons.views.basic_view import BasicView
from commons.views.payload_param_name import PayloadParamName
from identity.models import UserEntity
from identity.serializers.user_profile_serializer import UserProfileSerializer


class UserProfileViewViewSet(BasicView, APIView):
    # queryset = UserEntity.objects.all()
    # serializer_class = UserProfileSerializer
    # http_method_names = ['put']
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(data=request.data)

        if serializer.is_valid():
            self.user.mobile_phone_number = request.data.get(PayloadParamName.mobile_phone_number)
            self.user.account_number = request.data.get(PayloadParamName.account_number)
            self.user.email = request.data.get(PayloadParamName.email)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST)
