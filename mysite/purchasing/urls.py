
from django.urls import path

from . import views


urlpatterns = [

    path('add_supplier', views.add_supplier, name='add_supplier'),
    path('supplier_list', views.supplier_list, name='supplier_list'),
    path('supplieritem_list', views.supplieritem_list, name='supplieritem_list'),
    path('add_supplieritem', views.add_supplieritem, name='add_supplieritem'),

]