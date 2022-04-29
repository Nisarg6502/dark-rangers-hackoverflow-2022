from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static", default="")
    author = models.CharField(max_length=100)
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    publishing_house = models.CharField(max_length=100)
    ISBN_number = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name