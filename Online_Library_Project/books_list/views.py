from django.shortcuts import render

from .models import Book


def book_list(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "books_list/book_list.html", context)

from drf_spectacular.views import SpectacularAPIView
class APISchemaView(SpectacularAPIView):
    pass