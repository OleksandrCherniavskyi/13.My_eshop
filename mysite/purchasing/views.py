
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Supplier, SupplierItem
from .forms import AddSupplierForm, AddSupplierItemForm

# Create your views here.
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
    return render(request, 'purchasing/add_supplier.html', {'form': form})

@login_required
def supplier_list(request):
    suppliers = Supplier.objects.all()
    context = {
        'suppliers': suppliers
    }
    return render(request, 'purchasing/supplier_list.html', context)


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
    return render(request, 'purchasing/add_supplieritem.html', {'form': form})


@login_required
def supplieritem_list(request, pk):
    supplier_items = SupplierItem.objects.filter(supplier_id=pk)
    context = {
        'supplier_items': supplier_items
    }
    return render(request, 'purchasing/supplieritem_list.html', context)

def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    context = {
        'supplier': supplier
    }
    return render(request, 'purchasing/supplier_detail.html', context)