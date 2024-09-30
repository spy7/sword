from django.contrib.postgres.indexes import GinIndex
from django.db import models


class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    goodreads_book_id = models.IntegerField()
    best_book_id = models.IntegerField()
    work_id = models.IntegerField()
    books_count = models.IntegerField()
    isbn = models.CharField(max_length=15, blank=True)
    isbn13 = models.CharField(max_length=15, blank=True)
    authors = models.TextField(blank=True)
    original_publication_year = models.IntegerField()
    original_title = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    language_code = models.CharField(max_length=10, blank=True)
    average_rating = models.FloatField()
    ratings_count = models.IntegerField()
    work_ratings_count = models.IntegerField()
    work_text_reviews_count = models.IntegerField()
    ratings_1 = models.IntegerField()
    ratings_2 = models.IntegerField()
    ratings_3 = models.IntegerField()
    ratings_4 = models.IntegerField()
    ratings_5 = models.IntegerField()
    image_url = models.URLField()
    small_image_url = models.URLField()

    class Meta:
        indexes = [
            GinIndex(
                fields=["title"],
                name="gin_title_idx",
                opclasses=["gin_trgm_ops"],
            ),
            GinIndex(
                fields=["authors"],
                name="gin_authors_idx",
                opclasses=["gin_trgm_ops"],
            ),
            GinIndex(
                fields=["isbn13"],
                name="gin_isbn13_idx",
                opclasses=["gin_trgm_ops"],
            ),
            models.Index(fields=["language_code"], name="language_code_idx"),
        ]

    def __str__(self):
        return self.title


class BookReserve(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    reserve_date = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()

    def __str__(self):
        return self.book.title
