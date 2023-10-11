from django.db import models

# Create your models here.


class NomeUsuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=120)
    cel = models.IntegerField()
    email = models.TextField(max_length=40)
    cpf = models.IntegerField()
    estado_civil = models.TextField(max_length=40)
    genero = models.TextField(max_length=40)
    rua = models.TextField(max_length=80)
    complemento = models.TextField(max_length=40)
    cidade = models.TextField(max_length=40)
    estado = models.TextField(max_length=40)
    cep = models.TextField(max_length=40)