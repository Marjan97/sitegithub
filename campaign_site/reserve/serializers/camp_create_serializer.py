from rest_framework import serializers

from reserve.models.campaign_entity import CampaignEntity


class CampsCreateFormSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = CampaignEntity
        fields = [
            'name',
            'description',
            'gender',
            'year_of_entry',
            'capacity',
            'cost',
            'image',
            'is_verified',
        ]

    # def create(self, validated_data):
    #     return campaign_entity(**validated_data)
