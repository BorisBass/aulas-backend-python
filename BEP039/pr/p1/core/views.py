# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Tarefa
from .forms import TarefaForm


def lista(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'lista.html', {'tarefas': tarefas})

def criar(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao', '').strip()
        if descricao:
            Tarefa.objects.create(descricao=descricao)
        # Redireciona para a lista usando o nome da rota (não a URL fixa)
        return redirect(reverse('core:lista'))
    return render(request, 'criar.html')

def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)  # cria form com dados do POST
        if form.is_valid():  # valida os dados
            descricao = form.cleaned_data['descricao']  # dados limpos
            prioridade = form.cleaned_data['prioridade']
            status = form.cleaned_data['status']
            Tarefa.objects.create(descricao=descricao, prioridade=prioridade, status=status)
            return redirect('core:lista')

    else:
        form = TarefaForm()  # form vazio para GET
    
    return render(request, 'criar_tarefa.html', {'form': form})


def detalhar(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    # Gera a URL de edição para esta tarefa (ex: /editar/5/)
    url_editar = reverse('core:editar', args=[id])
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
        return redirect(reverse('core:detalhar', args=[id]))
    return render(request, 'editar.html', {'tarefa': tarefa})