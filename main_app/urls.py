# main_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.user, name='user'),
    path('reports/', views.reports, name='reports'),  # Fixedish the URL pattern to point to the reports view?
    path('reports/<int:report_id>/', views.detail, name='reports_detail'),
    path('scan_devices/', views.scan_devices, name='scan_devices'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),  
]


