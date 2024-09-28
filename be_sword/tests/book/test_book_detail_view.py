import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from book.models import Book
from book.models import BookReserve


@pytest.mark.django_db
class TestBookDetailView:

    def test_get_book(self, client: APIClient, book: Book):
        response = client.get(reverse("book-detail", kwargs={"pk": book.pk}))

        assert response.status_code == status.HTTP_200_OK
        assert response.data["title"] == "Book one"
        assert response.data["authors"] == "Author one"
        assert response.data["isbn13"] == "1234567890123"
        assert response.data["language_code"] == "eng"

    def test_get_wrong_book(self, client: APIClient, book: Book):
        response = client.get(reverse("book-detail", kwargs={"pk": book.pk + 1}))
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_get_book_detail_with_reserve(
        self, client: APIClient, book_reserve: BookReserve
    ):
        response = client.get(
            reverse("book-detail", kwargs={"pk": book_reserve.book.pk})
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["title"] == "Book one"
        assert response.data["is_reserved"]

    def test_get_book_detail_without_reserve(self, client: APIClient, book: Book):
        response = client.get(reverse("book-detail", kwargs={"pk": book.pk}))

        assert response.status_code == status.HTTP_200_OK
        assert response.data["title"] == "Book one"
        assert not response.data["is_reserved"]
