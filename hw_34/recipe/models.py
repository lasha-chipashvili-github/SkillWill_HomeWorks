from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
     name = models.CharField(max_length=400)
     ingredient = models.CharField(max_length=1000)
     time=models.IntegerField()
     process= models.CharField(max_length=2000)
     user = models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self):
        return self.name , self.user
