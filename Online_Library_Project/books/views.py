from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Book
from cart.models import CartItem

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    user = request.user
    in_cart = CartItem.objects.filter(user=user, book=book).exists()
    
    context = {'book': book, 'in_cart': in_cart}
    return render(request, 'books/book_detail.html', context)
