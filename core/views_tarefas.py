from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms_tarefas import TarefaForm


def tarefa_lista(request):
    tarefas = Tarefa.objects.select_related('projeto').all()
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})


def tarefa_criar(request):
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Tarefa cadastrada com sucesso!')
        return redirect('tarefa_lista')
    return render(request, 'tarefas/form.html', {'form': form})


def tarefa_editar(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    form = TarefaForm(request.POST or None, instance=tarefa)
    if form.is_valid():
        form.save()
        messages.success(request, 'Tarefa atualizada com sucesso!')
        return redirect('tarefa_lista')
    return render(request, 'tarefas/form.html', {'form': form})


def tarefa_excluir(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('tarefa_lista')
    return render(request, 'tarefas/confirmar_exclusao.html', {'tarefa': tarefa})