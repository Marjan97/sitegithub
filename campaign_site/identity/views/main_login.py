from identity.models import UserEntity
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from commons.views.basic_view import BasicView


class main_login(BasicView, APIView):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def post(self, request):

        student_code = request.data.get("student_code")
        national_code = request.data.get("password")

        user = get_object_or_404(UserEntity, student_code=student_code)
        # user.set_password(national_code)
        # user.save()

        if user.student_code != student_code:
            return JsonResponse(data={"message": "student_code is not correct"}, status=status.HTTP_200_OK)
        if user.national_code != national_code:
            return JsonResponse(data={"message": "national_code is not correct"}, status=status.HTTP_200_OK)

        user.is_active = True
        user.save()
        return JsonResponse(data={"message": "Welcome!!!"}, status=status.HTTP_200_OK)
