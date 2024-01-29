from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    slug = models.SlugField(unique=True, blank=False, null=False)

    def __str__(self):
        return self.category_name



class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    post_body = models.TextField(blank=False, null=False)
    post_cat = models.ForeignKey(Category, on_delete=models.RESTRICT)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-edit_date"]

# Create your models here.
