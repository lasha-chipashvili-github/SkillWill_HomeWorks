from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    slug = models.SlugField(unique=True, blank=False, null=False)

    def __str__(self):
        return self.category_name
#
# class PostTag(models.Model):
#     tag = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#
#     def __str__(self):
#         return self.tag


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    post_body = models.TextField(blank=False, null=False)
    post_cat = models.ForeignKey(Category, on_delete=models.RESTRICT)
#    post_tag = models.ManyToManyField(PostTag, blank=True, related_name='tags')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


