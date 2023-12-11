from django.db import models

# Create your models here.
class Animal(models.Model):
    animal_name = models.CharField(max_length=50, blank=False, null=False, default="None")
    animal_kind = models.CharField(max_length=50, blank=False, null=False, default="None")
    animal_breed = models.CharField(max_length=50, blank=False, null=False, default="None")
    animal_age = models.FloatField(blank=False, default=0)
