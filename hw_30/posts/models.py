from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    body = models.TextField(blank=False, null=False)
    slug = models.SlugField(unique=True, null=False)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-id"]
