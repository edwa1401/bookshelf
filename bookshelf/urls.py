from django.contrib import admin
from django.urls import path

from books.views import (get_books_view,
                         get_book_detail_view)
from books.API_views import get_books_from_api_view, get_api_book_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', get_books_view),
    path('books/<int:book_id>/', get_book_detail_view),
    path('api/books/', get_books_from_api_view),
    path('api/books/<int:book_id>/', get_api_book_detail_view),

]
