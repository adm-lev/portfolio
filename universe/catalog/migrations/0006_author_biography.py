# Generated by Django 4.0.5 on 2022-06-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_book_language_alter_book_genre_alter_book_isbn_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='biography',
            field=models.TextField(blank=True, help_text='Добавьте биографию', null=True, verbose_name='Биография'),
        ),
    ]
