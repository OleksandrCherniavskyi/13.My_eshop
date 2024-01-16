from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    producer = models.CharField(max_length=50)
    size_x = models.FloatField()
    size_y = models.FloatField()
    size_z = models.FloatField()
    weight = models.FloatField()
    comment = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=80)
    nip = int
    regon = int
    site = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    short_name = models.CharField(max_length=40)
    email = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.short_name

class SupplierItem(models.Model):
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.supplier} - {self.item}"