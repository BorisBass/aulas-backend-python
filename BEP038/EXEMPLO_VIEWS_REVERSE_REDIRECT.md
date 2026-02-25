# Contexto e exemplo completo: views, reverse() e redirect()

## O que este exemplo quer dizer

O trecho de `core/views.py` mostra **dois padrões importantes** em Django:

1. **redirect + reverse** — após processar um formulário (POST), em vez de devolver outra página direto, a view **redireciona** o usuário para outra URL (ex.: lista de tarefas). Usar `reverse('core:lista')` evita escrever a URL à mão: o Django monta a URL a partir do nome da rota, então se você mudar o path no `urls.py`, o redirecionamento continua certo.

2. **reverse com args** — na view `detalhar`, precisamos gerar o link “Editar” que aponta para a mesma tarefa (ex.: `/editar/5/`). Em vez de concatenar string (`f'/editar/{id}/'`), usamos `reverse('core:editar', args=[id])`. O Django preenche o `<int:id>` da rota com o valor passado; o template recebe `url_editar` já pronto para usar no `<a href="">`.

Ou seja: **redirect** leva o usuário para outra URL após uma ação; **reverse** gera a URL como string a partir do nome da rota (e de argumentos, se houver), mantendo o projeto consistente e fácil de manter.

---

## Exemplo completo (todos os módulos)

Abaixo está um exemplo mínimo que conecta **models**, **urls**, **views** e **templates**, incluindo o uso de `reverse()` e `redirect()`.

### 1. Model (dados)

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

### 2. URLs do app core

```python
# core/urls.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.lista, name='lista'),  # home = lista ('' mostra a lista)
    path('criar/', views.criar, name='criar'),
    path('detalhar/<int:id>/', views.detalhar, name='detalhar'),
    path('editar/<int:id>/', views.editar, name='editar'),
]
```

---

### 3. URLs do projeto (raiz)

```python
# meu_projeto/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # inclui as URLs do app core com namespace
    path('', include(('core.urls', 'core'), namespace='core')),
]
```

Assim, as URLs ficam: `/`, `/criar/`, `/detalhar/1/`, `/editar/1/`. Neste exemplo a **home é a lista**: a rota `''` mostra a lista de tarefas (não há `home.html` separado).

Aqui aparecem **dois níveis de nome**:

- No `core/urls.py` usamos `app_name = 'core'` e `name='lista'`, `name='criar'`, etc.
- No `meu_projeto/urls.py` usamos `namespace='core'`.

Isso permite usar nomes como **`core:lista`**, **`core:detalhar`** e **`core:editar`** tanto no `reverse()` quanto no `{% url %}` dos templates.

---

### 4. Views (lógica + reverse e redirect)

```python
# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Tarefa

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
```

- **redirect(reverse('core:lista'))**: após criar, manda o usuário para a lista sem hardcodar `/lista/` ou `/`.
- **reverse('core:editar', args=[id])**: gera `/editar/5/` (ou o id da tarefa) para usar no template.

---

### 5. Templates

Os templates ficam em `core/templates/` (sem subpasta com o nome do app). No `render` usamos `'lista.html'`, `'criar.html'`, etc.

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
    <p><a href="{% url 'core:criar' %}">Nova tarefa</a></p>
    <ul>
      {% for t in tarefas %}
      <li>
        <a href="{% url 'core:detalhar' t.id %}">{{ t.descricao }}</a>
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
    <p><a href="{% url 'core:lista' %}">Voltar à lista</a></p>
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
    <!-- url_editar foi gerada na view com reverse('core:editar', args=[id]) -->
    <p><a href="{{ url_editar }}">Editar</a></p>
    <p><a href="{% url 'core:lista' %}">Voltar à lista</a></p>
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
      <input
        type="text"
        name="descricao"
        value="{{ tarefa.descricao }}"
        required
      />
      <button type="submit">Salvar</button>
    </form>
    <p><a href="{% url 'core:detalhar' tarefa.id %}">Ver detalhe</a></p>
    <p><a href="{% url 'core:lista' %}">Voltar à lista</a></p>
  </body>
</html>
```

---

## Resumo para explicar na prática

| Conceito                              | Onde aparece                | Para que serve                                                                        |
| ------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------- |
| **redirect()**                        | View `criar` (e `editar`)   | Enviar o usuário para outra URL após POST (evita reenvio do formulário ao atualizar). |
| **reverse('core:lista')**             | View `criar`                | Obter a URL da lista pelo nome da rota, em vez de escrever `/` ou `/lista/` fixo.     |
| **reverse('core:editar', args=[id])** | View `detalhar`             | Gerar a URL de edição (ex.: `/editar/5/`) para passar ao template no `url_editar`.    |
| **{% url 'core:criar' %}**            | Templates                   | No HTML, gerar o link para criar; equivalente ao reverse, no template.                |
| **get_object_or_404**                 | Views `detalhar` e `editar` | Buscar a tarefa por `id` e responder 404 se não existir.                              |

Com esse markdown você tem o **contexto** do exemplo (o que redirect e reverse significam) e um **exemplo completo** com todos os módulos (models, urls, views, templates) para demonstrar na prática.
