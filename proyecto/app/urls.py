from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.store, name = 'Tienda'),
    path('cart/', views.cart, name = 'Carrito'),
    path('checkout/', views.checkout, name = 'Pago'),
    path('update_item/', views.updateItem, name = 'update_item'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('', views.inicio, name='inicio'),

    ]