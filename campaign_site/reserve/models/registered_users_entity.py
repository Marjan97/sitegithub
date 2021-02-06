from commons.manager.base_entity_manager import BaseEntityManager
from commons.models.base_entity import BaseModel
from django.db import models
from django.utils import timezone
from identity.enums import UserType
import datetime
from django.db import models


class RegisteredUsersEntity(BaseModel):
    user = models.ForeignKey('identity.UserEntity', on_delete=models.PROTECT, null=False,
                             related_name='registered_campaigns', verbose_name='دانشجو')
    campaign = models.ForeignKey('reserve.CampaignEntity', on_delete=models.PROTECT, null=False,
                                 related_name='registered_users', verbose_name='اردو')

    # IMPORTANT: when user cancels a campaign or a campaign in canceled by admin these 3 fields are filled.
    is_canceled = models.BooleanField(default=0, verbose_name='کنسل شده است')
    canceled_by = models.IntegerField(choices=UserType.choices(), default=None, verbose_name='کنسل شده توسط')
    cancel_time = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ کنسلی')

    objects = BaseEntityManager(alive_only=True)
    objects_including_deleted = BaseEntityManager(alive_only=False)

    creation_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False, editable=False)
    deletion_time = models.DateTimeField(blank=True, null=True,
                                         default=None, editable=False)

    class Meta:
        db_table = "registered_users"
        verbose_name_plural = "رزرو اردو"

    def student(self):
        return self.user.first_name + ' ' + self.user.last_name + " - " + self.user.student_code

    # def fn(self):
    #     # fmt='%Y-%m-%d %H:%M:%S'
    #
    #     dates=[self.cancel_time,self.creation_time,self.deletion_time,self.last_update_time]
    #     for d in dates:
    #         cr_date = datetime.datetime(d.creation_time.year, d.creation_time.month, d.creation_time.day)
    #
    # return cr_date.strftime('%m/%d/%Y')
