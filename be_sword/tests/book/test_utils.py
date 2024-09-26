from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

from book.models import Book
from book.utils import handle_books_uploaded, treat_serializer_errors
from book.utils import send_uploaded_email


@pytest.mark.django_db()
class TestHandleBooksUploaded:
    def test_handle_books_uploaded(self, csv_file: MagicMock):
        success, invalid_books = handle_books_uploaded(csv_file)
        assert success == 1
        assert Book.objects.count() == 1
        assert len(invalid_books) == 1


class TestTreatSerializerErrors:
    def test_treat_serializer_errors(self, serializer_error: dict):
        treated_error = treat_serializer_errors(serializer_error)
        assert treated_error == {"isbn13": ["This Field Is Required."]}


class TestSendUploadedEmail:
    @patch("book.utils.send_mail")
    def test_send_uploaded_email(
        self, send_mail_mock: MagicMock, serializer_error: dict
    ):
        send_uploaded_email(
            3, {"1234567890123": {"isbn13": ["This Field Is Required."]}}
        )
        send_mail_mock.assert_called_once_with(
            "Books uploaded",
            "3 books uploaded successfully\nInvalid books: 1234567890123: {'isbn13': ['This Field Is Required.']}",
            "host_user@example.com",
            ["sysadmin@example.com"],
        )
