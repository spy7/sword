from book.models import Book
from django.contrib import admin


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "authors", "isbn13"]
    search_fields = ["title", "authors", "isbn13"]
