from django.urls import path

from app.views import CreateAuthor, CreateBook, DestroyAuthor, DestroyBook, ListAuthors, ListBooks, RetreiveAuthor, RetreiveBook, RetrieveUpdateDestroyAuthor, RetrieveUpdateDestroyBook, UpdateAuthor, UpdateBook

urlpatterns = [
    path('create_book/', CreateBook.as_view(), name='create_book'),
    path('list_books/', ListBooks.as_view(), name='list_books'),
    path('destroy_book/<str:book_name>', DestroyBook.as_view(), name='destroy_book'),
    path('retrieve_book/<str:book_name>', RetreiveBook.as_view(), name='retrieve_book'),
    path('update_book/<str:book_name>', UpdateBook.as_view(), name='update_book'),
    path('rud_book/<str:book_name>', RetrieveUpdateDestroyBook.as_view(), name='update_book'),

    path('create_author/', CreateAuthor.as_view(), name='create_author'),
    path('list_authors/', ListAuthors.as_view(), name='list_authors'),
    path('destroy_author/<int:id>', DestroyAuthor.as_view(), name='destroy_author'),
    path('retrieve_author/<int:id>', RetreiveAuthor.as_view(), name='retrieve_author'),
    path('update_author/<int:id>', UpdateAuthor.as_view(), name='update_author'),
    path('rud_author/<int:id>', RetrieveUpdateDestroyAuthor.as_view(), name='update_author'),
]
