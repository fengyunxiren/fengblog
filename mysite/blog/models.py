from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    create_time = models.DateTimeField(auto_now_add=timezone.now())
    update_time = models.DateTimeField(auto_now=timezone.now())
    is_delete = models.BooleanField(default=False)
    name = models.CharField(max_length=128, unique=True)
    describle = models.CharField(max_length=256, default="")
    # image = models.ImageField(upload_to='/var/test')

    def __str__(self):
        return self.name

class Author(models.Model):
    create_time = models.DateTimeField(auto_now_add=timezone.now())
    update_time = models.DateTimeField(auto_now=timezone.now())
    is_delete = models.BooleanField(default=False)
    name = models.CharField(max_length=64)
    nickname = models.CharField(max_length=64, default="")
    gender = models.IntegerField(choices=((0, 'secret'), (1, 'male'), (2, 'female')), default=0)
    signature = models.CharField(max_length=128, default='lol')

    def __str__(self):
        return self.name



class Article(models.Model):
    create_time = models.DateTimeField(auto_now_add=timezone.now())
    update_time = models.DateTimeField(auto_now=timezone.now())
    is_delete = models.BooleanField(default=False)
    title = models.CharField(max_length=128)
    describle = models.CharField(max_length=256)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title


class Images(models.Model):
    create_time = models.DateTimeField(auto_now_add=timezone.now())
    update_time = models.DateTimeField(auto_now=timezone.now())
    is_delete = models.BooleanField(default=False)
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='static/myphoto/%Y/%m/%d/', null=True, max_length=255)

    def __str__(self):
        return self.name
