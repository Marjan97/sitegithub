from commons.manager.base_entity_manager import BaseEntityManager
from commons.models.base_entity import BaseModel
from django.db import models

from identity.enums import UserType


class RegisteredUsers(BaseModel):
    user = models.ForeignKey('identity.UserEntity', on_delete=models.PROTECT, null=False,
                             related_name='registered_campaigns')
    campaign = models.ForeignKey('reserve.CampaignEntity', on_delete=models.PROTECT, null=False,
                                 related_name='registered_users')

    # IMPORTANT: when user cancels a campaign or a campaign in canceled by admin these 3 fields are filled.
    is_canceled = models.BooleanField(default=0)
    canceled_by = models.IntegerField(choices=UserType.choices(), default=None)
    cancel_time = models.DateTimeField(blank=True, null=True)

    objects = BaseEntityManager(alive_only=True)
    objects_including_deleted = BaseEntityManager(alive_only=False)

    creation_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False, editable=False)
    deletion_time = models.DateTimeField(blank=True, null=True,
                                         default=None, editable=False)

    class Meta:
        db_table = "registered_users"
