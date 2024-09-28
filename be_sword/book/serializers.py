from rest_framework import serializers

from .models import Book
from .models import BookReserve


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "book_id",
            "books_count",
            "title",
            "authors",
            "isbn13",
            "language_code",
            "original_publication_year",
            "average_rating",
            "ratings_count",
            "image_url",
        ]


class BookDetailSerializer(BookSerializer):
    is_reserved = serializers.SerializerMethodField()

    class Meta(BookSerializer.Meta):
        model = Book
        fields = BookSerializer.Meta.fields + ["is_reserved"]

    def get_is_reserved(self, obj):
        return BookReserve.objects.filter(book=obj).exists()


class BookUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def to_internal_value(self, data):
        data["isbn"] = str(data.get("isbn", ""))
        data["isbn13"] = str(
            int(float(data.get("isbn13"))) if data.get("isbn13") else ""
        )
        data["original_publication_year"] = int(
            float(data.get("original_publication_year") or 0)
        )
        return super().to_internal_value(data)


class BookResultSerializer(serializers.Serializer):
    number_of_books = serializers.IntegerField()
    invalid_books = serializers.ListField(child=serializers.CharField())


class BookReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReserve
        fields = ["book", "reserve_date", "customer_name", "customer_email"]
        read_only_fields = ["book", "reserve_date"]
