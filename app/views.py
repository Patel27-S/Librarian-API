from django.shortcuts import render
from app.models import Book

# Create your views here.
from rest_framework.generics import CreateAPIView


# The librarian should be able to create a new book in the libary's record.
# If the author is new then he should be able to add that author's info in the database as well.
# For a new book, he definitely has to add entries in the database.

class CreateBook(CreateAPIView):
    model = Book
    