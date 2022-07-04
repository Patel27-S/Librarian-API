from django.shortcuts import render
from app.models import Author, Book, Entry
from app.serializers import AuthorSerializer, BookSerializer, EntrySerializer

# Create your views here.
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, \
                                    UpdateAPIView,RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status


# Books Views :-
class CreateBook(CreateAPIView):
    model = Book
    serializer_class = BookSerializer

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


class RetrieveUpdateDestroyBook(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    lookup_field = 'book_name'
    serializer_class = BookSerializer


# Author Views :-
class CreateAuthor(CreateAPIView):
    model = Author
    serializer_class = AuthorSerializer

    def post(self, request, *args, **kwargs):

        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        try:
            instance = Author.objects.get(email=email)
        except:
            author = Author(first_name=first_name, last_name=last_name, email=email)
            author.save()
            return Response(
                            data={
                                'Author':'Author is succesfully created.'
                                }, 
                            status=status.HTTP_200_OK,
                            )
        if instance:
            return Response(
                            data={
                                'Error':'The author is already existing. If it is a different author \
                                         then enter another email for the author as the mentioned is already\
                                         taken. '
                                         }, 
                            status=status.HTTP_400_BAD_REQUEST,
                            )
        
        

class ListAuthors(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'email']

    def get_queryset(self):
        return Author.objects.all()


class RetrieveUpdateDestroyAuthor(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    lookup_field = 'id'
    serializer_class = AuthorSerializer


# Entry Views :-
class CreateEntry(CreateAPIView):
    model = Entry
    serializer_class = EntrySerializer

    def post(self, request, *args, **kwargs):

        book = request.data.get('book')
        author = request.data.get('author')
    
        try:
            instance = Entry.objects.get(book=book, author=author)

        except:
            book_instance = Book.objects.get(id=book)
            author_instance = Author.objects.get(id=author)
            entry = Entry(book=book_instance, author=author_instance)
            entry.save()
            return Response(
                            data={
                                f'{book_instance.book_name} is authored by':\
                                f'{author_instance.first_name} {author_instance.last_name}'
                                }, 
                            status=status.HTTP_200_OK,
                            )
        if instance:
            return Response(
                            data={
                                'Error':'The entry is already existing.'
                                }, 
                            status=status.HTTP_400_BAD_REQUEST,
                            )
  
class ListEntries(ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['book', 'author']

    def get_queryset(self):
        return Entry.objects.all()


class RetrieveUpdateDestroyEntry(RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    lookup_field = 'id'
    serializer_class = EntrySerializer