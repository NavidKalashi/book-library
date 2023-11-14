from django.shortcuts import render
from .models import Book

def books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book/books.html', context)

def book(request, pk):
    book = Book.objects.get(id=pk)
    context = {'book': book}
    return render(request, 'book/single_book.html', context)