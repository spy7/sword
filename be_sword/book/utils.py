import csv
import io

from django.conf import settings
from django.core.mail import send_mail

from book.models import Book
from book.serializers import BookUploadSerializer


def handle_books_uploaded(file) -> tuple[int, dict]:
    """
    Read the CSV file and create Book objects
    Return a list of invalid books
    """
    books = []
    invalid_books = {}
    file_data = io.TextIOWrapper(file.file, encoding="utf-8")
    reader = csv.DictReader(file_data)
    for row in reader:
        serializer = BookUploadSerializer(data=row)
        if serializer.is_valid():
            books.append(Book(**serializer.validated_data))
        else:
            invalid_books[row["isbn13"]] = treat_serializer_errors(serializer.errors)
    Book.objects.bulk_create(books, batch_size=1000, ignore_conflicts=True)
    return len(books), invalid_books


def treat_serializer_errors(errors: dict) -> dict:
    """
    Treat serializer errors and return a dictionary with the field name and the error message
    """
    treated_errors = {}
    for field, error_list in errors.items():
        treated_errors[field] = [error.title() for error in error_list]
    return treated_errors


def send_uploaded_email(success: int, invalid_books: str) -> None:
    '''
    Send an email to the system admin with the upload results
    '''
    subject = settings.EMAIL_UPLOAD_SUBJECT
    message = settings.EMAIL_UPLOAD_MESSAGE % success
    fail_message = settings.EMAIL_UPLOAD_FAIL % ', '.join(f"{b[0]}: {b[1]}" for b in invalid_books.items())
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_SYSTEM_ADMIN]

    if invalid_books:
        message += fail_message

    send_mail(subject, message, from_email, recipient_list)
