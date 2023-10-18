from django.db.models.query import QuerySet
from django.http import HttpRequest, JsonResponse

from books.models import Book
from books.serializer import serialize_book


def get_books_from_api_view(request: HttpRequest) -> list[JsonResponse] | None:
    books = Book.objects.all()
    view_books =[serialize_book(book) for book in books]
    return JsonResponse(view_books, safe=False)


def get_api_book_detail_view(request: HttpRequest, book_id: int) -> JsonResponse | None:
    book = Book.objects.filter(id=book_id).first()
    if not book:
        return JsonResponse('Нет книги с таким номером', status=404, safe=False)
    return JsonResponse(serialize_book(book), safe=False)
