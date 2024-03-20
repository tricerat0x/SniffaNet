# main_app/urls.py

from django.urls import path
from . import views
from .views import perform_scan
	
urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.user, name='user'),
    path('reports/', views.reports, name='reports'),
    path('perform_scan/', perform_scan, name='perform_scan'),
]







    

