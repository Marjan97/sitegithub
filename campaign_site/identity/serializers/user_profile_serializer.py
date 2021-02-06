from rest_framework import serializers

from commons.views.payload_param_name import PayloadParamName
from identity.models import UserEntity


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEntity
        fields = [
            PayloadParamName.account_number,
            PayloadParamName.email,
            PayloadParamName.mobile_phone_number,
            PayloadParamName.student_code,
        ]
        read_only_fields = [
            PayloadParamName.student_code,
        ]
