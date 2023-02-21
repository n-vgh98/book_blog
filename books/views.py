from django.shortcuts import render, get_object_or_404
from .models import *


def list_books(request):
    books = Book.objects.filter(is_publish=True)
    authors = Author.objects.all()
    context = {
        'ketabha': books,
        'authors': authors
    }
    return render(request, 'books/list_books.html', context)


def detail_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book': book
    }
    return render(request, 'books/detail_book.html', context)
