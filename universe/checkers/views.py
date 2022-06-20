from django.shortcuts import render
# from .models import Book, Author, Genre
from django.views import generic


def index(request):
    """

    :param request:
    :return:
    """
    # num_books = Book.objects.all().count()
    # num_genres = Genre.objects.all().count()
    # num_authors = Author.objects.all().count()

    return render(
        request,
        'checkers/index.html',
        # context=
        # {
        #     'num_books': num_books, 'num_genres': num_genres, 'num_authors': num_authors
        # }
    )