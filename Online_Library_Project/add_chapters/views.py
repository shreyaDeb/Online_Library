from django.shortcuts import render, redirect
from .forms import ChapterForm  # Import the form
from .models import BookChapter  # Import the Chapter model

def add_chapters(request):
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            # Create and save the chapter
            chapter = form.save()
            return redirect('add_chapters')  # Redirect to the same page after successful submission
    else:
        form = ChapterForm()
    
    context = {'form': form}
    return render(request, 'add_chapters/add_chapters.html', context)
