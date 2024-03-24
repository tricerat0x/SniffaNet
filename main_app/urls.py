from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout', views.logout_view, name='logout'),
    path('user/', views.user, name='user'),
    path('reports/', views.reports, name='reports'),
    path('scan-devices/', views.scan_devices, name='scan_devices'),  # Updated URL pattern
    path('scan-detail/<int:scan_result_id>/', views.scan_detail, name='scan_detail'),
]



