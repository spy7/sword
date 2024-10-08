# Generated by Django 5.1.1 on 2024-09-25 19:33

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("book_id", models.IntegerField()),
                ("goodreads_book_id", models.IntegerField()),
                ("best_book_id", models.IntegerField()),
                ("work_id", models.IntegerField()),
                ("books_count", models.IntegerField()),
                ("isbn", models.CharField(max_length=15)),
                ("isbn13", models.CharField(max_length=15)),
                ("authors", models.CharField(max_length=255)),
                ("original_publication_year", models.IntegerField()),
                ("original_title", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                ("language_code", models.CharField(max_length=10)),
                ("average_rating", models.FloatField()),
                ("ratings_count", models.IntegerField()),
                ("work_ratings_count", models.IntegerField()),
                ("work_text_reviews_count", models.IntegerField()),
                ("ratings_1", models.IntegerField()),
                ("ratings_2", models.IntegerField()),
                ("ratings_3", models.IntegerField()),
                ("ratings_4", models.IntegerField()),
                ("ratings_5", models.IntegerField()),
                ("image_url", models.URLField()),
                ("small_image_url", models.URLField()),
            ],
        ),
    ]
