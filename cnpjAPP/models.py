from django.db import models


class Empresa(models.Model):
    cnpj = models.CharField(max_length=200, blank=True, null=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    nomeFantasia = models.CharField(max_length=200, blank=True, null=True)