from django.urls import path

from book.views import BookDetailView
from book.views import BookReserveView
from book.views import BookView

urlpatterns = [
    path("books/", BookView.as_view(), name="books"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("book/<int:pk>/reserve/", BookReserveView.as_view(), name="book-reserve"),
]
