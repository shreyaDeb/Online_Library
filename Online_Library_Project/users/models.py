from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class BookRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
