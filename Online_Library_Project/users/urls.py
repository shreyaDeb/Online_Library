from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.user_signup, name="user_signup"),
    path("user_dashboard/", views.user_dashboard, name="user_dashboard"),
    path("make_book_request/", views.make_book_request, name="make_book_request"),
    # Add more URLs for user-related views as needed
]
