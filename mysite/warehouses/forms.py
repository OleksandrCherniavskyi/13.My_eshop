from django import forms
from .models import Item, Category, Supplier, SupplierItem

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'category', 'producer', "produce_code", 'size_x',
                  'size_y', 'size_z', 'comment', 'image',)


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name',)

class AddSupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('name', 'street', 'zip_code', 'city', 'nip',
                  'regon', 'site', 'contact', 'short_name', 'email',
                  'comment', )

class AddSupplierItemForm(forms.ModelForm):
    class Meta:
        model = SupplierItem
        fields = ('supplier', 'item', 'link',)