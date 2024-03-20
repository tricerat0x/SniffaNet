from django.urls import path
from . import views

urlpatterns = [
    path('reports/', views.ReportList.as_view(), name='reports_index'),
    path('reports/<int:pk>/', views.ReportDetail.as_view(), name='reports_detail'),
    path('reports/<int:pk>/delete/', views.ReportDelete.as_view(), name='reports_delete'),


]