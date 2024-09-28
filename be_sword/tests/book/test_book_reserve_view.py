import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from book.models import Book
from book.models import BookReserve


@pytest.mark.django_db
class TestBookReserveView:

    def test_reserve_book(self, client: APIClient, book: Book, reserve_payload: dict):
        response = client.post(
            reverse("book-reserve", kwargs={"pk": book.pk}), data=reserve_payload
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["book"] == book.pk
        assert response.data["customer_name"] == reserve_payload["customer_name"]
        assert response.data["customer_email"] == reserve_payload["customer_email"]
        reserve = BookReserve.objects.get(pk=book.pk)
        assert reserve.book == book
        assert reserve.customer_name == reserve_payload["customer_name"]
        assert reserve.customer_email == reserve_payload["customer_email"]

    def test_reserve_same_book_should_fail(
        self, client: APIClient, book_reserve: BookReserve, reserve_payload: dict
    ):
        response = client.post(
            reverse("book-reserve", kwargs={"pk": book_reserve.book.pk}),
            data=reserve_payload,
        )
        assert response.status_code == status.HTTP_409_CONFLICT

    def test_reserve_book_with_invalid_payload(self, client: APIClient, book: Book):
        response = client.post(
            reverse("book-reserve", kwargs={"pk": book.pk}),
            data={"customer_name": "Some name"},
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {"customer_email": ["This field is required."]}
