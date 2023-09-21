from django.db import models

class BookChapter(models.Model):
    book = models.ForeignKey('books_list.Book', on_delete=models.CASCADE)  # Assuming a ForeignKey relationship to the Book model
    chapter_name = models.CharField(max_length=100)
    chapter_content = models.TextField()
    
    def __str__(self):
        return self.chapter_name
