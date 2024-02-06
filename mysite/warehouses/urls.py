# Add these lines to your urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'warehouses'

urlpatterns = [
    path('', views.warehouses, name='index'),
]

if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
