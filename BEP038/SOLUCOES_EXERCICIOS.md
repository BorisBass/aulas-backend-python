## Soluções - BEP038: URLs e Rotas no Django

### Solução Exercício 1: Configurar URLs básicas

```python
# core/urls.py
from django.urls import path
from .views import home, lista, criar, detalhar

urlpatterns = [
    path('', home, name='home'),
    path('lista/', lista, name='lista'),
    path('criar/', criar, name='criar'),
    path('detalhar/<int:id>/', detalhar, name='detalhar'),
]
```

```python
# core/views.py
from django.shortcuts import render
from .models import Tarefa

def home(request):
    return render(request, 'home.html')

def lista(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'lista.html', {'tarefas': tarefas})

def criar(request):
    # lógica de criação
    return render(request, 'criar.html')

def detalhar(request, id):
    tarefa = Tarefa.objects.get(id=id)
    return render(request, 'detalhar.html', {'tarefa': tarefa})
```

### Solução Exercício 2: Criar app produtos

```bash
# No terminal
python manage.py startapp produtos
```

```python
# meu_projeto/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'produtos',  # adicionar aqui
]
```

```python
# produtos/urls.py
from django.urls import path
from .views import listar_produtos, detalhar_produto

urlpatterns = [
    path('', listar_produtos, name='listar'),
    path('detalhar/<int:id>/', detalhar_produto, name='detalhar'),
]
```

```python
# meu_projeto/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('produtos/', include('produtos.urls')),  # prefixo produtos/
]
```

### Solução Exercício 3: Configurar namespaces

```python
# core/urls.py
from django.urls import path
from .views import lista, criar

app_name = 'core'  # define namespace

urlpatterns = [
    path('lista/', lista, name='lista'),
    path('criar/', criar, name='criar'),
]
```

```python
# produtos/urls.py
from django.urls import path
from .views import listar_produtos

app_name = 'produtos'  # define namespace

urlpatterns = [
    path('', listar_produtos, name='lista'),
]
```

```python
# meu_projeto/urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('produtos/', include(('produtos.urls', 'produtos'), namespace='produtos')),
]
```

```html
<!-- template.html -->
<a href="{% url 'core:lista' %}">Lista de Tarefas</a>
<a href="{% url 'produtos:lista' %}">Lista de Produtos</a>
```

### Solução Exercício 4: Usar reverse()

```python
# core/views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Tarefa

def criar(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        Tarefa.objects.create(descricao=descricao)
        return redirect(reverse('core:lista'))  # redireciona usando reverse
    return render(request, 'criar.html')

def detalhar(request, id):
    tarefa = Tarefa.objects.get(id=id)
    url_editar = reverse('core:editar', args=[id])  # gera /editar/1/
    return render(request, 'detalhar.html', {
        'tarefa': tarefa,
        'url_editar': url_editar
    })
```

### Solução Exercício 5: URLs com parâmetros

```python
# produtos/urls.py
from django.urls import path
from .views import listar_produtos, produtos_por_categoria

app_name = 'produtos'

urlpatterns = [
    path('', listar_produtos, name='listar'),
    path('categoria/<str:categoria>/', produtos_por_categoria, name='categoria'),
]
```

```python
# produtos/views.py
from django.shortcuts import render
from django.urls import reverse
from .models import Produto

def produtos_por_categoria(request, categoria):
    produtos = Produto.objects.filter(categoria=categoria)
    return render(request, 'produtos_categoria.html', {
        'produtos': produtos,
        'categoria': categoria
    })
```

```html
<!-- produtos_categoria.html -->
<h1>Produtos da categoria: {{ categoria }}</h1>
<ul>
{% for produto in produtos %}
    <li>{{ produto.nome }}</li>
{% endfor %}
</ul>

<!-- Links para outras categorias usando reverse -->
<a href="{% url 'produtos:categoria' categoria='livros' %}">Livros</a>
<a href="{% url 'produtos:categoria' categoria='eletronicos' %}">Eletrônicos</a>
```
