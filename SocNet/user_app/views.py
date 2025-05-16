from django.shortcuts import render
from django_registration.views import RegistrationForm
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from .models import SocNetUser
from django.core.mail import send_mail
import random
import string
from .form import CodeForm
from django.http import HttpResponseRedirect

# Create your views here.

class UserReg(FormView):
    form_class = RegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("activation")

    def form_valid(self, form: RegistrationForm):
        confirmation_code = ''.join(random.choices(string.ascii_letters + string.digits, k = 6))
        new_user = SocNetUser.objects.create_user(
            email = form.cleaned_data["email"],
            password = form.cleaned_data["password1"],
            confirmation_code = confirmation_code,
            is_active = False
        )
        send_mail(
            subject = "Код підтвердження реєстрації",
            message = f"{confirmation_code}",
            from_email = "zx00xsanyazx@gmail.com",
            recipient_list = [f'{form.cleaned_data["email"]}'],
            fail_silently = False
        )
        print(new_user.pk)
        return HttpResponseRedirect(reverse_lazy("activation", kwargs = {"id": new_user.pk}))


class UserActivate(FormView):
    form_class = CodeForm
    template_name = "activation.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form: CodeForm):
        code = form.cleaned_data["code"]
        user = SocNetUser.objects.get(id = self.kwargs['id']) 
        if user.confirmation_code == code:
            user.confirmation_code = None
            user.is_active = True
            user.save()

        return super().form_valid(form)
    
class UserLogin(LoginView):
    template_name = 'login.html'

class UserLogout(LogoutView):
    next_page = 'home'
