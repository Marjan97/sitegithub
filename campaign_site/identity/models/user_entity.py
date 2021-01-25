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
    is_staff = True
    date_joined = None
    password = models.CharField(_('password'), null=True, blank=True, max_length=128)
    mobile_phone_number = models.CharField(max_length=12, blank=True, help_text='شماره تلفن را با 0 وارد کنید', null=True,verbose_name='شماره تلفن همراه')
    # todo change name of otp
    otp = models.PositiveIntegerField(blank=True, null=True,verbose_name='کد یکبار مصرف')
    otp_create_time = models.DateTimeField(auto_now=True)
    user_type = models.IntegerField(choices=UserType.choices(),blank=True, default=UserType.simple.value,verbose_name='نوع کاربری دانشجو')
    student_code = models.CharField(max_length=10,blank=True, unique=True, null=False,verbose_name='شماره دانشجویی')  # todo change name of student_code
    national_code = models.CharField(max_length=10,blank=True, null=True,verbose_name='شماره ملی')
    account_number = models.CharField(max_length=16, null=True,blank=True,verbose_name='شماره حساب')
    field_of_study = models.CharField(max_length=20, blank=True,verbose_name='رشته تحصیلی')
    gender = models.IntegerField(choices=GenderType.choices(), blank=True,null=True,verbose_name='جنسیت')
    year_of_entry = models.IntegerField(null=True,blank=True,verbose_name='سال ورودی دانشجو')
    is_guest = models.BooleanField(default=False,verbose_name='مهمان')

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

    class Meta:
        db_table = "user_entity"


        verbose_name_plural = "دانشجو"
