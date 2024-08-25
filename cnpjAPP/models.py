from django.db import models


class Empresa(models.Model):
    cnpj = models.CharField(max_length=200, blank=True, null=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    nomeFantasia = models.CharField(max_length=200, blank=True, null=True)


class Endereco(models.Model):
    cnpj = models.ForeignKey('Empresa', models.DO_NOTHING, blank=True, null=True)
    logradouro = models.CharField(max_length=200, blank=True, null=True)
    numero = models.CharField(max_length=200, blank=True, null=True)
    cep = models.CharField(max_length=200, blank=True, null=True)

    