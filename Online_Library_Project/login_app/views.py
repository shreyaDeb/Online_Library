from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_staff:
                return redirect('employee_dashboard')
            else:
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login_app/login.html', {'form': form})
