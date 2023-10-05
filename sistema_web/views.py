from django.shortcuts import render

# Create your views here.

def cadastro_produtos(request):

    return render(request, "cadastro_produto.html")
