from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from commons.views.basic_view import BasicView
from commons.views.payload_param_name import PayloadParamName


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
        # initial_data = request.data
        # initial_data[PayloadParamName.student_code] = self.user.student_code
        # serializer = UserProfileSerializer(data=initial_data)
        #
        # if serializer.is_valid():
        #     serializer.save()
        self.user.mobile_phone_number = request.data.get(PayloadParamName.mobile_phone_number)
        self.user.account_number = request.data.get(PayloadParamName.account_number)
        self.user.email = request.data.get(PayloadParamName.email)
        self.user.save()
        result = dict()
        result[PayloadParamName.success] = "آپدیت پروفایل با موفقیت انجام شد."
        return Response(data=result, status=status.HTTP_200_OK)

    # return Response(status=status.HTTP_400_BAD_REQUEST)
