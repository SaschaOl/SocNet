from django.urls import path
from .views import UserReg, UserActivate, UserLogin, UserLogout


urlpatterns = [
    path("registration/", UserReg.as_view(), name = "registration"),
    path("activation/<int:id>", UserActivate.as_view(), name = "activation"),
    path("login/", UserLogin.as_view(), name = "login"),
    path("logout/", UserLogout.as_view(), name="logout")
]