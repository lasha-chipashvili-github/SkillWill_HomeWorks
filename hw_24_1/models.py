from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    genre = models.CharField(max_length=255)
    release_date = models.DateField()
    director = models.CharField(max_length=255)
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.title
