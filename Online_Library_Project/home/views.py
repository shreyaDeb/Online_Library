from django.shortcuts import render
from drf_spectacular.views import SpectacularAPIView

# Create your views here.
from books_list.models import Book


def home(request):
    top_books = Book.objects.order_by("title")[:10]
    context = {"top_books": top_books}
    return render(request, "home/home.html", context)


class APISchemaView(SpectacularAPIView):
    pass
