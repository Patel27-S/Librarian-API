from django.db import models

# Create your models here.

# Model - 1
class Book(models.Model):
    
    # Model Filed Options
    cover_type_choices = [
        ('soft cover', 'Soft Cover'), 
        ('hard cover', 'Hard Cover')
        ]

    book_category_choices = [
        ('fitness', 'Fitness'), ('spirituality','Spirituality'), ('drama', 'Drama'), 
        ('horror', 'Horror'),('math', 'Math'), ('journal', 'Journal'), ('science', 'Science'), 
        ('travel & sports', 'Travel & Sports'), ('other', 'Other')
        ]

    book_popularity_options = [
        ('new book','A New Book - Hence Can\'t Tell'), ('not so popular', 'Not So Popular'),
        ('popular', 'Popular'), ('highly popular', 'Highly Popular')
        ]

    # Model Fields
    book_name = models.CharField(verbose_name= 'Book Name',max_length=120)
    number_of_pages = models.IntegerField(help_text='Please Enter the number of pages in the book.')
    cover_type = models.CharField(max_length=12,choices=cover_type_choices, help_text='Please Select the cover type of the book.')
    category = models.CharField(max_length=25,choices=book_category_choices, help_text='Please Select the category type of the book.')
    popularity = models.CharField(max_length=30,choices=book_popularity_options, help_text='Please Select the popularity type of the book.')
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} - {self.category}'



# Model - 2
class Author(models.Model):

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



# Model - 3
class Entry(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book.name} - {self.author.first_name} {self.author.last_name}'