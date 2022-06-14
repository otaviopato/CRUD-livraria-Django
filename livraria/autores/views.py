from django.shortcuts import render, redirect
from autores.forms import AutorForm

def novo_autor(request):
    formAutores = AutorForm(request.POST, None)
    if formAutores.is_valid():
        formAutores.save()
        redirect('/casa')
    return render(request, 'autores_create.html', {'formAutores': formAutores})