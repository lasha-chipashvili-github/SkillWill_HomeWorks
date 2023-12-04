from django.db import models
import datetime


# Create your models here.
class Kalendari(models.Model):
    tarigi = models.DateTimeField(auto_now=True, blank=False)


if __name__ == "__main__":
    today = Kalendari()
    today.save()