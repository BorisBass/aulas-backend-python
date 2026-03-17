# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Tarefa
from .forms import TarefaForm

@login_required
def lista(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'lista.html', {'tarefas': tarefas})

@login_required
def criar(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao', '').strip()
        if descricao:
            Tarefa.objects.create(descricao=descricao)
        # Redireciona para a lista usando o nome da rota (não a URL fixa)
        return redirect(reverse('core:lista'))
    return render(request, 'criar.html')

@login_required
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

@login_required
def detalhar(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    # Gera a URL de edição para esta tarefa (ex: /editar/5/)
    url_editar = reverse('core:editar', args=[id])
    return render(request, 'detalhar.html', {
        'tarefa': tarefa,
        'url_editar': url_editar,
    })

@login_required
def editar(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        descricao = request.POST.get('descricao', '').strip()
        if descricao:
            tarefa.descricao = descricao
            tarefa.save()
        return redirect(reverse('core:detalhar', args=[id]))
    return render(request, 'editar.html', {'tarefa': tarefa})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # autentica o usuário
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # faz login do usuário
            return redirect('core:lista')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)  # encerra a sessão do usuário
    return redirect('core:login')