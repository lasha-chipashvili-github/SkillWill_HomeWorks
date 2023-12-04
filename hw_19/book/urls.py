from django.urls import path
from .views import book

urlpatterns = [
    path("book/", book, name="book")
]