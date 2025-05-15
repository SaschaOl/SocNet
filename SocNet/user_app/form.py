from django_registration.views import RegistrationForm
from .models import SocNetUser
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class SocNetRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = SocNetUser

class CodeForm(forms.Form):
    code = forms.CharField(max_length = 6, label = "Введіть код підтвердження", required = True)


    