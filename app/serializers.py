from app.models import Author, Book, Entry
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['book_name','category','description','number_of_pages', 'cover_type',  'popularity' ]


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']


class EntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entry
        fields = ['book', 'author']

