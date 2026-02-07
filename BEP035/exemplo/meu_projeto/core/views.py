from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Tarefa

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

# Create your views here.
