from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings
from django.utils import timezone



class Category(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.category_name

class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    producer = models.CharField(max_length=50, blank=True)
    produce_code = models.CharField(max_length=50, blank=True)
    size_x = models.FloatField(null=True, blank=True, default=0)
    size_y = models.FloatField(null=True, blank=True, default=0)
    size_z = models.FloatField(null=True, blank=True, default=0)
    weight = models.FloatField(null=True, blank=True, default=0)
    comment = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="static/warehouses/items/")
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.category} - {self.name} '

    def image_url(self):
        return os.path.join(settings.MEDIA_URL, str(self.image))



class Supplier(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=80, blank=True)
    nip = models.IntegerField(null=True, blank=True)
    regon = models.IntegerField(null=True, blank=True)
    site = models.CharField(max_length=200, blank=True)
    contact = models.CharField(max_length=200, blank=True)
    short_name = models.CharField(max_length=40, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    comment = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='suppliers', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.short_name


class SupplierItem(models.Model):
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    link = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name='supplieritem', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.item} - {self.supplier} - {self.link}"


class Warehouse(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    min_qty = models.IntegerField(null=True, blank=True)
    localization = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.item} - {self.qty} - {self.localization}"

class Purchasing(models.Model):
    date = models.DateField()
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    prise = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    delivery_time = models.DateField(null=True, blank=True)
    invoice = models.ForeignKey('InvoiceIn', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.date} - {self.item} - { self.qty} - {self.prise} - {self.supplier} - " \
               f"{self.delivery_time} - {self.invoice}"

class InvoiceIn(models.Model):
    date = models.DateField()
    invoice_number = models.CharField(max_length=50, blank=True)
    time_to_pay = models.DateField()
    done = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='static/warehouses/invoice_attachments/', null=True, blank=True)

    def __str__(self):
        return f"{self.date} - {self.invoice_number} - {self.done} - {self.attachment}"
