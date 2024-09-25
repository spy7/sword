import csv
import io

from django.conf import settings
from django.core.mail import send_mail

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
            invalid_books.append(row["isbn13"])
    Book.objects.bulk_create(books, batch_size=1000, ignore_conflicts=True)
    return invalid_books


def send_uploaded_email(invalid_books: str):
    subject = settings.EMAIL_UPLOAD_SUBJECT
    message = settings.EMAIL_UPLOAD_MESSAGE
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_SYSTEM_ADMIN]

    if invalid_books:
        message += f"\nInvalid books: {', '.join(invalid_books)}"

    send_mail(subject, message, from_email, recipient_list)
