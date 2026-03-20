# BEP040 / pr / p3 – Sistema de Tarefas Multiusuário com Testes

Este projeto é um exemplo completo de sistema de tarefas multiusuário em Django, usado na BEP040/BEP041 para demonstrar **autenticação**, **autorização** e **testes automatizados**.

---

## 1. Criar e ativar a virtualenv

**O que é**: um ambiente isolado de Python, onde as bibliotecas deste projeto não misturam com as do sistema.

No diretório `BEP040/pr/p3`:

```bash
python -m venv .venv
```

Ativar (Windows / PowerShell):

```bash
.venv\Scripts\Activate.ps1
```

Depois da ativação, o prompt deve mostrar `(.venv)` no início.

---

## 2. Instalar o Django

**O que é**: framework web que vamos usar para criar o sistema.

Com a virtualenv ativa:

```bash
pip install "django>=4,<5"
```

---

## 3. Criar o projeto Django

**O que é**: o “container” principal da aplicação (configurações globais, URLs raiz, WSGI etc.).

Ainda em `BEP040/pr/p3`:

```bash
django-admin startproject p1 .
```

Isso cria:

- `manage.py`
- pasta `p1/` (com `settings.py`, `urls.py`, `wsgi.py` etc.).

---

## 4. Criar o app `core`

**O que é**: módulo da aplicação que concentra o domínio de “tarefas” (models, views, templates, urls).

```bash
python manage.py startapp core
```

Surge a pasta `core/` com `models.py`, `views.py`, etc.

---

## 5. Registrar o app no `settings.py`

**Por quê**: o Django só enxerga o app se ele estiver em `INSTALLED_APPS`.

Em `p1/settings.py`, na lista `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # nosso app de tarefas
]
```

O bloco `TEMPLATES` já deve estar com `APP_DIRS: True` e os context processors padrão.

Verifique o idioma e a time zone, também no `settings.py`

```python

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = "America/Sao_Paulo"

```
---

## 6. Definir o modelo `Tarefa` (multiusuário)

**O que é**: a representação no banco de dados de uma tarefa, incluindo o dono (`usuario`).

Arquivo `core/models.py`:

```python
from django.conf import settings
from django.db import models


class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    prioridade = models.CharField(max_length=20)  # alta, media, baixa
    status = models.IntegerField(default=0)       # 0 a 100
    concluida = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tarefas'
    )

    def __str__(self):
        return self.titulo
```

Registre a model (tabela do banco) no `core/admin.py` para que ela apareça no painel do admin

```python

from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    # campos que aparecem na lista do admin
    list_display = ("id", "titulo", "descricao", "prioridade", "status", "concluida", "criado_em", "usuario")

```

---

## 7. Criar e aplicar migrações

**O que é**: migrações traduzem as definições dos models em tabelas no banco de dados.

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 8. Criar superusuário

**Para quê**: acessar o Django Admin e poder marcar usuários como staff, testar permissões etc.

```bash
python manage.py createsuperuser
```

Responda username, e-mail e senha.

---

## 9. Formulário `TarefaForm` (ModelForm)

**O que é**: uma classe que gera o formulário HTML a partir do modelo `Tarefa`, com widgets e validação.

Arquivo `core/forms.py`:

```python
from django import forms
from django.core.exceptions import ValidationError
from .models import Tarefa


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'prioridade', 'status', 'concluida']
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
            'prioridade': forms.Select(
                choices=[('alta', 'Alta'), ('media', 'Média'), ('baixa', 'Baixa')],
                attrs={'class': 'form-control'}
            ),
            'status': forms.NumberInput(attrs={'min': 0, 'max': 100, 'class': 'form-control'}),
            'concluida': forms.CheckboxInput(),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if titulo and len(titulo.strip()) < 3:
            raise ValidationError('O título deve ter pelo menos 3 caracteres.')
        return titulo.strip() if titulo else titulo
```

---

## 10. Views principais

**O que são**: funções que recebem a requisição HTTP, consultam o banco e devolvem um template com contexto.

Arquivo `core/views.py` (estrutura principal simplificada):

```python
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
```

---

## 11. URLs (roteamento)

**O que é**: mapeia URLs para views.

`core/urls.py`:

```python
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('tarefas/', views.lista_tarefas, name='lista'),
    path('tarefas/nova/', views.criar_tarefa, name='criar'),
    path('tarefas/<int:pk>/editar/', views.editar_tarefa, name='editar'),
    path('tarefas/<int:pk>/excluir/', views.excluir_tarefa, name='excluir'),
    path('staff/tarefas/', views.tarefas_todos_usuarios, name='tarefas_todos'),
]
```

`p1/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'core'), namespace='core')),
]
```

---

## 12. Templates

**O que são**: arquivos HTML (com Django Template Language) que exibem as páginas da aplicação.

Precisamos de 2 pastas `templates`:

1 na raiz do projeto (`templates`): aqui ficará o template `base.html` que é o template básico que será renderizado primeiro e depois todos outros templates `se encaixarão` nele.

E outra no app (`core/templates`): aqui ficarão os templates que completam o base.

Estrutura:

```text
templates/
  base.html

core/
  templates/ 
    login.html
    core/
      home.html
      lista.html
      criar.html
      editar.html
      confirmar_excluir.html
      tarefas_todos.html
```

Cada template corresponde a uma view e usa Bootstrap para layout (no projeto final).


Altere o `settings.py` incluindo a pasta `templates` do projeto para o `base.html`.

Lá deve estar assim:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], # Modifique esta linha
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
e precisa ficar assim:

```python

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # BASE_DIR diretório padrão do projeto. Onde fica o manage.py
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

---

## 13. Testes automatizados (`core/tests.py`)

**O que são**: funções que rodam o sistema “em miniatura” para garantir regras como:

- anônimo não acessa `/tarefas/`
- usuário só vê as próprias tarefas
- criação de tarefa associa `usuario=request.user`
- usuário não edita/exclui tarefa de outro
- staff vê tarefas de todos

Para rodar os testes:

```bash
python manage.py test core
```

---

## 14. Rodar o servidor (teste manual)

Com a venv ativa:

```bash
python manage.py runserver
```

Acessar no navegador:

- `http://127.0.0.1:8000/` → login
- `http://127.0.0.1:8000/home/` → tela de boas-vindas
- `http://127.0.0.1:8000/tarefas/` → tarefas do usuário logado
- `http://127.0.0.1:8000/staff/tarefas/` → tarefas de todos (apenas para staff)

---

## 15. Gerar `requirements.txt` com `pip freeze`

**O que é**: lista de dependências instaladas na virtualenv, usada para reproduzir o ambiente em outra máquina.

Com a venv ativa, na raiz do projeto (`BEP040/pr/p3`):

```bash
pip freeze > requirements.txt
```

Esse arquivo deve ser versionado no Git junto com o projeto.

