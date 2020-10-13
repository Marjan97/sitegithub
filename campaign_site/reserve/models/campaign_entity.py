from django.db import models

from commons.manager.base_entity_manager import BaseEntityManager
from commons.models import BaseEntity
from commons.models.base_entity import BaseModel
from identity.enums import GenderType


class CampaignEntity(BaseModel):
    name = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=100, blank=False)
    creator = models.ForeignKey('identity.UserEntity', on_delete=models.PROTECT,
                                null=False, related_name='campaigns')
    gender = models.IntegerField(choices=GenderType.choices(), null=True)
    year_of_entry = models.IntegerField(null=True)
    capacity = models.IntegerField()

    cost = models.DecimalField(max_digits=6, decimal_places=2)
    is_verified = models.BooleanField()
    verification_time = models.DateTimeField(blank=True, null=True)

    objects = BaseEntityManager(alive_only=True)
    objects_including_deleted = BaseEntityManager(alive_only=False)

    creation_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False, editable=False)
    deletion_time = models.DateTimeField(blank=True, null=True,
                                         default=None, editable=False)
