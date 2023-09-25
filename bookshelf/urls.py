from django.contrib import admin
from django.urls import path

from books.views import (books_from_api_view, books_view,
                         single_book_from_api_view, single_book_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', books_view),
    path('books/<int:book_id>/', single_book_view),
    path('api/books/', books_from_api_view),
    path('api/books/<int:book_id>/', single_book_from_api_view),

]
