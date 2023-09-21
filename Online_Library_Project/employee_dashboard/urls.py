from django.urls import path
from . import views

urlpatterns = [
    path('admin_employee_dashboard/', views.admin_employee_dashboard, name='admin_employee_dashboard'),
    # Add more URLs for employee dashboard-related views as needed
]
