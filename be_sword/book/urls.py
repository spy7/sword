from django.urls import path

from book.views import BookDetailView
from book.views import BookView

urlpatterns = [
    path("books/", BookView.as_view(), name="books"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
]
