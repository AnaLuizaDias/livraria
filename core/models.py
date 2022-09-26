import site
from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=255)

class editora(models.Model):
    descricao = models.CharField(max_length=255)
    site = models.URLField()