from dataclasses import fields
from email.mime import image
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from UserAppFinal.models import *

class AvatarForm(forms.ModelForm):
    """Avatar form"""
    imagen = forms.ImageField()
    class Meta:
        model = Avatar
        fields = ['imagen',]
        
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
        fields = ('username', 'email', 'first_name', 'last_name');

class MensajesForm(forms.ModelForm):

    class Meta:
        model = Mensajes  # Modelo del cual importa
        fields = [
            'recibe',
            'mensaje',
        ]
        #  Widget para agrandar el area de texto(TextField) a 80 columnas
        widgets = {'mensaje': forms.Textarea(attrs={'cols': 80})}


