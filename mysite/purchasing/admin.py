from django.contrib import admin
from .models import Supplier, SupplierItem, InvoiceIn, Purchasing


admin.site.register(Supplier)
admin.site.register(SupplierItem)
admin.site.register(Purchasing)
admin.site.register(InvoiceIn)