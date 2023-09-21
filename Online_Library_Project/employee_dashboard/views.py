from django.shortcuts import render
from users.models import BookRequest
from django.contrib.auth.decorators import user_passes_test

def is_admin_employee(user):
    return user.is_staff and user.employee_profile.is_admin

@user_passes_test(is_admin_employee)
def admin_employee_dashboard(request):
    book_requests = BookRequest.objects.all()
    
    context = {'book_requests': book_requests}
    return render(request, 'employee_dashboard/admin_employee_dashboard.html', context)
