from rest_framework import serializers
from reserve.models import campaign_entity


class CampsHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = campaign_entity
        fields = ['name',]