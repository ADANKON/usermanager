from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'password1', 'password2')

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Nom d’utilisateur')
    password = forms.CharField(widget=forms.PasswordInput)