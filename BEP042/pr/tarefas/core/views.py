from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Tarefa
from .forms import TarefaForm


@login_required(login_url='core:login')
def home(request):
    contexto = {'nome': request.user.username}
    return render(request, 'core/home.html', contexto)


@login_required(login_url='core:login')
def lista_tarefas(request):
    tarefas = Tarefa.objects.filter(usuario=request.user).order_by('-criado_em')
    return render(request, 'core/lista.html', {'tarefas': tarefas})


@staff_member_required(login_url='core:login')
def tarefas_todos_usuarios(request):
    tarefas = Tarefa.objects.select_related('usuario').order_by('-criado_em')
    return render(request, 'core/tarefas_todos.html', {'tarefas': tarefas})


@login_required(login_url='core:login')
def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            tarefa.save()
            return redirect('core:lista')
    else:
        form = TarefaForm()
    return render(request, 'core/criar.html', {'form': form})


@login_required(login_url='core:login')
def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('core:lista')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'core/editar.html', {'form': form, 'tarefa': tarefa})


@login_required(login_url='core:login')
def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('core:lista')
    return render(request, 'core/confirmar_excluir.html', {'tarefa': tarefa})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:home')
        messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')


@login_required(login_url='core:login')
def logout_view(request):
    logout(request)
    return redirect('core:login')