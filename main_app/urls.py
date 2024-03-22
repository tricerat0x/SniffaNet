from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('reports/', views.reports_index, name='reports'),
    path('reports/<int:pk>/', views.reports_detail, name='reports_detail'),
    path('reports/<int:pk>/delete/', views.ReportDelete.as_view(), name='reports_delete'),
    path('profile/', views.profile_detail, name='profile_detail'),
    path('profile/update/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('accounts/signup/', views.signup, name='signup'),
    path('user/', views.user, name='user'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),


]