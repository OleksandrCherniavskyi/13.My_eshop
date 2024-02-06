from django.contrib import admin
from .models import Item, Supplier, SupplierItem, Category, Warehouse, InvoiceIn, Purchasing
from django.db import models
from django.forms.widgets import CheckboxInput, ClearableFileInput
from django.utils.html import format_html



admin.site.register(Item)


admin.site.register(Supplier)
admin.site.register(SupplierItem)
admin.site.register(Category)
admin.site.register(Warehouse)
admin.site.register(Purchasing)

admin.site.register(InvoiceIn)
