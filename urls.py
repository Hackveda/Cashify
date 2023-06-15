from django.urls import path
from cashify_app import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('devices/', views.device_list_view, name='device_list'),
    path('devices/create/', views.device_create_view, name='device_create'),
    path('devices/<int:device_id>/', views.device_detail_view, name='device_detail'),
    path('transactions/', views.transaction_view, name='transactions'),
    # Other URL patterns for repair services, refurbished devices, etc.
]
