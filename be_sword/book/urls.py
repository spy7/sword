from django.urls import include
from django.urls import path

urlpatterns = [
    path("v1/", include("book.v1.urls")),
]
