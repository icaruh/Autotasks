from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/<int:cliente_id>/', views.detalhes_cliente, name='detalhes_cliente'),
    path('clientes/novo/', views.adicionar_cliente, name='adicionar_cliente'),
]
