from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    # campos que aparecem na lista do admin
    list_display = ("id", "titulo", "descricao", "prioridade", "status", "concluida", "criado_em", "usuario")