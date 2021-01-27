from rest_framework import serializers

from reserve.models.registered_users import RegisteredUsers


class CampsRegisteredUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredUsers
        fields = [
            'user',
            'campaign',

        ]


