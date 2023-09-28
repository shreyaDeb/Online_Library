from django.shortcuts import render

from book_logic.models import BookRental


def user_dashboard(request):
    user = request.user
    rented_books = BookRental.objects.filter(user=user, returned=False)
    past_rentals = BookRental.objects.filter(user=user, returned=True)
    return render(
        request,
        "user_dashboard.html",
        {"user": user, "rented_books": rented_books, "past_rentals": past_rentals},
    )
