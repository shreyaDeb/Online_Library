from django import forms
from .models import BookChapter

class ChapterForm(forms.ModelForm):
    class Meta:
        model = BookChapter
        fields = ['chapter_name', 'chapter_content']
