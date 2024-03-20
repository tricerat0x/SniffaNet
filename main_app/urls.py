from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.user, name='user'),
    path('reports/', views.index, name='reports'),
    path('scan_devices/', views.scan_devices, name='scan_devices'),
    # Add other paths as needed
]
