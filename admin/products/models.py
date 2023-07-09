from django.db import models
from django.contrib.auth.models import AbstractUser, User


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CustomUser(User):
    nickname = models.CharField(max_length=100)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    products = models.ManyToManyField(Product, related_name='users')
