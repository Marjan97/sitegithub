# from rest_framework import serializers
# from reserve.models import CampaignEntity
#
#
# class CampsHomeSerializer(serializers.ModelSerializer):
#     is_registered = serializers.SerializerMethodField('_get_campaign_is_registered_parameter')
#
#     def _get_campaign_is_registered_parameter(self, _campaign_entity):
#     user_registered_accessible_camp_ids = _campaign_entity.filter(
#         registered_users__user_id=self.user.id).values_list(PayloadParamName.id, flat=True)
#
#     class Meta:
#         model = CampaignEntity
#         fields = [
#             'id',
#             'name',
#         ]
