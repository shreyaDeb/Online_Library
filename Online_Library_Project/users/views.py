from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import BookRequestForm

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def user_dashboard(request):
    user = request.user
    # Implement user dashboard logic here
    return render(request, 'users/user_dashboard.html', {'user': user})

def make_book_request(request):
    if request.method == 'POST':
        form = BookRequestForm(request.POST)
        if form.is_valid():
            # Save the book request
            form.save()
            return redirect('user_dashboard')
    else:
        form = BookRequestForm()
    return render(request, 'users/make_book_request.html', {'form': form})
