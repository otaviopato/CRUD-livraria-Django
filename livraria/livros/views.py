from django.shortcuts import render, redirect, get_object_or_404
from livros.forms import LivroForm
from livros.models import Livro
from autores.models import Autor, AutorLivro
from django.utils.timezone import now

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'listar_livro.html', {'livros': livros})

def novo_livro(request):
    formLivro = LivroForm(request.POST, None)
    formLivro.base_fields['criado_em'].prepare_value(now())
    if formLivro.is_valid():
        print('entoru')
        formLivro.save()
        return redirect('listar_livro')
    return render(request, 'novo_livro.html', {'formLivro': formLivro})

def atualizar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    formLivro = LivroForm(request.POST or None, request.FILES or None, instance=livro)

    if formLivro.is_valid():
        formLivro.save()
        return redirect('listar_livro')

    return render(request, 'atualizar_livros.html', {'formLivro': formLivro, 'livro': livro})

def detalhe_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    return render(request, 'detalhe_livros.html', {'livro': livro})

def deletar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livro')
    return render(request, 'deletar_livro.html', { 'livro': livro })

def vincular_autor_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    autores_livro = AutorLivro.objects.all().filter(livro_id=id)
    autores = []
    for autor_livro in autores_livro:
        autores.append(autor_livro.autor_id)
    formLivro = LivroForm(request.POST or None, request.FILES or None, instance=livro)

    if formLivro.is_valid():
        formLivro.save()
        return redirect('listar_livro')

    return render(request, 'vincular_autor_a_livro.html', {'formLivro': formLivro, 'livro': livro, 'autores': autores})
