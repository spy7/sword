# Generated by Django 5.1.1 on 2024-09-28 13:40

import django.db.models.deletion

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0007_remove_book_id_alter_book_book_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="BookReserve",
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
                ("reserve_date", models.DateTimeField(auto_now_add=True)),
                ("customer_name", models.CharField(max_length=255)),
                ("customer_email", models.EmailField(max_length=254)),
                (
                    "book",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="book.book"
                    ),
                ),
            ],
        ),
    ]
