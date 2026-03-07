## Refatoração do sistema de tarefas para multiusuário

### Objetivo

Transformar o sistema de tarefas em um app multiusuário onde:

- **Usuário comum**: vê e gerencia apenas **suas** tarefas.
- **Admin (staff/superuser)**: consegue ver as tarefas de **todo mundo**.
- Após login, o usuário cai numa **tela genérica de boas-vindas** e a partir daí navega para suas tarefas.

---

## 1. Modelo `Tarefa` ligado ao usuário

Arquivo: `core/models.py`

```python
from django.conf import settings
from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    concluida = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    # NOVO: dono da tarefa
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tarefas'
    )

    def __str__(self):
        return self.titulo
```

**Conceitos para os slides**:

- `ForeignKey` ligando a tarefa ao `User`.
- Cada tarefa pertence a um usuário, então todas as consultas (queries) passam a filtrar por esse campo.

---

## 2. URLs principais e fluxo de navegação

Arquivo: `core/urls.py` (exemplo):

```python
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.login_view, name='login'),          # raiz = login
    path('home/', views.home, name='home'),            # tela genérica pós-login
    path('tarefas/', views.lista_tarefas, name='lista'),
    path('tarefas/nova/', views.criar_tarefa, name='criar'),
    path('tarefas/<int:pk>/editar/', views.editar_tarefa, name='editar'),
    path('tarefas/<int:pk>/excluir/', views.excluir_tarefa, name='excluir'),
    path('admin/tarefas/', views.tarefas_todos_usuarios, name='tarefas_todos'),
]
```

- `''` continua sendo a rota de **login**.
- Após login bem-sucedido, redirecionar para `/home/` (view `home`).
- As rotas de tarefas ficam sob `/tarefas/`.
- Uma rota específica (`admin/tarefas/`) mostra tarefas de todos os usuários para staff/admin.

---

## 3. View de boas-vindas pós-login

Arquivo: `core/views.py`

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='core:login')
def home(request):
    contexto = {
        'nome': request.user.username,
    }
    return render(request, 'core/home.html', contexto)
```

Uso típico:

- Depois que o login deu certo, fazer `return redirect('core:home')`.
- A tela `home.html` é genérica (“Bem-vindo, fulano”) e oferece links para:
  - “Minhas tarefas”
  - (Opcional) “Tarefas de todos os usuários” se `request.user.is_staff`.

---

## 4. Views de tarefas por usuário

### 4.1. Lista – apenas tarefas do usuário logado

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarefa
from .forms import TarefaForm

@login_required(login_url='core:login')
def lista_tarefas(request):
    tarefas = Tarefa.objects.filter(usuario=request.user).order_by('-criado_em')
    return render(request, 'core/lista.html', {'tarefas': tarefas})
```

### 4.2. Criar tarefa – sempre associando ao `request.user`

```python
@login_required(login_url='core:login')
def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user      # ponto-chave
            tarefa.save()
            return redirect('core:lista')
    else:
        form = TarefaForm()
    return render(request, 'core/criar.html', {'form': form})
```

### 4.3. Editar / excluir – garantindo que o dono é o usuário logado

```python
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
    return render(request, 'core/editar.html', {'form': form})

@login_required(login_url='core:login')
def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('core:lista')
    return render(request, 'core/confirmar_excluir.html', {'tarefa': tarefa})
```

**Conceitos para os slides (autenticação/autorização)**:

- Uso de `request.user` em queries:
  - `Tarefa.objects.filter(usuario=request.user)`.
- Restrição por dono do objeto:
  - `get_object_or_404(Tarefa, pk=pk, usuario=request.user)`.

---

## 5. View para admin ver tarefas de todos os usuários

Aproveitar o **Django Admin** já é suficiente, mas é didático ter uma view simples:

```python
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required(login_url='core:login')
def tarefas_todos_usuarios(request):
    tarefas = Tarefa.objects.select_related('usuario').order_by('-criado_em')
    return render(request, 'core/tarefas_todos.html', {'tarefas': tarefas})
```

Conceitos:

- `@staff_member_required` limita o acesso a usuários com `is_staff=True`.
- `select_related('usuario')` otimiza a consulta juntando o usuário junto com a tarefa.

Template de exemplo (bem simples):

```html
<!-- core/tarefas_todos.html -->
<h1>Tarefas de todos os usuários</h1>

<table>
  <thead>
    <tr>
      <th>Título</th>
      <th>Usuário</th>
      <th>Concluída?</th>
      <th>Criado em</th>
    </tr>
  </thead>
  <tbody>
    {% for tarefa in tarefas %}
    <tr>
      <td>{{ tarefa.titulo }}</td>
      <td>{{ tarefa.usuario.username }}</td>
      <td>{{ tarefa.concluida|yesno:"Sim,Não" }}</td>
      <td>{{ tarefa.criado_em }}</td>
    </tr>
    {% empty %}
    <tr>
      <td colspan="4">Nenhuma tarefa cadastrada.</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
```

---

## 6. Templates simples para o fluxo

### 6.1. `home.html` (pós-login)

```html
<h1>Bem-vindo, {{ nome }}!</h1>

<p>Escolha uma opção:</p>
<ul>
  <li><a href="{% url 'core:lista' %}">Minhas tarefas</a></li>
  {% if request.user.is_staff %}
  <li>
    <a href="{% url 'core:tarefas_todos' %}">Tarefas de todos os usuários</a>
  </li>
  {% endif %}
</ul>
```

### 6.2. `lista.html` (minhas tarefas)

```html
<h1>Minhas tarefas</h1>

<p><a href="{% url 'core:criar' %}">Nova tarefa</a></p>

<ul>
  {% for tarefa in tarefas %}
  <li>
    {{ tarefa.titulo }} {% if tarefa.concluida %}(concluída){% endif %} –
    <a href="{% url 'core:editar' tarefa.pk %}">editar</a> –
    <a href="{% url 'core:excluir' tarefa.pk %}">excluir</a>
  </li>
  {% empty %}
  <li>Você ainda não tem tarefas.</li>
  {% endfor %}
</ul>
```

Os demais templates (`criar.html`, `editar.html`, `confirmar_excluir.html`) podem aproveitar o padrão já usado nas BEPs (form simples com `{{ form.as_p }}` ou equivalente).

---

## 7. Pontos que precisam aparecer nos slides

### 7.1. BEP039 – Formulários

- Uso de `form.save(commit=False)` para:
  - Ajustar campos que **não** vêm do formulário (por exemplo, `usuario`).
  - Exemplo direto:

    ```python
    tarefa = form.save(commit=False)
    tarefa.usuario = request.user
    tarefa.save()
    ```

### 7.2. BEP040 – Autenticação e Autorização

- `request.user` como forma de acessar o usuário logado.
- Filtrar dados por usuário:

  ```python
  Tarefa.objects.filter(usuario=request.user)
  ```

- Proteger acesso a objetos por dono:

  ```python
  get_object_or_404(Tarefa, pk=pk, usuario=request.user)
  ```

- Conceitos de `is_staff` / `is_superuser` e `@staff_member_required`.
- Fluxo pós-login:
  - Login → `redirect('core:home')` → `home` com `@login_required` e saudação usando `request.user.username`.

---
