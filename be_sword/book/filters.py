from django.db.models import Q
from django_filters import CharFilter
from django_filters.rest_framework import FilterSet

from book.models import Book


class BookFilter(FilterSet):
    search = CharFilter(method="filter_by_search")
    title = CharFilter(lookup_expr="icontains")
    authors = CharFilter(lookup_expr="icontains")
    isbn13 = CharFilter(lookup_expr="icontains")

    class Meta:
        model = Book
        fields = ["title", "authors", "isbn13", "language_code"]

    def filter_by_search(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value)
            | Q(authors__icontains=value)
            | Q(isbn13__icontains=value)
        )
