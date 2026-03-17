from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    # campos que aparecem na lista do admin
    list_display = ("id", "descricao", "prioridade", "status")