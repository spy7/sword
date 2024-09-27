from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookUploadSerializer(BookSerializer):
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
