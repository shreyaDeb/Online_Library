from django.shortcuts import render

# Create your views here.
from books_list.models import Book
from drf_spectacular.views import SpectacularAPIView


def home(request):
    top_books = Book.objects.order_by("title")[:10]
    context = {"top_books": top_books}
    return render(request, "home/home.html", context)

class APISchemaView(SpectacularAPIView):
    pass