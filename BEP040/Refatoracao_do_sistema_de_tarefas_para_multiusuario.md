## Refatoração do sistema de tarefas para multiusuário

### Objetivo

Transformar o sistema de tarefas em um app multiusuário onde:

- **Usuário comum**: vê e gerencia apenas **suas** tarefas.
- **Admin (staff/superuser)**: consegue ver as tarefas de **todo mundo**.
- Após login, o usuário cai numa **tela genérica de boas-vindas** e a partir daí navega para suas tarefas.

---

## 1. Modelo `Tarefa` ligado ao usuário

Arquivo: `core/models.py`

Você pode manter os campos originais e incluir os novos (exemplo com `prioridade` e `status` como no `pr/p2/core`):

```python
from django.conf import settings
from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    prioridade = models.CharField(max_length=20)   # alta, media, baixa
    status = models.IntegerField(default=0)        # 0 a 100
    concluida = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    # dono da tarefa (não entra no formulário; preenchido na view)
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
- Cada tarefa pertence a um usuário; todas as consultas passam a filtrar por `usuario`.

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
    path('staff/tarefas/', views.tarefas_todos_usuarios, name='tarefas_todos'),
]
```

- `''` continua sendo a rota de **login**.
- Após login bem-sucedido, redirecionar para `/home/` (view `home`).
- As rotas de tarefas ficam sob `/tarefas/`.
- Uma rota específica (`admin/tarefas/`) mostra tarefas de todos os usuários para staff/admin.

---

## 2.1. Onde ficam os templates (estrutura de pastas)

O Django, com `APP_DIRS: True` nos `TEMPLATES` do `settings.py`, procura templates dentro de cada app na pasta **`templates/`**. Para evitar conflito de nomes entre apps, costumamos criar uma subpasta com o nome do app. No app `core`, a estrutura fica assim:

```
core/
├── models.py
├── views.py
├── forms.py
├── urls.py
└── templates/
    └── core/
        ├── home.html           ← tela de boas-vindas pós-login
        ├── lista.html         ← listagem “minhas tarefas” (rota tarefas/)
        ├── criar.html         ← formulário nova tarefa (rota tarefas/nova/)
        ├── editar.html         ← formulário editar (rota tarefas/<pk>/editar/)
        ├── confirmar_excluir.html  ← confirmação de exclusão (rota tarefas/<pk>/excluir/)
        └── tarefas_todos.html  ← lista para staff (rota admin/tarefas/)
```

O template de **login** não precisa estar no namespace do app; pode ficar em `core/templates/login.html` e ser chamado como `'login.html'` no `render()` (desde que o Django encontre esse caminho).

**Como o `render()` usa esses arquivos**

- `render(request, 'core/home.html', ...)` → procura em `core/templates/core/home.html`.
- `render(request, 'core/lista.html', ...)` → procura em `core/templates/core/lista.html`.
- Ou seja: o **primeiro** `core` é o “caminho lógico” do template (nome do template); o **segundo** é a pasta física dentro de `core/templates/`.

Resumo por rota:

| Rota                     | View                     | Template (caminho lógico)       | Arquivo físico                               |
| ------------------------ | ------------------------ | ------------------------------- | -------------------------------------------- |
| `/`                      | `login_view`             | `'login.html'`                  | `core/templates/login.html`                  |
| `/home/`                 | `home`                   | `'core/home.html'`              | `core/templates/core/home.html`              |
| `/tarefas/`              | `lista_tarefas`          | `'core/lista.html'`             | `core/templates/core/lista.html`             |
| `/tarefas/nova/`         | `criar_tarefa`           | `'core/criar.html'`             | `core/templates/core/criar.html`             |
| `/tarefas/<pk>/editar/`  | `editar_tarefa`          | `'core/editar.html'`            | `core/templates/core/editar.html`            |
| `/tarefas/<pk>/excluir/` | `excluir_tarefa`         | `'core/confirmar_excluir.html'` | `core/templates/core/confirmar_excluir.html` |
| `/staff/tarefas/`        | `tarefas_todos_usuarios` | `'core/tarefas_todos.html'`     | `core/templates/core/tarefas_todos.html`     |

---

## 3. Refatoração do `forms.py`

O formulário deve refletir os campos do modelo que o usuário pode editar. Os campos **`usuario`** e **`criado_em`** não entram no form: o primeiro é preenchido na view com `request.user`; o segundo é automático (`auto_now_add=True`).

Use **ModelForm** para reaproveitar o modelo e incluir todos os campos desejados (incluindo `titulo`, `descricao`, `prioridade`, `status`, `concluida`):

Arquivo: `core/forms.py`

```python
from django import forms
from django.core.exceptions import ValidationError
from .models import Tarefa


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'prioridade', 'status', 'concluida']
        # não incluir: usuario (definido na view), criado_em (automático)
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'prioridade': 'Prioridade',
            'status': 'Status (%)',
            'concluida': 'Concluída',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Estudar Django'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'prioridade': forms.Select(choices=[('alta', 'Alta'), ('media', 'Média'), ('baixa', 'Baixa')], attrs={'class': 'form-control'}),
            'status': forms.NumberInput(attrs={'min': 0, 'max': 100, 'class': 'form-control'}),
            'concluida': forms.CheckboxInput(),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if titulo and len(titulo.strip()) < 3:
            raise ValidationError('O título deve ter pelo menos 3 caracteres.')
        return titulo.strip() if titulo else titulo
```

Se no seu modelo não existir `prioridade` nem `status`, use apenas:

```python
fields = ['titulo', 'descricao', 'concluida']
```

**Importante**: na view de **criar** tarefa, você continua fazendo:

```python
tarefa = form.save(commit=False)
tarefa.usuario = request.user
tarefa.save()
```

assim o campo `usuario` nunca vem do formulário e fica sempre correto.

---

## 4. View de boas-vindas pós-login

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

## 5. Views de tarefas por usuário

### 5.1. Lista – apenas tarefas do usuário logado

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

### 5.2. Criar tarefa – sempre associando ao `request.user`

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

### 5.3. Editar / excluir – garantindo que o dono é o usuário logado

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

## 6. View para admin ver tarefas de todos os usuários

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

## 7. Templates simples para o fluxo

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

Os templates `criar.html` e `editar.html` devem ter um `<form method="post" action="...">` com `{% csrf_token %}` e `{{ form.as_p }}` (ou equivalente).

### 7.3. `confirmar_excluir.html` (exclusão) – modelo correto

A view **não envia** um objeto `form`; ela envia só `tarefa`. O template de excluir é apenas uma **página de confirmação**: um formulário em POST para a mesma URL (ou para a rota de excluir) com um botão “Excluir”. **Não** use `{{ form.as_p }}` aqui.

**Erros comuns** no template de excluir:

- Título dizendo “Editar” em vez de “Excluir”.
- Usar `{{ form.as_p }}` quando a view não passa `form` (só `tarefa`), o que quebra a página.

**Exemplo correto** (arquivo: `core/templates/core/confirmar_excluir.html`):

```html
<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <title>Excluir Tarefa</title>
  </head>
  <body>
    <h1>Excluir tarefa?</h1>
    <p>Deseja realmente excluir <strong>{{ tarefa.titulo }}</strong>?</p>

    <form method="post" action="{% url 'core:excluir' tarefa.pk %}">
      {% csrf_token %}
      <button type="submit">Sim, excluir</button>
    </form>

    <p><a href="{% url 'core:lista' %}">Cancelar (voltar à lista)</a></p>
  </body>
</html>
```

Se no seu modelo o campo principal for `descricao` em vez de `titulo`, use `{{ tarefa.descricao }}` no texto de confirmação.

---

## 8. Pontos que precisam aparecer nos slides

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
