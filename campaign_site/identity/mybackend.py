from django.contrib.auth.backends import ModelBackend
from .models import user_entity


class MobileBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        mobile = kwargs['mobile']
        try:
            user = user_entity.objects.get(mobile=mobile)
        except MyUser.DoesNotExist:
            pass
