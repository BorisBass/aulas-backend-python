from django.conf import settings
from django.db import models


class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    prioridade = models.CharField(max_length=20)  # alta, media, baixa
    status = models.IntegerField(default=0)       # 0 a 100
    concluida = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tarefas'
    )

    def __str__(self):
        return self.titulo