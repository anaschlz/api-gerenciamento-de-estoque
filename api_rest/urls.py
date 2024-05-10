from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_products, name='get_all_products'),  # Rota para listar todos os produtos
    path('product/<int:pk>/', views.get_product_by_id),  # Rota para obter detalhes de um produto por ID
    path('data/<int:pk>/', views.manage_product),  # Rota para criar ou excluir um produto
]

