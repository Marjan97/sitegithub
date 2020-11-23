from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
# from phone_field import PhoneField
from commons.manager.base_entity_manager import BaseEntityManager
from identity.enums import UserType, GenderType
from commons.models.base_entity import BaseEntity
from identity.manager.user_entity_manager import MyUserManager
from reserve.models import CampaignEntity


class UserEntity(AbstractUser, BaseEntity):
    username = None
    is_staff = None
    date_joined = None
    password = models.CharField(_('password'), null=True, blank=True, max_length=128)
    mobile_phone_number = models.CharField(max_length=12, blank=True, help_text='Contact phone number', unique=True)
    registered_campaigns = models.ManyToManyField(CampaignEntity)
    # todo change name of otp
    otp = models.PositiveIntegerField(blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now=True)
    user_type = models.IntegerField(choices=UserType.choices(), default=UserType.simple.value)
    student_code = models.CharField(max_length=10, unique=True, null=False) # todo change name of student_code
    gender = models.IntegerField(choices=GenderType.choices(), null=True)
    year_of_entry = models.IntegerField(null=True)

    objects = MyUserManager(alive_only=True)
    objects_including_deleted = MyUserManager(alive_only=False)

    creation_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False, editable=False)
    deletion_time = models.DateTimeField(blank=True, null=True,
                                         default=None, editable=False)

    # REQUIRED_FIELDS = [mobile_phone_number]
    USERNAME_FIELD = 'student_code'
    backend = 'identity.mybackend.MobileBackend'
