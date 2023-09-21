from django.shortcuts import render, redirect, get_object_or_404
from .models import BookRental
from books_list.models import Book
from django.contrib import messages

def rent_book(request, book_id):
    user = request.user
    book = get_object_or_404(Book, pk=book_id)
    
    # Check if the book is already rented
    if BookRental.objects.filter(book=book, user=user, returned=False).exists():
        messages.error(request, "This book is already rented by you.")
    else:
        rental = BookRental(book=book, user=user, due_date=datetime.now() + timedelta(days=14))
        rental.save()
        messages.success(request, "You have successfully rented the book.")
    
    return redirect('book_detail', book_id=book_id)

from datetime import datetime, timedelta

def extend_rental(request, rental_id):
    user = request.user
    rental = get_object_or_404(BookRental, pk=rental_id, user=user, returned=False)
    
    # Check if the book can be extended
    if rental.extended:
        messages.error(request, "You have already extended this rental once.")
    else:
        rental.extended = True
        rental.due_date = rental.calculate_due_date()
        rental.save()
        messages.success(request, "Rental extended for 7 days.")
    
    return redirect('dashboard')  # Redirect to the user's dashboard
