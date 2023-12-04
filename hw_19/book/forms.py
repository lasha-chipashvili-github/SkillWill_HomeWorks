from django import forms
from .models import Book

class BookForm(forms.Form):
    # book_title = forms.CharField(label="Title", max_length=255)
    # book_author = forms.CharField(label="Author", max_length=255)
    # book_publisher = forms.CharField(label="Publisher", max_length=255)
    # book_number_of_pages = forms.IntegerField(label="Pages")
    # book_price = forms.FloatField(label="Price")

    class Meta:
        model = Book
        fields = ["book_title", "book_author", "book_publisher", "book_number_of_pages", "book_price"]

