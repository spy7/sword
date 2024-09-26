from rest_framework.generics import ListAPIView

from book.filters import BookFilter
from book.models import Book
from book.serializers import BookSerializer


class BookView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filterset_class = BookFilter

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return response
