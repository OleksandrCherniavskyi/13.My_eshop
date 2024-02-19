from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def crm(request):
    return render(request, 'core/crm.html')