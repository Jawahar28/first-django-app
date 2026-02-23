from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    age = models.IntegerField(default=10)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.PositiveIntegerField()
    description = models.CharField(max_length=255)
