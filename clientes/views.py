from django.shortcuts import HttpResponse, render,redirect
from .models import NomeUsuario

# Create your views here.

def tela_inicio(request):

    return render(request, "cadastro_produto.html")

#cadastro de novos clientes
def cadastro_de_clientes(request):
    novo_cliente = NomeUsuario()
   

    novo_cliente.nome = request.POST.get('nome')
    novo_cliente.cel = request.POST.get("tel")
    novo_cliente.email = request.POST.get("email")
    novo_cliente.cpf = request.POST.get("cpf")
    novo_cliente.estado_civil = request.POST.get("estado_civil")
    novo_cliente.genero = request.POST.get("genero_select")
    novo_cliente.rua = request.POST.get("rua")
    novo_cliente.complemento = request.POST.get("complemento")
    novo_cliente.cidade = request.POST.get("cidade")
    novo_cliente.estado = request.POST.get("estado")
    novo_cliente.cep = request.POST.get("cep")

    novo_cliente.save()
    return redirect("tela_inicio")
    #return HttpResponse("teste")
    #return render(request, "cadastro_produto.html")
   