from django.db import models


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('andamento', 'Em andamento'),
        ('concluida', 'Concluída'),
    ]

    titulo = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    prazo = models.DateField(null=True, blank=True)
    criada_em = models.DateTimeField(auto_now_add=True)
    projeto = models.ForeignKey(
        'Projeto',
        on_delete=models.CASCADE,
        related_name='tarefas',
    )

    def __str__(self):
        return self.titulo