import uuid
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.db import models
from livros.models import Livro

# https://docs.djangoproject.com/en/4.0/topics/db/models/
class Autor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=40)
    data_criacao = models.DateField(auto_now=True)
    criado_em = models.DateTimeField(default=datetime.now, blank=True, verbose_name="Data de Nascimento", help_text="Data de criação do registro")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em", help_text="Data da última atualização do registro")
    # https://docs.djangoproject.com/en/4.0/ref/models/options/
    class Meta:
        verbose_name = _('Autor')

# https://docs.djangoproject.com/en/4.0/topics/db/models/
class AutorLivro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE, db_column='autor_id') # models.DO_NOTHING
    livro_id = models.ForeignKey(Livro, on_delete=models.CASCADE, db_column='livro_id') # models.DO_NOTHING
    criado_em = models.DateTimeField(default=datetime.now, blank=True, verbose_name="Criado em", help_text="Data de criação do registro")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em", help_text="Data da última atualização do registro")
    # https://docs.djangoproject.com/en/4.0/ref/models/options/
    class Meta:
        verbose_name = _('Autor_Livro')
        unique_together = ['autor_id', 'livro_id']
