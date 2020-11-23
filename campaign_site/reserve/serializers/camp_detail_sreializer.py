from rest_framework import serializers
from reserve.models import campaign_entity


class CampsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = campaign_entity
        fields = [
            'id',
            'name',
            'description',
            'gender',
            'year_of_entry',
            'capacity',
            'cost',
        ]
