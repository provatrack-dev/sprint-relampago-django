from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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
            messages.success(request, 'Projeto cadastrado com sucesso!')
            return redirect('projeto_lista')
    else:
        form = ProjetoForm()
    return render(request, 'projetos/form.html', {'form': form})


def projeto_editar(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto atualizado com sucesso!')
            return redirect('projeto_lista')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'projetos/form.html', {'form': form})


def projeto_excluir(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        projeto.delete()
        messages.success(request, 'Projeto excluído com sucesso!')
        return redirect('projeto_lista')
    return render(request, 'projetos/confirmar_exclusao.html', {'projeto': projeto})