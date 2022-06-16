from django.shortcuts import render
from .models import Book, Author, Genre
from django.views import generic


def index(request):
    """

    :param request:
    :return:
    """
    num_books = Book.objects.all().count()
    num_genres = Genre.objects.all().count()
    num_authors = Author.objects.all().count()

    return render(
        request,
        'catalog/index.html',
        context=
        {
            'num_books': num_books, 'num_genres': num_genres, 'num_authors': num_authors
        }
    )


class BookListView(generic.ListView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


class GenreListView(generic.ListView):
    model = Genre


class BookDetailView(generic.DetailView):
    model = Book


class AuthorDetailView(generic.DetailView):
    model = Author


class GenreDetailView(generic.DetailView):
    model = Genre











