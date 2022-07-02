from django.urls import path

from app.views import CreateBook, ListBooks

urlpatterns = [
    path('create_book/', CreateBook.as_view(), name='create_book'),
    path('list_books', ListBooks.as_view(), name='list_books'),
]
