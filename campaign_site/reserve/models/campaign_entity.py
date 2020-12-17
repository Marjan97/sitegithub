from django.db import models
from rest_framework.fields import JSONField

from commons.manager.base_entity_manager import BaseEntityManager
from commons.models import BaseEntity
from commons.models.base_entity import BaseModel
from identity.enums import GenderType


class CampaignEntity(BaseModel):
    name = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=100, blank=False)
    # creator = models.ForeignKey('identity.UserEntity', on_delete=models.PROTECT,null=False, related_name='campaigns')
    gender = models.IntegerField(choices=GenderType.choices(), null=True)
    year_of_entry = models.CharField(max_length=50, blank=False)
    capacity = models.IntegerField(default=20)

    image = models.ImageField(upload_to='Images/', default='Images/None/No_img.jpg')

    cost = models.DecimalField(max_digits=6, decimal_places=2)
    is_verified = models.BooleanField()
    verification_time = models.DateTimeField(blank=True, null=True)

    is_canceled = models.BooleanField(default=0)
    cancel_time = models.DateTimeField(blank=True, null=True)

    execution_time = models.DateTimeField(blank=True, null=True)
    Registration_time_1 = models.DateTimeField(blank=True, null=True)
    Registration_time_2 = models.DateTimeField(blank=True, null=True)

    objects = BaseEntityManager(alive_only=True)
    objects_including_deleted = BaseEntityManager(alive_only=False)

    creation_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False, editable=False)
    deletion_time = models.DateTimeField(blank=True, null=True,
                                         default=None, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "campaign_entity"
