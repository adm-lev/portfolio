from django.shortcuts import render
# from .models import Book, Author, Genre
from django.views import generic


def index(request):
    """

    :param request:
    :return:
    """

    return render(
        request,
        'tutorial_english/index.html',

    )