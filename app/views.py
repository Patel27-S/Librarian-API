from django.shortcuts import render
from app.models import Author, Book
from app.serializers import AuthorSerializer, BookSerializer

# Create your views here.
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.exceptions import ValidationError


# The librarian should be able to create a new book in the libary's record.
# If the author is new then he should be able to add that author's info in the database as well.
# For a new book, he definitely has to add entries in the database.

class CreateBook(CreateAPIView):
    model = Book
    serializer_class = BookSerializer

    # Overriding the create() method so that the same book is not
    # entered twice by the Librarian in the database and also
    # so that he doesn't have to manually check it, even through
    # the filtering options.
    def create(self, request, *args, **kwargs):

        book_name = request.data.get('book_name')
        instance = Book.objects.filter(book_name= book_name)
        if instance:
            raise ValidationError({'book':'The same book has been already added. Please check.'})
        else:
            return super().create(request, *args, **kwargs)
        


class ListBooks(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['book_name', 'category', 'popularity', 'cover_type', 'number_of_pages']
    search_fields = ['description']
    ordering_fields = ['book_name']

    def get_queryset(self):
        return Book.objects.all()


class DestroyBook(DestroyAPIView):
    queryset = Book.objects.all()
    lookup_field = 'book_name'
    serializer_class = BookSerializer



# class CreateAuthor(CreateAPIView):
#     model = Author
#     serializer_class = AuthorSerializer

#     # Overriding the create() method so that the same book is not
#     # entered twice by the Librarian in the database and also
#     # so that he doesn't have to manually check it, even through
#     # the filtering options.
#     def create(self, request, *args, **kwargs):

#         first_name = request.data.get('first_name')
#         last_name = request.data.get('last_name')
#         email = request.data.get('email')
#         instance = Author.objects.filter(first_name= first_name, last_name= last_name, email = email)
#         if instance:
#             raise ValidationError({'author':'The same author has been already added. Please check.'})
#         else:
#             return super().create(request, *args, **kwargs)

