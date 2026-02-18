from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
from .models import Tarefa

# Create your views here.

def home(request):
    contexto = {
        "nome": "Joao",
        "data": date.today(),
    }
    return render(request, "home.html", contexto)

def lista(request):
    tarefas = Tarefa.objects.all()  # SELECT no banco
    contexto = {"tarefas": tarefas}
    return render(request, "lista.html", contexto)