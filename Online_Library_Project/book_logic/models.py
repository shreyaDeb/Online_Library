from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models


class BookRental(models.Model):
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="rentals"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="book_logic_rentals"
    )
    rental_date = models.DateTimeField(default=datetime.now)
    due_date = models.DateTimeField()
    returned = models.BooleanField(default=False)
    extended = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

    def calculate_due_date(self):
        if not self.extended:
            return self.rental_date + timedelta(days=14)
        else:
            return self.rental_date + timedelta(days=21)

    def is_due_soon(self):
        return self.due_date - datetime.now() <= timedelta(days=2)
