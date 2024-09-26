import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from book.models import Book


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
