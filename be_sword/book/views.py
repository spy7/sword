from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

from book.filters import BookFilter
from book.models import Book
from book.serializers import BookSerializer


class BookView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filterset_class = BookFilter


class BookDetailView(RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
