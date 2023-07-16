from django.db import models


class User(models.Model):
    pass


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
