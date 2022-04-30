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
    description = models.CharField(max_length=1000, default="No description available")
    availability = models.CharField(max_length=100, default="Lend")

    def __str__(self):
        return self.book_name

class Contact(models.Model):
    query_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    subject = models.CharField(max_length=70)
    query = models.CharField(max_length=500)

    def __str__(self):
        return self.name