# Generated by Django 4.0.5 on 2022-07-02 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('no_of_pages', models.IntegerField(help_text='Please Enter the number of pages in the book.')),
                ('cover_type', models.CharField(choices=[('soft cover', 'Soft Cover'), ('hard cover', 'Hard Cover')], help_text='Please Select the cover type of the book.', max_length=12)),
                ('category', models.CharField(choices=[('fitness', 'Fitness'), ('spirituality', 'Spirituality'), ('drama', 'Drama'), ('horror', 'Horror'), ('math', 'Math'), ('journal', 'Journal'), ('science', 'Science'), ('travel & sports', 'Travel & Sports')], help_text='Please Select the category type of the book.', max_length=25)),
                ('popularity', models.CharField(choices=[('new book', "A New Book - Hence Can't Tell"), ('not so popular', 'Not So Popular'), ('popular', 'Popular'), ('highly popular', 'Highly Popular')], help_text='Please Select the popularity type of the book.', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.book')),
            ],
        ),
    ]
