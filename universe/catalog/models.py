from django.db import models
from django.urls import reverse


class Genre(models.Model):
    """
    Genre
    """

    name = models.CharField(max_length=200, help_text='Выберите жанр книги', unique=True, verbose_name='Жанр')

    def __str__(self):
        """

        :return:
        """
        return self.name


class Book(models.Model):
    """
    Book
    """
    title = models.CharField(max_length=200, unique=True, verbose_name='Название')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, verbose_name='Автор(ы)')
    summary = models.TextField(max_length=2000, help_text='Добавьте описание', verbose_name='Аннотация')
    isbn = models.CharField('ISBN', max_length=20, help_text='20 символов')
    genre = models.ManyToManyField('Genre', help_text='Укажите жанр', verbose_name='Жанр')
    language = models.CharField(max_length=20, help_text='Укажите язык', verbose_name='Язык', null=True, blank=True)

    def __str__(self):
        """

        :return:
        """
        return self.title

    def get_absolute_url(self):
        """

        :return:
        """
        return reverse('book-detail', args=[str(self.id)])


class Author(models.Model):
    """
    Author
    """
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    date_to_death = models.DateField(null=True, blank=True, verbose_name='Дата смерти')
    biography = models.TextField(help_text='Добавьте биографию', verbose_name='Биография', null=True, blank=True)

    def get_absolute_url(self):
        """

        :return:
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """

        :return:
        """
        return f'{self.last_name}, {self.first_name}'










