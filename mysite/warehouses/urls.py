# Add these lines to your urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


urlpatterns = [
    path('', views.warehouses, name='warehouses'),
    path('add_item', views.add_item, name='add_item'),
    path('item_list', views.item_list, name='item_list'),
    path('add_category', views.add_category, name='add_category'),
    #path('add_supplier', views.add_supplier, name='add_supplier'),
    #path('supplier_list', views.supplier_list, name='supplier_list'),
    #path('supplieritem_list', views.supplieritem_list, name='supplieritem_list'),
    #path('add_supplieritem', views.add_supplieritem, name='add_supplieritem'),

]

if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
