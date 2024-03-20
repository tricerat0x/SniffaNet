# main_app/urls.py

from django.urls import path
from .views import perform_scan

urlpatterns = [
    path('perform_scan/', perform_scan, name='perform_scan'),
]
