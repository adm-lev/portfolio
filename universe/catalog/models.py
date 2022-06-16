from django.db import models
from django.urls import reverse


class Genre(models.Model):
    """
    Genre
    """

    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self):
        """

        :return:
        """
        return self.name


class Book(models.Model):
    """
    Book
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=2000, help_text='Enter a brief')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 chars')
    genre = models.ManyToManyField('Genre', help_text='Select genre')

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
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_to_death = models.DateField('Died', null=True, blank=True)

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










