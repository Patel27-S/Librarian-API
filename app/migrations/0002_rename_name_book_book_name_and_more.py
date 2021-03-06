# Generated by Django 4.0.5 on 2022-07-02 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='book_name',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='no_of_pages',
            new_name='number_of_pages',
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('fitness', 'Fitness'), ('spirituality', 'Spirituality'), ('drama', 'Drama'), ('horror', 'Horror'), ('math', 'Math'), ('journal', 'Journal'), ('science', 'Science'), ('travel & sports', 'Travel & Sports'), ('other', 'Other')], help_text='Please Select the category type of the book.', max_length=25),
        ),
    ]
