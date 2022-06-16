from django.contrib import admin
from .models import Author, Genre, Book


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)


# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name')
#
#
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author')

