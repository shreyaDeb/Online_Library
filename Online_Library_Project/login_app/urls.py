from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.user_login, name="user_login"),
    # Add more URLs for login-related views as needed
]
