from django.urls import path

from . import views

urlpatterns = [
    path("add_chapters/", views.add_chapters, name="add_chapters"),
    # Add more URLs for managing book chapters as needed
]
