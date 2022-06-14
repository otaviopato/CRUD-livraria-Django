from django import forms
from autores.models import Autor, AutorLivro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class AutorLivroForm(forms.ModelForm):
    class Meta:
        model = AutorLivro
        fields = '__all__'
