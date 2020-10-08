from rest_framework import serializers
from identity.models import UserEntity



class mobileloginserializer(serializers.ModelSerializer):
    class Meta:
        model=UserEntity
        fields = ['mobile_phone_number','otp']