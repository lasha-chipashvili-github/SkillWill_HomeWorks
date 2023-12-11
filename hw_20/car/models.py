from django.db import models


# Create your models here.
class Car(models.Model):
    car_type = models.CharField(blank=False, max_length=30)
    car_brand = models.CharField(blank=False, max_length=60)
    car_model = models.CharField(blank=False, max_length=60)
    car_production_year = models.IntegerField(blank=False)