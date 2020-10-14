from django.db import models
from django.utils import timezone

from commons.manager.base_entity_manager import BaseEntityManager


class BaseEntity:
    creation_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False, editable=False)
    deletion_time = models.DateTimeField(blank=True, null=True)

    objects = BaseEntityManager()
    objects_including_deleted = BaseEntityManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deletion_time = timezone.now()
        self.save()

    def hard_delete(self, using=None, keep_parents=False):
        super().delete(using, keep_parents)

    def restore(self, restore_parents=False):
        self.is_deleted = False
        self.deletion_time = None
        self.save()


class BaseModel(BaseEntity, models.Model):
    """
    Use this to subclass Project models. (except UserEntity)
    """

    class Meta:
        abstract = True

