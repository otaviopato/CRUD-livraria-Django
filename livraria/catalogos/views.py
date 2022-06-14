from django.shortcuts import render, redirect
from livros.forms import LivroForm
from catalogos.forms import CatalogoForm
from .models import Catalogo
from livros.models import Livro
from autores.models import Autor



def catalogo_create(request):
    formCatalogo = CatalogoForm(request.POST, None)
    if formCatalogo.is_valid():
        formCatalogo.save()
        redirect('')
    catalogo = Catalogo.objects.all()
    return render(request, 'catalogo_create.html', { 'formCatalogo': formCatalogo, 'catalogo': catalogo })

def catalogo_list(request):
    return render(request, 'catalogo_list.html')
