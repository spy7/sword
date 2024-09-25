from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

from book.models import Book
from book.utils import handle_books_uploaded
from book.utils import send_uploaded_email


@pytest.mark.django_db()
class TestHandleBooksUploaded:
    def test_handle_books_uploaded(self, csv_file: MagicMock):
        invalid_books = handle_books_uploaded(csv_file)
        assert Book.objects.count() == 1
        assert len(invalid_books) == 1


class TestSendUploadedEmail:
    @patch("book.utils.send_mail")
    def test_send_uploaded_email(self, send_mail_mock):
        send_uploaded_email(["1234567890123"])
        send_mail_mock.assert_called_once_with(
            "Books uploaded",
            "Books uploaded successfully\nInvalid books: 1234567890123",
            "host_user@example.com",
            ["sysadmin@example.com"],
        )
