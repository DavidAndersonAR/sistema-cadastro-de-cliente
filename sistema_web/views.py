from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def cadastro_produtos(request):

    return render(request, "cadastro_produto.html")

# Responsavel pelo login do usuario
def index(request):

    return render(request, "login.html")


def login_user(request):


    if request.method == 'GET':
    

        return render(request, "login.html")
    

    else:
     
        user = authenticate(request, username=request.POST["user"], password = request.POST["password"])
        login(request, user)

        return redirect("cadastro_produtos")



def cadastro(request):
    

    return render(request, "criar_login.html")

def usuario(request):


    user = User.objects.create_user(username=request.POST["user"], password=request.POST["password"])
    user.save() 

    login(request, user)

    return redirect("login")
    #return JsonResponse("Usuario criado com sucesso")




