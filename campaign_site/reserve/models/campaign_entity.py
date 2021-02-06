from django.db import models
from rest_framework.fields import JSONField
from .registered_users_entity import RegisteredUsersEntity
from commons.manager.base_entity_manager import BaseEntityManager
from commons.models import BaseEntity
from commons.models.base_entity import BaseModel
from identity.enums import GenderType

import datetime


class CampaignEntity(BaseModel):
    name = models.CharField(max_length=30, blank=False, verbose_name='عنوان اردو')
    description = models.CharField(max_length=100, blank=False, verbose_name='توضیحات')
    # creator = models.ForeignKey('identity.UserEntity', on_delete=models.PROTECT,null=False, related_name='campaigns')
    gender = models.IntegerField(choices=GenderType.choices(), null=True, verbose_name='جنسیت')
    year_of_entry = models.CharField(max_length=50, blank=False, verbose_name='سال ورودی  اردو')
    capacity = models.IntegerField(default=20, verbose_name='ظرفیت')

    image = models.ImageField(upload_to='Images/', default='Images/None/No_img.jpg', verbose_name='بارگذاری پوستر اردو')

    cost = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='هزینه')
    is_verified = models.BooleanField(verbose_name='تایید شده است')
    verification_time = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ تایید اردو')

    is_canceled = models.BooleanField(default=0, verbose_name='کنسل شده است')
    cancel_time = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ کنسلی اردو')
    # canceled_by = models.IntegerField(choices=[(1, 'admin'), (2, 'simple')], default=None)

    execution_time = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ برگزاری اردو')
    Registration_time_1 = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ شروع ثبت نام')
    Registration_time_2 = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پایان ثبت نام')

    objects = BaseEntityManager(alive_only=True)
    objects_including_deleted = BaseEntityManager(alive_only=False)

    creation_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False, editable=False)
    deletion_time = models.DateTimeField(blank=True, null=True,
                                         default=None, editable=False)

    def __str__(self):
        return self.name

    def execution_date(self):
        ex_time = datetime.datetime(self.execution_time.year, self.execution_time.month, self.execution_time.day)

        return ex_time.strftime('%m/%d/%Y')

    def is_registered(self):
        return len(RegisteredUsersEntity.objects.filter(campaign=self.id))

    def rest_capacity(self):
        return self.capacity - self.is_registered()

    class Meta:
        db_table = "campaign_entity"
        verbose_name_plural = "اردوها"
