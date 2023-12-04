from django.db import models

# Create your models here.
class Reader(models.Model):
    reader_name = models.CharField(max_length=50, blank=False)
    reader_surname = models.CharField(max_length=50, blank=False)
    reader_id_number = models.IntegerField(blank=False, unique=True)