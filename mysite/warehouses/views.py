
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Warehouse, Item, Category
from .forms import AddItemForm, AddCategoryForm


@login_required
def warehouses(request):
    availability = Warehouse.objects.all()

    context = {
        'availability': availability
    }

    return render(request, 'warehouses/warehouses.html', context)


@login_required
def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.created_by = request.user
            form.save()

            return redirect('item_list')  # Redirect to the item list or any other view
    else:
        form = AddItemForm()

    return render(request, 'warehouses/add_item.html',{'form': form})

@login_required
def item_list(request):
    avalible_item = Item.objects.all()
    context = {
        'avalible_item': avalible_item
    }

    return render(request, 'warehouses/item_list.html', context)

@login_required
def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.created_by = request.user
            form.save()

            return redirect('add_category')  # Redirect to the item list or any other view
    else:
        form = AddCategoryForm()

    avalible_category = Category.objects.all()
    context = {
        'avalible_category': avalible_category,
        'form': form,
    }

    return render(request, 'warehouses/add_category.html', context)

