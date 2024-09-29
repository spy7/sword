from rest_framework import serializers

from book.models import Book


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
