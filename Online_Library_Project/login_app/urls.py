from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .views import CustomLogoutView



urlpatterns = [
    path("login/", views.user_login, name="user_login"),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    # Add more URLs for login-related views as needed
]
