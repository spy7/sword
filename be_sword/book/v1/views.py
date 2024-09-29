import logging

from django.db import IntegrityError
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from book.models import Book
from book.models import BookReserve
from book.v1.filters import BookFilter
from book.v1.serializers import BookDetailSerializer
from book.v1.serializers import BookReserveSerializer
from book.v1.serializers import BookSerializer

logger = logging.getLogger(__name__)


class BookView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filterset_class = BookFilter


class BookDetailView(RetrieveAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()


class BookReserveView(CreateAPIView):
    serializer_class = BookReserveSerializer
    queryset = BookReserve.objects.all()

    def create(self, request, *args, **kwargs):
        book = Book.objects.get(pk=self.kwargs["pk"])
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            try:
                book_reserve = BookReserve.objects.create(
                    book=book, **serializer.validated_data
                )
                logging.info("Book reserved successfully.")
                return Response(
                    BookReserveSerializer(book_reserve).data,
                    status=status.HTTP_201_CREATED,
                )
            except IntegrityError:
                logging.warning("This book is already reserved.")
                return Response(
                    {"detail": "This book is already reserved."},
                    status=status.HTTP_409_CONFLICT,
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
