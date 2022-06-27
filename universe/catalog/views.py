from django.shortcuts import render
from .models import Book, Author, Genre
from django.views import generic
import os
import textract
import docx
import fitz
from django.contrib.auth.decorators import login_required


@login_required
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


@login_required
def reading(request, pk):
    summary = Book.objects.get(id=pk)
    book_path = summary.unit_file
    extention = str(book_path).split('.')
    if extention[1] == 'docx':
        docfile = docx.Document(os.path.join('media', str(book_path)))
        return render(request, 'catalog/book_read.html', context={'docfile': docfile, 'extention': extention[1]})

    elif extention[1] == 'pdf':
        pdf_file = fitz.open(os.path.join('media', str(book_path)))
        return render(request, 'catalog/book_read.html', context={'docfile': pdf_file, 'extention': extention[1]})


@login_required
def reading_pdf(request, pk):
    summary = Book.objects.get(id=pk)
    book_path = summary.unit_file

    pdf_file = fitz.open(os.path.join('media', str(book_path)))


@login_required
def special(request, pk):
    summary = Book.objects.get(id=pk)
    book_path = summary.unit_file

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











