from django_filters import CharFilter
from django_filters.rest_framework import FilterSet

from book.models import Book


class BookFilter(FilterSet):
    title = CharFilter(lookup_expr="icontains")
    content = CharFilter(lookup_expr="icontains")

    class Meta:
        model = Book
        fields = ["title", "authors", "isbn13", "language_code"]
