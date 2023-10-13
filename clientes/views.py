from django.shortcuts import HttpResponse, render,redirect, get_object_or_404
from django.urls import reverse
from .models import NomeUsuario
from .forms import UserForm

# Create your views here.

def tela_inicio(request):

    return render(request, "cadastro_produto.html")

#cadastro de novos clientes
def cadastro_de_clientes(request):
    novo_cliente = NomeUsuario()
   

    novo_cliente.nome = request.POST.get("nome")
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

def lista_de_clientes(request):
    clientes = NomeUsuario.objects.all

    contexto = {
        "clientes" : clientes
    }
    
    return render(request, "lista_de_clientes.html", contexto)

def excluir_cliente(request, id_usuario):

    cliente = get_object_or_404(NomeUsuario, id_usuario = id_usuario)
    cliente.delete()

    return redirect(reverse('lista_de_clientes'))
    
def editar_cliente(request, id_usuario):
    cliente = get_object_or_404(NomeUsuario, id_usuario = id_usuario)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=cliente)
        print('primeiro if')
        
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('editar_cliente', id_usuario=cliente.id_usuario)
    else:
        print('primeiro else')
        form = UserForm(instance=cliente)
    
    return render(request, "editar_cliente.html", {'form' : form})