from django.urls import path
from . import views

urlpatterns = [
    path('reports/', views.reports_index, name='reports_index'),
    path('reports/<int:pk>/', views.reports_detail, name='reports_detail'),
    path('reports/<int:pk>/delete/', views.ReportDelete.as_view(), name='reports_delete'),


]