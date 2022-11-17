from django.db import models
from django.forms import ModelForm

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    register = models.CharField(max_length=8)
    area = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name} {self.register} {self.area}"


class Funcionario(models.Model):
    nome = models.CharField(max_length=30)
    registro = models.CharField(max_length=7)
    posto = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.id}: {self.nome} {self.registro} {self.posto}"

class Armario(models.Model):
    patrimonio = models.CharField(max_length=6)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name="Funcionario", blank=True)
    posicao = models.CharField(max_length=10)
    localizacao = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.id}: {self.patrimonio} {self.funcionario} {self.posicao}"

class Turno(models.Model):
    atual = models.CharField(max_length=10)
    primeiraopcao = models.CharField(max_length=10)
    segundaopcao = models.CharField(max_length=10)
    funcionario = models.ManyToManyField(Funcionario, blank=True)

    def __str__(self):
        return f"{self.atual} {self.primeiraopcao} {self.segundaopcao}"


