from rest_framework import serializers
from identity.models import UserEntity


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEntity
        fields = [
            'mobile_phone_number',
            'account_number',
            'first_name',
            'last_name',
            'user_type',
            'student_code',
            'field_of_study',
            'year_of_entry',
        ]
