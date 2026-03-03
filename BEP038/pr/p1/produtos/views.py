from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

# Create your views here.

produtos = [
    {"id": 1, "desc": "Caneta BIC", "preco": 1.50 },
    {"id": 2, "desc": "Lápis", "preco": 1.0 },
    {"id": 3, "desc": "Borracha 2 cores", "preco": 0.50 }
]


def home(request):
    contexto = {
        "nome": "App de Produtos",
        "data": date.today(),
    }
    return render(request, "produtos/home.html", contexto)

def lista(request):
    contexto = {"produtos": produtos}
    return render(request, "produtos/lista.html", contexto)