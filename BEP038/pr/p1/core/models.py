from django.db import models

class Tarefa(models.Model):
    descricao = models.CharField(max_length=200, db_index=True)  # cria indice neste campo
    prioridade = models.CharField(max_length=20)  # alta, media, baixa
    status = models.IntegerField(default=0)  # 0 a 100

    class Meta:
        indexes = [
            models.Index(fields=["prioridade"]),  # indice para buscas por prioridade
        ]

    def __str__(self):
        return f"Descrição: {self.descricao} / Prioridade: {self.prioridade}"