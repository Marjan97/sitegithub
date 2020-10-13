from django.contrib.auth.base_user import BaseUserManager

from commons.manager.base_entity_manager import BaseEntityManager


class MyUserManager(BaseUserManager, BaseEntityManager):
    def create_user(self, mobile_phone_number, password=None, **other_fields):
        if not mobile_phone_number:
            raise ValueError("mobile is required...!")
        user = self.model(mobile_phone_number=mobile_phone_number, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, mobile_phone_number, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser muse have is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser muse have is_superuser=True')
        return self.create_user(mobile_phone_number, password, **other_fields)
