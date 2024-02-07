
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Warehouse, Item, Category, Supplier, SupplierItem
from .forms import AddItemForm, AddCategoryForm, AddSupplierForm, AddSupplierItemForm


@login_required
def warehouses(request):
    avalible_item = Warehouse.objects.all()

    context = {
        'avalible_item': avalible_item,
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

            return redirect('item_list')  # Redirect to the item list or any other view
    else:
        form = AddCategoryForm()

    avalible_category = Category.objects.all()
    context = {
        'avalible_category': avalible_category,
        'form': form,
    }

    return render(request, 'warehouses/add_category.html', context)

@login_required
def add_supplier(request):
    if request.method == 'POST':
        form = AddSupplierForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.created_by = request.user
            form.save()

            return redirect('supplier_list')  # Redirect to the item list or any other view
    else:
        form = AddSupplierForm()
    return render(request, 'warehouses/add_supplier.html', {'form': form})

@login_required
def supplier_list(request):
    suppliers = Supplier.objects.all()
    context = {
        'suppliers': suppliers
    }
    return render(request, 'warehouses/supplier_list.html', context)


@login_required
def add_supplieritem(request):
    if request.method == 'POST':
        form = AddSupplierItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.created_by = request.user
            form.save()

            return redirect('supplieritem_list')  # Redirect to the item list or any other view
    else:
        form = AddSupplierItemForm()
    return render(request, 'warehouses/add_supplieritem.html', {'form': form})


@login_required
def supplieritem_list(request):
    supplieritems = SupplierItem.objects.all()
    context = {
        'supplieritems': supplieritems
    }
    return render(request, 'warehouses/supplieritem_list.html', context)

