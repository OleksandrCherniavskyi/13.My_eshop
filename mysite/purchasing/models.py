
from django.db import models


from django.contrib.auth.models import User

from django.utils import timezone



class Purchasing(models.Model):
    date = models.DateField()
    item = models.ForeignKey('warehouses.Item', on_delete=models.CASCADE)
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
    item = models.ForeignKey('warehouses.Item', related_name='supplieritem', on_delete=models.CASCADE)
    link = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name='supplieritem', on_delete=models.CASCADE, null=True, blank=True)
