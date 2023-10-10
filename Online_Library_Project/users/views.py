from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import BookRequestForm


def user_signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Use authenticate to log in the user
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password)
            login(request, user)

            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "users/signup.html", {"form": form})


def user_dashboard(request):
    user = request.user
    # Implement user dashboard logic here
    return render(request, "user_dashboard.html", {"user": user})


def make_book_request(request):
    if request.method == "POST":
        form = BookRequestForm(request.POST)
        if form.is_valid():
            # Save the book request
            form.save()
            return redirect("user_dashboard")
    else:
        form = BookRequestForm()
    return render(request, "users/make_book_request.html", {"form": form})
