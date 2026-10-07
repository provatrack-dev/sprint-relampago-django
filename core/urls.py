from django.urls import path
from . import views_projetos, views_tarefas

urlpatterns = [
    # --- Projetos (SAMUEL) ---
    path('', views_projetos.projeto_lista, name='projeto_lista'),
    path('projetos/novo/', views_projetos.projeto_criar, name='projeto_criar'),
    path('projetos/<int:pk>/editar/', views_projetos.projeto_editar, name='projeto_editar'),
    path('projetos/<int:pk>/excluir/', views_projetos.projeto_excluir, name='projeto_excluir'),

    # --- Tarefas (VITOR) ---
]