from django import forms
from .models import Tarefa


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'status', 'prazo', 'projeto']
        widgets = {
            'prazo': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }