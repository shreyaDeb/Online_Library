from django.urls import path
from . import views

urlpatterns = [
    path('rent/<int:book_id>/', views.rent_book, name='rent_book'),
    path('extend/<int:rental_id>/', views.extend_rental, name='extend_rental'),
    # Add URLs for due date notifications and automatic returns if needed
]
