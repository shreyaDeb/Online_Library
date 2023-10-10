from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            # Use authenticate to check the user's credentials
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect("employee_dashboard")
                else:
                    return redirect("user_dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "login_app/login.html", {"form": form})

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')