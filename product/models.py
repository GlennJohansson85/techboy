#------------------------------------------------------------------------------PRODUCT/MODELS.PY
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=0, null=True, blank=True)
    image_url = models.URLField(max_length= 1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)  

    def __str__(self):
        return self.title
