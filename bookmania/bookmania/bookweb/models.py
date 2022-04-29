from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    contact = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=500, default='')

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static", default="")
    author = models.CharField(max_length=100)
    provider = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    publishing_house = models.CharField(max_length=100)
    ISBN_number = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name