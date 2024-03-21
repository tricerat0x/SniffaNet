from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('oauth2callback/', views.home, name='home'),
    path('user/', views.user, name='user'),
    path('reports/', views.index, name='reports'),
    path('reports/<int:report_id>/', views.detail, name='reports_detail'),
    path('scan_devices/', views.scan_devices, name='scan_devices'),
]

