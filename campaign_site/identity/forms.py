from django import forms
from .models.user_entity import UserEntity


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserEntity
        fields = ['mobile_phone_number', ]
