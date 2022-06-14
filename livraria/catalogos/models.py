import uuid
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.db import models
from livros.models import Livro

class Catalogo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=40)
    data_criacao = models.DateField(auto_now=True)
    criado_em = models.DateTimeField(default=datetime.now, blank=True, verbose_name="Criado em", help_text="Data de criação do registro")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em", help_text="Data da última atualização do registro")
    class Meta:
        verbose_name = _('Catalogo')

class CatalogoLivro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    catalogo_id = models.ForeignKey(Catalogo, on_delete=models.CASCADE, db_column='catalogo_id') 
    livro_id = models.ForeignKey(Livro, on_delete=models.CASCADE, db_column='livro_id')
    criado_em = models.DateTimeField(default=datetime.now, blank=True, verbose_name="Criado em", help_text="Data de criação do registro")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em", help_text="Data da última atualização do registro")
    class Meta:
        verbose_name = _('Catalogo_Livro')
        unique_together = ['catalogo_id', 'livro_id']
