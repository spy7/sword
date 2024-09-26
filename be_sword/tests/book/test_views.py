from django.conf import settings
import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import override_settings
from book.models import Book


@pytest.mark.django_db
class TestBookView:

    def test_get_books(self, client: APIClient, book: Book):
        response = client.get(reverse("books"))

        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1
        assert response.data["results"][0]["title"] == "Book one"
        assert response.data["results"][0]["authors"] == "Author one"
        assert response.data["results"][0]["isbn13"] == "1234567890123"
        assert response.data["results"][0]["language_code"] == "eng"

    def test_get_two_books(self, client: APIClient, books: list[Book]):
        response = client.get(reverse("books"))

        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 2

    def test_get_books_filter_by_unique_title(
        self, client: APIClient, books: list[Book]
    ):
        response = client.get(reverse("books"), {"title": "Book one"})

        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1

    def test_get_books_filter_by_lower_title(
        self, client: APIClient, books: list[Book]
    ):
        response = client.get(reverse("books"), {"title": "book one"})

        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1

    def test_get_books_filter_by_both_title(self, client: APIClient, books: list[Book]):
        response = client.get(reverse("books"), {"title": "Book"})

        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 2

    @override_settings(REST_FRAMEWORK=settings.REST_FRAMEWORK | {"PAGE_SIZE": 5})
    def test_get_paginated_books(self, client: APIClient, many_books: list[Book]):
        response = client.get(reverse("books"))

        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 10
        assert len(response.data["results"]) == 5

    def test_get_paginated_books_with_limit(self, client: APIClient, many_books: list[Book]):
        response = client.get(reverse("books"), {"limit": 5})

        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 10
        assert len(response.data["results"]) == 5

    def test_get_paginated_books_with_offset(self, client: APIClient, many_books: list[Book]):
        response = client.get(reverse("books"), {"offset": 9})

        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 10
        assert len(response.data["results"]) == 1
