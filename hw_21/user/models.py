from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)

    # USERNAME_FIELD = "email"

    # def get_absolute_url(self):
    #     return reverse("custom_user_detail", kwargs={"pk": self.pk})
    class Meta:
        db_table = 'custom_users'
        verbose_name = 'custom_user'
        verbose_name_plural = 'custom_users'


#%% hypothetic code


# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=64)
#     date_of_birth = models.DateField()
#
#     class Meta:
#         verbose_name = 'custom_user'
#         verbose_name_plural = 'custom_users'
#
#     def __str__(self):
#         return f"{self.email} - {self.date_of_birth}"
#