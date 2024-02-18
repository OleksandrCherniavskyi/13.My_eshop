from django import forms
from .models import Item, Category

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'category', 'producer', "produce_code", 'size_x',
                  'size_y', 'size_z', 'comment', 'image',)


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name',)

