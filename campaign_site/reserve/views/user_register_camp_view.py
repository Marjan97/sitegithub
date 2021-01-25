from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from reserve.models import CampaignEntity, RegisteredUsers
from identity.models import UserEntity
from rest_framework.generics import get_object_or_404

from commons.views.payload_param_name import PayloadParamName
from reserve.serializers.camp_detail_sreializer import CampsDetailsSerializer

from commons.views.basic_view import BasicView
from reserve.serializers.camp_create_serializer import CampsCreateFormSerializer


class CampRegister(BasicView, CreateAPIView):
    http_method_names = ['post']
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def _get_object(self, id):
        try:
            return CampaignEntity.objects.get(id=id)
        except CampaignEntity.DoesNotExist:
            return JsonResponse(data={
                "message": "campaign does not exists!",
            }, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        camp_id = kwargs.get(PayloadParamName.camp_id)
        camp_entity = self._get_object(camp_id)
        user_entity = get_object_or_404(UserEntity, student_code=self.user.student_code)

        # RegisteredUsers.objects.create(user=user_entity,campaign=camp_entity)

        # user_registered.save()
        # camp_serializer = CampsDetailsSerializer(camp_entity, context={
        #     PayloadParamName.user_id: self.user.id,
        # })
        return Response(status=status.HTTP_200_OK)
