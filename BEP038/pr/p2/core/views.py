# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa

def lista(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'lista.html', {'tarefas': tarefas})

def criar(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao', '').strip()
        if descricao:
            Tarefa.objects.create(descricao=descricao)
        return redirect('/')  # URL fixa: se mudar a rota no urls.py, aqui quebra
    return render(request, 'criar.html')

def detalhar(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    url_editar = f'/editar/{id}/'  # montado na mão
    return render(request, 'detalhar.html', {
        'tarefa': tarefa,
        'url_editar': url_editar,
    })

def editar(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        descricao = request.POST.get('descricao', '').strip()
        if descricao:
            tarefa.descricao = descricao
            tarefa.save()
        return redirect(f'/detalhar/{id}/')  # URL fixa
    return render(request, 'editar.html', {'tarefa': tarefa})