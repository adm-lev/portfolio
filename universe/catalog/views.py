from django.shortcuts import render
from .models import Book, Author, Genre
from django.views import generic
import os
import textract
import docx


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


def reading(request, pk):
    summary = Book.objects.get(id=pk)
    book_path = summary.unit_file
    docfile = docx.Document(os.path.join('media', str(book_path)))


def special(request, pk):
    summary = Book.objects.get(id=pk)
    book_path = summary.unit_file
    # with open(os.path.join('media', str(book_path)), 'r') as f:
    #     file_content = f.read()
    #     f.close()
    # context = {'file_content': file_content}
    # with textract.process(os.path.join('media', str(book_path))) as text:
    #     text_file = text
    #     text.write()
    text = textract.process(os.path.join('media', str(book_path)))
    text_file = text.decode('utf8')

    return render(request, 'catalog/book_read.html', context={'text': text_file})


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











