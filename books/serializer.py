from typing import Any
from books.models import Book


def serialize_book(book: Book) -> dict[str, Any]:
    return {
        'id': book.pk,
        'title': book.title,
        'author_full_name': book.author_full_name,
        'year_of_publishing': book.year_of_publishing,
        'copies_printed': book.copies_printed,
        'short_description': book.short_description
    }   