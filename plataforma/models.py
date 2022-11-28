from django.contrib.auth.models import User
from django.db import models


class Escolas(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=256)
    cpf_cnpj = models.CharField(max_length=16)
    email = models.EmailField()
    telefone = models.CharField(max_length=19)
    responsavel = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Responsaveis(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=256)
    cpf_cnpj = models.CharField(max_length=16)
    email = models.EmailField()
    telefone = models.CharField(max_length=19)

    def __str__(self):
        return self.nome


class Transportadores(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=256)
    cpf_cnpj = models.CharField(max_length=16)
    email = models.EmailField()
    telefone = models.CharField(max_length=19)
    veiculo = models.CharField(max_length=50)
    placa = models.CharField(max_length=8)
    capacidade = models.IntegerField()

    def __str__(self):
        return self.nome


class Alunos(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=256)
    cpf_cnpj = models.CharField(max_length=16)
    email = models.EmailField()
    escola = models.CharField(max_length=50)
    end_escola = models.CharField(max_length=80)
    responsaveis = models.ForeignKey(Responsaveis, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    