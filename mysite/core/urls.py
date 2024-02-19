from django.urls import path
# Add these lines to your urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('crm/', views.crm, name='crm'),
    ]


#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)