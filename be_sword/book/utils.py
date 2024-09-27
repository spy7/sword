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
    file_data = io.TextIOWrapper(file.file, encoding="utf-8")
    reader = csv.DictReader(file_data)
    books = [row for row in reader]
    serializer = BookUploadSerializer(data=books, many=True)
    serializer.is_valid()
    invalid_books = {}
    valid_books = serializer.validated_data
    if not valid_books:
        for index, error in enumerate(serializer.errors):
            if error:
                invalid_books[books[index]["book_id"]] = treat_serializer_errors(error)
            else:
                valid_books.append(books[index])
    book_list = [Book(**book) for book in valid_books]
    Book.objects.bulk_create(book_list, batch_size=1000, ignore_conflicts=True)
    return len(book_list), invalid_books


def treat_serializer_errors(errors: dict) -> dict:
    """
    Treat serializer errors and return a dictionary with the field name and the error message
    """
    treated_errors = {}
    for field, error_list in errors.items():
        treated_errors[field] = [error.title() for error in error_list]
    return treated_errors


def send_uploaded_email(success: int, invalid_books: dict[str, dict]) -> None:
    """
    Send an email to the system admin with the upload results
    """
    subject = settings.EMAIL_UPLOAD_SUBJECT
    message = settings.EMAIL_UPLOAD_MESSAGE % success
    fail_message = (
        settings.EMAIL_UPLOAD_FAIL
        + "\n"
        + ",\n".join(f"{b[0]}: {b[1]}" for b in invalid_books.items())
    )
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_SYSTEM_ADMIN]

    if invalid_books:
        message += "\n" + fail_message

    send_mail(subject, message, from_email, recipient_list)
