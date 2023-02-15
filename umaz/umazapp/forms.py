from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
