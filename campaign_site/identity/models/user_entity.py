from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
# from phone_field import PhoneField
from identity.enums import UserType
from identity.manager import MyUserManager
from commons.models.base_entity import BaseEntity


class UserEntity(AbstractUser, BaseEntity):

    username = None
    email = models.EmailField(_('email address'), blank=False, unique=True)
    mobile_phone_number = models.CharField(max_length=11, blank=True, help_text='Contact phone number', unique=True)
    otp = models.PositiveIntegerField(blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now=True)
    user_type = models.IntegerField(choices=UserType.choices(), default=UserType.simple.value)

    USERNAME_FIELD = 'mobile_phone_number'
    objects = MyUserManager()
    backend='identity.mybackend.MobileBackend'

    REQUIRED_FIELDS = [mobile_phone_number]
