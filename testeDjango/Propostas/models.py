import os

from django.conf import settings
from django.db import models
from PIL import Image


class CampoProposta(models.Model):
    TIPOS_CAMPO = [
        ('texto', 'Texto'),
        ('imagem', 'Imagem'),
        ('arquivo', 'Arquivo'),
        ('booleano', 'Booleano'),
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
    imagem = models.ImageField(upload_to='propostas/imagens/%Y/%m/', null=True, blank=True)
    arquivo = models.FileField(upload_to='propostas/arquivos/%Y/%m/', null=True, blank=True)
    booleano = models.BooleanField(null=True, blank=True)

    @staticmethod
    def resize_image(img, new_with=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_with:
            img_pil.close()
            return
        new_height = round((new_with * original_height) / original_width)
        new_img = img_pil.resize((new_with, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)
    def __str__(self):
        return f"Resposta para '{self.campo.nome}'"