from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    # Add more URLs for book-related views as needed
]
