from django.contrib import admin
from .models import Item, Supplier, SupplierItem, Category

admin.site.register(Item)
admin.site.register(Supplier)
admin.site.register(SupplierItem)
admin.site.register(Category)
