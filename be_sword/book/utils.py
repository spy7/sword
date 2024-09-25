import csv
import io

from book.models import Book
from book.serializers import BookUploadSerializer


def handle_books_uploaded(file):
    """
    Read the CSV file and create Book objects
    Return a list of invalid books
    """
    books = []
    invalid_books = []
    file_data = io.TextIOWrapper(file.file, encoding="utf-8")
    reader = csv.DictReader(file_data)
    for row in reader:
        serializer = BookUploadSerializer(data=row)
        if serializer.is_valid():
            books.append(Book(**serializer.validated_data))
        else:
            invalid_books.append(row)
    Book.objects.bulk_create(books, batch_size=1000, ignore_conflicts=True)
    return invalid_books
