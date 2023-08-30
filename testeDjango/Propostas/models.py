import os

from django.conf import settings
from django.db import models
from PIL import Image


class CampoProposta(models.Model):
    TIPOS_CAMPO = [
        ('texto', 'Texto'),
    ]

    tipo = models.CharField(max_length=10, choices=TIPOS_CAMPO)
    nome = models.CharField(max_length=200)  # Nome do campo

    def __str__(self):
        return self.nome


class Proposta(models.Model):
    nome = models.CharField(max_length=200)
    campos = models.ManyToManyField(CampoProposta, through='ValorCampo')
    def __str__(self):
        return f"Proposta de {self.nome}"
    

class ValorCampo(models.Model):
    proposta = models.ForeignKey(Proposta, on_delete=models.CASCADE)
    campo = models.ForeignKey(CampoProposta, on_delete=models.CASCADE)
    texto = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Resposta para '{self.campo.nome}'"