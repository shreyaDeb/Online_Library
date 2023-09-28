from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.TextField()
    genres = models.ManyToManyField("Genre")
    star_rating = models.DecimalField(max_digits=3, decimal_places=2)
    cover_image = models.ImageField(upload_to="book_covers/")

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
