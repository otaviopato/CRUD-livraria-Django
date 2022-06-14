import uuid
from datetime import datetime
from django.db import models

class Livro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=50)
    data_criacao = models.DateTimeField()
    numero_pagina = models.IntegerField()
    produtora = models.CharField(max_length=50)
    criado_em = models.DateTimeField(default=datetime.now, blank=True, verbose_name="Criado em", help_text="Data de criação do registro")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em", help_text="Data da última atualização do registro")
    class Meta:
        verbose_name = ('Livro')
