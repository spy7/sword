from unittest.mock import MagicMock

import pytest

from book.models import Book
from book.utils import handle_books_uploaded


@pytest.mark.django_db()
class TestHandleBooksUploaded:
    def test_handle_books_uploaded(self, csv_file: MagicMock):
        invalid_books = handle_books_uploaded(csv_file)
        assert Book.objects.count() == 1
        assert len(invalid_books) == 1
