from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
# from phone_field import PhoneField
from identity.manager import MyUserManager
from commons.models.base_entity import BaseEntity


class UserEntity(AbstractUser, BaseEntity):
    username = None
    email = models.EmailField(_('email address'), blank=False, unique=True)
    mobile = models.CharField(max_length=11,blank=True, help_text='Contact phone number',unique=True)
    otp = models.PositiveIntegerField(blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'mobile'
    objects = MyUserManager()

    REQUIRED_FIELDS = []