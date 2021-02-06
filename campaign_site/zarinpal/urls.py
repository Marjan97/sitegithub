from django.conf.urls import url
from rest_framework import routers

from .views import RequestZarinpal, VerifyZarinpal

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^request/$', RequestZarinpal.as_view(), name='request_zarinpal'),
    url(r'^verify/$', VerifyZarinpal.as_view(), name='verify_zarinpal'),
]
urlpatterns += router.urls
