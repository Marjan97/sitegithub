from rest_framework import serializers

from reserve.models.registered_users_entity import RegisteredUsersEntity


class CampsRegisteredUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredUsersEntity
        fields = [
            'user',
            'campaign',

        ]


