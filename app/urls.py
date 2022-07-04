from django.urls import path

from app.views import CreateAuthor, CreateBook, CreateEntry, DestroyAuthor, DestroyBook, DestroyEntry, ListAuthors, ListBooks, ListEntries, RetreiveAuthor, RetreiveBook, RetreiveEntry, RetrieveUpdateDestroyAuthor, RetrieveUpdateDestroyBook, RetrieveUpdateDestroyEntry, UpdateAuthor, UpdateBook, UpdateEntry

urlpatterns = [

    # Book URLs :-
    path('create_book/', CreateBook.as_view(), name='create_book'),
    path('list_books/', ListBooks.as_view(), name='list_books'),
    path('rud_book/<str:book_name>', RetrieveUpdateDestroyBook.as_view(), name='update_book'),

    # Author URLs :-
    path('create_author/', CreateAuthor.as_view(), name='create_author'),
    path('list_authors/', ListAuthors.as_view(), name='list_authors'),
    path('rud_author/<int:id>', RetrieveUpdateDestroyAuthor.as_view(), name='update_author'),

    # Entry URLs :-
    path('create_entry/', CreateEntry.as_view(), name='create_entry'),
    path('list_entries/', ListEntries.as_view(), name='list_entries'),
    path('rud_entry/<int:id>', RetrieveUpdateDestroyEntry.as_view(), name='update_entry'),

]
