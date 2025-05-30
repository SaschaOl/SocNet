from django.urls import path
from .views import HomePageView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(HomePageView.as_view()), name = "home")
]