from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Warehouse



@login_required
def warehouses(request):
    avalible_item = Warehouse.objects.all()

    context = {
        'avalible_item': avalible_item,
    }

    return render(request, 'warehouses/warehouses.html', context)