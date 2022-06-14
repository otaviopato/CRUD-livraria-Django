"""Company forms"""
from django import forms
from catalogos.models import Catalogo, CatalogoLivro
from django.forms import ModelForm

class CatalogoForm(ModelForm):
    class Meta:
        model = Catalogo
        fields = '__all__'

class CatalogoLivroForm(ModelForm):
    class Meta:
        model = CatalogoLivro
        fields = '__all__'
