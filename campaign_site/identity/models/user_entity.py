from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phone_field import PhoneField

from commons.models.base_entity import BaseEntity


class UserEntity(AbstractUser, BaseEntity):
    username = None
    email = models.EmailField(_('email address'), blank=False, unique=True)
    mobile_phone_number = PhoneField(blank=True, help_text='Contact phone number')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []