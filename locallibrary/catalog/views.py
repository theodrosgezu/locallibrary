from django.db.models import Count, Q
from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Count of books that contain a particular word
    word = 'ted'  # replace with your word
    num_books_word = Book.objects.filter(Q(title__icontains=word) | Q(summary__icontains=word)).count()

    # Count of genres that contain a particular word
    num_genres_word = Genre.objects.filter(name__icontains=word).count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,'num_books_word': num_books_word,
        'num_genres_word': num_genres_word,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)