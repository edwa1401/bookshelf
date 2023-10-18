from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from books.models import Book


def get_books_view(request: HttpRequest) -> HttpResponse | None:
    books = Book.objects.all()
    return render(request, 'all_books.html', context={'books': books})


def get_book_detail_view(request: HttpRequest, book_id: int) -> HttpResponse | None:
    book = Book.objects.filter(id=book_id).first()
    return render(request, 'book_detail.html', context={'book': book})
