
from django.urls import path

from . import views


urlpatterns = [

    path('add_supplier', views.add_supplier, name='add_supplier'),
    path('supplier_list', views.supplier_list, name='supplier_list'),
    #path('supplieritem_list', views.supplieritem_list, name='supplieritem_list'),
    path('supplieritem/<int:pk>/', views.supplieritem_list, name='supplieritem_list'),
    path('supplier/<int:pk>/', views.supplier_detail, name='supplier_detail'),

]