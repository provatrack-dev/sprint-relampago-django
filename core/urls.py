from django.urls import path
from . import views_projetos, views_tarefas

urlpatterns = [
    # --- Projetos (SAMUEL) ---
    path('', views_projetos.projeto_lista, name='projeto_lista'),
    path('projetos/novo/', views_projetos.projeto_criar, name='projeto_criar'),

    # --- Tarefas (VITOR) ---
]