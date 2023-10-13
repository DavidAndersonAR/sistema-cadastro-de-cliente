from django.urls import path
from clientes.views import cadastro_de_clientes, tela_inicio, lista_de_clientes, excluir_cliente, editar_cliente

urlpatterns = [
 
    path('cadastro_de_clientes/', cadastro_de_clientes, name="cadastro_de_clientes"),
    path('lista_de_clientes/', lista_de_clientes, name="lista_de_clientes"),
    path('tela_inicio/', tela_inicio, name="tela_inicio"),
    path('excluir_cliente/<int:id_usuario>', excluir_cliente, name="excluir_cliente"),
    path('lista_de_clientes/<int:id_usuario>/edit/', editar_cliente, name="editar_cliente")
]