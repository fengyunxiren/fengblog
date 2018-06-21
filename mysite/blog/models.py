from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    create_time = models.DateTimeField(auto_now_add=timezone.now())
    update_time = models.DateTimeField(auto_now=timezone.now())
    is_delete = models.BooleanField(default=False)
    name = models.CharField(max_length=128)
    describle = models.CharField(max_length=256, default="")
    image = models.ImageField(upload_to='/var/test')


class Tag(models.Model):
    create_time = models.DateTimeField(auto_now_add=timezone.now())
    update_time = models.DateTimeField(auto_now=timezone.now())
    is_delete = models.BooleanField(default=False)
    name = models.CharField(max_length=64)
    describle = models.CharField(max_length=128, default="")


class Article(models.Model):
    pass
