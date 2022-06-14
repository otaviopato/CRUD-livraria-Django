from django.urls import path, include
from .views import listar_livros, novo_livro, atualizar_livro, detalhe_livro, deletar_livro, vincular_autor_livro


urlpatterns = [
    path('listar/', listar_livros, name="listar_livro"),
    path('novo/', novo_livro, name="novo_livro"),
    path('detalhes/<str:id>', detalhe_livro, name="detalhe_livro"),
    path('atualizar/<str:id>', atualizar_livro, name="atualizar_livro"),
    path('deletar/<str:id>', deletar_livro, name="deletar_livro"),
    path('vincular-autor/<str:id>', vincular_autor_livro, name="vincular_autor_a_livro"),
]
