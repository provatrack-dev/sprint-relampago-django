from django.shortcuts import render, redirect
from .models import Projeto
from .forms_projetos import ProjetoForm


def projeto_lista(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos/lista.html', {'projetos': projetos})


def projeto_criar(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projeto_lista')
    else:
        form = ProjetoForm()
    return render(request, 'projetos/form.html', {'form': form})