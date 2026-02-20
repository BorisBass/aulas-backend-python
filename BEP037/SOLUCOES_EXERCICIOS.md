## Solucoes - BEP037: Views e Templates

### Exercicio 1: View basica
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Pagina inicial")
```

### Exercicio 2 e 3: Template + contexto
```html
<!-- templates/home.html -->
<h1>Bem-vindo</h1>
<p>Ola, {{ nome }}! Hoje e {{ data }}</p>
```
```python
from django.shortcuts import render
from datetime import date

def home(request):
    contexto = {"nome": "Joao", "data": date.today()}
    return render(request, "home.html", contexto)
```

### Exercicio 4: Lista no template
```html
<!-- templates/lista.html -->
<ul>
{% for t in tarefas %}
  <li>{{ t }}</li>
{% endfor %}
</ul>
```
```python
def lista(request):
    contexto = {"tarefas": ["Estudar", "Ler", "Praticar"]}
    return render(request, "lista.html", contexto)
```

### Exercicio 5: Renderizacao
```python
from django.shortcuts import render

def home(request):
    return render(request, "home.html")
```
