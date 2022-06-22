from django.contrib import admin
from .models import Author, Genre, Book


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)


# class BookInline(admin.StackedInline):
#     model = Book
#     extra = 2
#
#
# class BookAdmin(admin.ModelAdmin):
#
#     fields = ['title', 'author', 'summary', 'isbn', 'genre', 'language', 'picture']
#     inlines = [BookInline]
#     list_filter = ['title']
#
#
# admin.site.register(Book, BookAdmin)

