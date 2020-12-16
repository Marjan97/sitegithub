from rest_framework import serializers

from commons.views.payload_param_name import PayloadParamName
from reserve.models import campaign_entity, CampaignEntity


class CampsDetailsSerializer(serializers.ModelSerializer):
    is_registered = serializers.SerializerMethodField('_get_campaign_is_registered_parameter')

    def _get_campaign_is_registered_parameter(self, _campaign_entity: CampaignEntity):
        user_id = self.context.get(PayloadParamName.user_id)
        if user_id:
            return user_id in _campaign_entity.registered_users.values_list(PayloadParamName.id, flat=True)
        return False

    class Meta:
        model = CampaignEntity
        fields = [
            PayloadParamName.id,
            PayloadParamName.name,
            PayloadParamName.description,
            PayloadParamName.gender,
            PayloadParamName.year_of_entry,
            PayloadParamName.capacity,
            PayloadParamName.cost,
            PayloadParamName.execution_time,
            PayloadParamName.is_registered,
        ]
