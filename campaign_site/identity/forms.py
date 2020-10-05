from django import forms
from django.forms import ModelForm
from .models.user_entity import UserEntity


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserEntity
        fields = ['mobile_phone_number', ]
