from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('books_list.Book', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
