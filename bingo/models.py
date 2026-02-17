from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.PositiveIntegerField()
    description = models.CharField(max_length=255)
