from django.shortcuts import render
from app.models import Book
from app.serializers import BookSerializer

# Create your views here.
from rest_framework.generics import CreateAPIView, ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


# The librarian should be able to create a new book in the libary's record.
# If the author is new then he should be able to add that author's info in the database as well.
# For a new book, he definitely has to add entries in the database.

class CreateBook(CreateAPIView):
    model = Book
    serializer_class = BookSerializer


class ListBooks(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['book_name', 'category', 'popularity', 'cover_type', 'number_of_pages']
    search_fields = ['description']
    ordering_fields = ['book_name']

    def get_queryset(self):
        return Book.objects.all()


# class DestroyBook(DestroyAPIView):

