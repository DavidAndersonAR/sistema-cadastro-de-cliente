from django.db import models

# Create your models here.



class NomeUsuario(models.Model):

    ESTADO_CIVIL = (
        ("solteiro", "solteiro"),
        ("casado", "casado"),
        ("viuvo", "viuvo"),
    )

    GENEROS = (
        ("masculino", "masculino"),
        ("feminino", "feminino"),
        ("outros", "outros"),
    )


    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120)
    cel = models.IntegerField()
    email = models.EmailField(null=False, blank=False)
    cpf = models.IntegerField()

    estado_civil = models.CharField(max_length=40, choices=ESTADO_CIVIL, blank=False, null=False)
    genero = models.CharField(max_length=40, choices=GENEROS, blank=False, null=False)

    rua = models.CharField(max_length=80)
    complemento = models.CharField(max_length=40)
    cidade = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)
    cep = models.CharField(max_length=40)

    def __str__(self):
        return self.nome