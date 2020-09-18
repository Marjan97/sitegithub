from django.db import models
from django.utils import timezone


class BaseEntity:
    # todo: Cascading soft deletion/restoration is yet to be implemented
    is_deleted = models.BooleanField(default=False, editable=False)
    deletion_time = models.DateTimeField(blank=True, null=True,
                                         default=None, editable=False)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deletion_time = timezone.now()
        self.save()

    # objects = BaseModelManager(exclude_deleted=True)
    # objects_including_deleted = BaseModelManager(exclude_deleted=False)
    #
    # creation_time = models.DateTimeField(auto_now_add=True)
    # last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
