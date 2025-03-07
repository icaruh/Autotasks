from django.urls import path
from .views import lista_veiculos, adicionar_veiculo

urlpatterns = [
    path('veiculos/', lista_veiculos, name="lista_veiculos"),
    path('veiculos/novo/', adicionar_veiculo, name="adicionar_veiculo"),
]
