from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
