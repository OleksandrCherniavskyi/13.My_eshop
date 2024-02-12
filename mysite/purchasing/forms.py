from django import forms
from .models import Supplier, SupplierItem


class AddSupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('name', 'street', 'zip_code', 'city', 'nip',
                  'regon', 'site', 'contact', 'short_name', 'email',
                  'comment', )

class AddSupplierItemForm(forms.ModelForm):
    class Meta:
        model = SupplierItem
        fields = ('supplier', 'item', 'link', )
