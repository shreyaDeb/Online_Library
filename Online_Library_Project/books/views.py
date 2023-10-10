# Create your views here.
from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from cart.models import CartItem

from .models import Book
from .serializers import BookSerializer


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    user = request.user
    in_cart = CartItem.objects.filter(user=user, book=book).exists()
    context = {"book": book, "in_cart": in_cart}
    return render(request, "books/book_detail.html", context)


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
