from django.db import models

from commons.manager.base_entity_manager import BaseEntityManager
from commons.models.base_entity import BaseModel


class RegisteredUsers(BaseModel):
    user = models.ForeignKey('identity.UserEntity', on_delete=models.PROTECT,
                             null=False, related_name='registered_campaigns')
    campaign = models.ForeignKey('reserve.CampaignEntity', on_delete=models.PROTECT,
                                 null=False, related_name='registered_users')

    objects = BaseEntityManager(alive_only=True)
    objects_including_deleted = BaseEntityManager(alive_only=False)

    creation_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False, editable=False)
    deletion_time = models.DateTimeField(blank=True, null=True,
                                         default=None, editable=False)
