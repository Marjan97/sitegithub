from rest_framework import serializers
from campaign.models import campaign_entity



class CampsCreateFormSerializer(serializers.ModelSerializer):

    image=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = campaign_entity
        fields = [
            'name',
            'description',
            'gender',
            'year_of_entry',
            'capacity',
            'cost',
            'image',
        ]

    # def create(self, validated_data):
    #     return campaign_entity(**validated_data)
