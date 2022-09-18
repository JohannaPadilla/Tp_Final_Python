from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from UserAppFinal.models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password1 = None
    password2 = None

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class AvatarForm(forms.ModelForm):
    imagen = forms.ImageField()

    class Meta:
        model = Avatar
        fields = "__all__"
