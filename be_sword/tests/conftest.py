from unittest.mock import MagicMock

import pytest

from django.core.files.uploadedfile import SimpleUploadedFile
from model_bakery import baker
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APIClient

from book.models import Book


@pytest.fixture
def csv_content() -> str:
    title = (
        "book_id,goodreads_book_id,best_book_id,work_id,books_count,isbn,isbn13,authors,"
        "original_publication_year,original_title,title,language_code,average_rating,ratings_count,"
        "work_ratings_count,work_text_reviews_count,ratings_1,ratings_2,ratings_3,ratings_4,ratings_5,"
        "image_url,small_image_url"
    )
    valid_book = (
        "1,2767052,2767052,2792775,272,439023483,9.78043902348e+12,Suzanne Collins,2008.0,"
        'The Hunger Games,"The Hunger Games (The Hunger Games, #1)",eng,4.34,4780653,4942365,155254,66715,'
        "127936,560092,1481305,2706317,https://images.gr-assets.com/books/1447303603m/2767052.jpg,"
        "https://images.gr-assets.com/books/1447303603s/2767052.jpg"
    )
    invalid_book = (
        "2,3,3,4640799,491,439554934,9.78043955493e+12,,1997.0,,,eng,4.44,4602479,4800065,75867,75504,"
        "101676,455024,1156318,3011543,https://images.gr-assets.com/books/1474154022m/3.jpg,"
        "https://images.gr-assets.com/books/1474154022s/3.jpg"
    )
    return title + "\n" + valid_book + "\n" + invalid_book


@pytest.fixture
def csv_file(csv_content: str) -> MagicMock:
    csv_file = SimpleUploadedFile(
        "books.csv", csv_content.encode("utf-8"), content_type="text/csv"
    )
    return csv_file


@pytest.fixture
def serializer_error() -> dict:
    return {"isbn13": [ErrorDetail(string="This field is required.", code="required")]}


@pytest.fixture
def client() -> APIClient:
    return APIClient()


@pytest.fixture
def book() -> Book:
    return baker.make(
        Book,
        title="Book one",
        authors="Author one",
        isbn13="1234567890123",
        language_code="eng",
    )


@pytest.fixture
def book2() -> Book:
    return baker.make(
        Book,
        title="Book two",
        authors="Somebody",
        isbn13="5555555555555",
        language_code="pt",
    )


@pytest.fixture
def books(book: Book, book2: Book) -> list[Book]:
    return [book, book2]


@pytest.fixture
def many_books() -> list[Book]:
    return [baker.make(Book) for _ in range(10)]
