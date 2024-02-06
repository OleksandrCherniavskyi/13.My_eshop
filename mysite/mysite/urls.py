from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views





urlpatterns = [

    path('', include("core.urls")),
    path('', include("userprofile.urls")),
    path('', include("dashboard.urls")),
    path('warehouses/', include('warehouses.urls')),
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

]
