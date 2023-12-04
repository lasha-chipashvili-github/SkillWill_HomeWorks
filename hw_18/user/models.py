from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(blank=False, max_length=30)
    userlastname = models.CharField(blank=False, max_length=60)
    date_of_birth = models.DateField(blank=False)


if __name__ == "__main__":
    user = User(username="Lasha", userlastname="Chipashvili",dateofbirth='2000-12-13')
    user.save()