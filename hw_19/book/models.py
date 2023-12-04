from django.db import models

# Create your models here.
class Book(models.Model):
    book_title = models.CharField(max_length=255, blank=False)
    book_author = models.CharField(max_length=255, blank=False)
    book_publisher = models.CharField(max_length=255, blank=False)
    book_number_of_pages = models.IntegerField(blank=False)
    book_price = models.FloatField(blank=False)

    # def __str__(self):
    #     return self.book_title, self.book_author

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"

