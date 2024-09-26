from book.models import Book
from django_filters.rest_framework import FilterSet
from django_filters import CharFilter


class BookFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains')
    content = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ["title", "authors", "isbn13", "language_code"]
