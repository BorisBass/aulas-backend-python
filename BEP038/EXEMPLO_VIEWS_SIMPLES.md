# Exemplo simples: sem reverse, redirect com URL fixa e sem namespace

Este arquivo mostra o **mesmo** app de tarefas (lista, criar, detalhar, editar), mas **sem** usar `reverse()`, sem namespace e com URLs escritas à mão nos templates e no `redirect()`. Use ao lado do `EXEMPLO_VIEWS_REVERSE_REDIRECT.md` para comparar com os alunos.

---

## 1. Model (dados)

Igual ao outro exemplo.

```python
# core/models.py
from django.db import models

class Tarefa(models.Model):
    descricao = models.CharField(max_length=200)
    prioridade = models.CharField(max_length=10, default='media')
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.descricao
```

---

## 2. URLs do app core (sem app_name e sem name nas rotas)

```python
# core/urls.py
from django.urls import path
from . import views

# sem app_name
urlpatterns = [
    path('', views.lista),
    path('criar/', views.criar),
    path('detalhar/<int:id>/', views.detalhar),
    path('editar/<int:id>/', views.editar),
]
```

---

## 3. URLs do projeto (raiz) — include simples, sem namespace

```python
# meu_projeto/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

As URLs continuam: `/`, `/criar/`, `/detalhar/1/`, `/editar/1/`.

---

## 4. Views — redirect com URL fixa, link de editar montado na mão

```python
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
```

---

## 5. Templates — links com URL fixa (sem {% url %})

Os templates ficam em `core/templates/`. Todos os links usam o caminho literal da URL.

**Lista** (`core/templates/lista.html`):

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <title>Lista de Tarefas</title>
</head>
<body>
  <h1>Tarefas</h1>
  <p><a href="/criar/">Nova tarefa</a></p>
  <ul>
    {% for t in tarefas %}
    <li>
      <a href="/detalhar/{{ t.id }}/">{{ t.descricao }}</a>
    </li>
    {% empty %}
    <li>Nenhuma tarefa.</li>
    {% endfor %}
  </ul>
</body>
</html>
```

**Criar** (`core/templates/criar.html`):

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <title>Criar Tarefa</title>
</head>
<body>
  <h1>Criar Tarefa</h1>
  <form method="post">
    {% csrf_token %}
    <label>Descrição:</label>
    <input type="text" name="descricao" required />
    <button type="submit">Salvar</button>
  </form>
  <p><a href="/">Voltar à lista</a></p>
</body>
</html>
```

**Detalhar** (`core/templates/detalhar.html`):

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <title>Detalhe</title>
</head>
<body>
  <h1>{{ tarefa.descricao }}</h1>
  <p>Prioridade: {{ tarefa.prioridade }} | Status: {{ tarefa.status }}%</p>
  <p><a href="{{ url_editar }}">Editar</a></p>
  <p><a href="/">Voltar à lista</a></p>
</body>
</html>
```

**Editar** (`core/templates/editar.html`):

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <title>Editar Tarefa</title>
</head>
<body>
  <h1>Editar: {{ tarefa.descricao }}</h1>
  <form method="post">
    {% csrf_token %}
    <label>Descrição:</label>
    <input type="text" name="descricao" value="{{ tarefa.descricao }}" required />
    <button type="submit">Salvar</button>
  </form>
  <p><a href="/detalhar/{{ tarefa.id }}/">Ver detalhe</a></p>
  <p><a href="/">Voltar à lista</a></p>
</body>
</html>
```

---

## Resumo: diferenças em relação ao exemplo com reverse/redirect/namespace

| Onde        | Versão simples (este arquivo)     | Versão com reverse/namespace (outro MD) |
| ----------- | ---------------------------------- | --------------------------------------- |
| **urls app**| Sem `app_name`, sem `name=`        | `app_name = 'core'`, `name='lista'` etc. |
| **urls projeto** | `include('core.urls')`        | `include(('core.urls','core'), namespace='core')` |
| **redirect**| `redirect('/')`, `redirect(f'/detalhar/{id}/')` | `redirect(reverse('core:lista'))`, `reverse('core:detalhar', args=[id])` |
| **view detalhar** | `url_editar = f'/editar/{id}/'` | `url_editar = reverse('core:editar', args=[id])` |
| **templates** | `href="/"`, `href="/criar/"`, `href="/detalhar/{{ t.id }}/"` | `href="{% url 'core:lista' %}"`, `{% url 'core:detalhar' t.id %}` |

Se você mudar uma URL no `urls.py` (por exemplo de `''` para `'inicio/'`), na versão simples é preciso alterar **todos** os lugares que usam essa URL. Na versão com reverse e `{% url %}`, basta alterar em um lugar (o `urls.py`).
