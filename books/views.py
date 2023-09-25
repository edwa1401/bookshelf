from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import render

from books.models import Book


def get_books() -> QuerySet | None:
    books = Book.objects.all()
    if not books:
        return None
    return books


def books_view(request: HttpRequest) -> HttpResponse | None:
    books = get_books()
    return render(request, 'books.html', context={'books': books})


def get_book_by_id(book_id: int) -> QuerySet | None:
    return Book.objects.filter(id=book_id).first()
    

def single_book_view(request: HttpRequest, book_id: int) -> HttpResponse | None:
    book = get_book_by_id(book_id)
    return render(request, 'book.html', context={'book': book})


def serialize_book(book: QuerySet) -> dict:
    return {
        'id': book.pk,
        'title': book.title,
        'author_full_name': book.author_full_name,
        'year_of_publishing': book.year_of_publishing,
        'copies_printed': book.copies_printed,
        'short_description': book.short_description
    }

def books_from_api_view(request: HttpRequest) -> list[JsonResponse] | None:
    books = get_books()
    if not books:
        return HttpResponseNotFound('Нет книг')
    view_books =[serialize_book(book) for book in books]
    return JsonResponse(view_books, safe=False)


def single_book_from_api_view(request: HttpRequest, book_id: int) -> JsonResponse | None:
    book = get_book_by_id(book_id)
    if not book:
        return HttpResponseNotFound('Нет книги с таким номером')
    return JsonResponse(serialize_book(book))
