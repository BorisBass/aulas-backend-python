## Soluções - BEP039: Formulários e Validação de Dados

### Solução Exercício 1: Criar Form básico

```python
# core/forms.py
from django import forms

class TarefaForm(forms.Form):
    descricao = forms.CharField(
        max_length=200,
        required=True,
        label='Descrição'
    )
    prioridade = forms.ChoiceField(
        choices=[
            ('alta', 'Alta'),
            ('media', 'Média'),
            ('baixa', 'Baixa')
        ],
        label='Prioridade'
    )
    status = forms.IntegerField(
        min_value=0,
        max_value=100,
        initial=0,
        label='Status (%)'
    )
```

### Solução Exercício 2: View com formulário

```python
# core/views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import TarefaForm
from .models import Tarefa

def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            descricao = form.cleaned_data['descricao']
            prioridade = form.cleaned_data['prioridade']
            status = form.cleaned_data['status']
            Tarefa.objects.create(
                descricao=descricao,
                prioridade=prioridade,
                status=status
            )
            return redirect(reverse('core:lista'))
    else:
        form = TarefaForm()
    
    return render(request, 'criar_tarefa.html', {'form': form})
```

```python
# core/urls.py
from django.urls import path
from .views import criar_tarefa

app_name = 'core'
urlpatterns = [
    path('criar/', criar_tarefa, name='criar'),
]
```

### Solução Exercício 3: Validação customizada

```python
# core/forms.py
from django import forms
from django.core.exceptions import ValidationError

class TarefaForm(forms.Form):
    descricao = forms.CharField(
        max_length=200,
        required=True,
        label='Descrição'
    )
    prioridade = forms.ChoiceField(
        choices=[
            ('alta', 'Alta'),
            ('media', 'Média'),
            ('baixa', 'Baixa')
        ],
        label='Prioridade'
    )
    status = forms.IntegerField(
        min_value=0,
        max_value=100,
        initial=0,
        label='Status (%)'
    )
    
    def clean_descricao(self):
        descricao = self.cleaned_data.get('descricao')
        if descricao and len(descricao.strip()) < 5:
            raise ValidationError('A descrição deve ter pelo menos 5 caracteres.')
        return descricao.strip()
```

### Solução Exercício 4: Template com erros

```html
<!-- core/templates/criar_tarefa.html -->
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Criar Tarefa</title>
</head>
<body>
    <h1>Criar Nova Tarefa</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Salvar</button>
    </form>
    <a href="{% url 'core:lista' %}">Voltar para lista</a>
</body>
</html>
```

### Solução Exercício 5: Validação entre campos

```python
# core/forms.py
from django import forms
from django.core.exceptions import ValidationError

class EventoForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome do Evento')
    data_inicio = forms.DateField(label='Data de Início')
    data_fim = forms.DateField(label='Data de Fim')
    
    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get('data_inicio')
        data_fim = cleaned_data.get('data_fim')
        
        if data_inicio and data_fim:
            if data_fim < data_inicio:
                raise ValidationError({
                    'data_fim': 'A data de fim deve ser posterior à data de início.'
                })
        
        return cleaned_data
```

```python
# core/views.py
def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            # processar evento
            return redirect('core:lista')
    else:
        form = EventoForm()
    
    return render(request, 'criar_evento.html', {'form': form})
```

```html
<!-- core/templates/criar_evento.html -->
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Salvar</button>
</form>
```

### Solução Exercício 6: Template customizado

```html
<!-- core/templates/criar_tarefa.html -->
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Criar Tarefa</title>
    <style>
        .campo {
            margin-bottom: 15px;
        }
        .campo label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .campo input,
        .campo select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .erros {
            color: red;
            font-size: 0.9em;
            margin-top: 5px;
        }
        .erros ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .help-text {
            color: #666;
            font-size: 0.85em;
            margin-top: 3px;
        }
    </style>
</head>
<body>
    <h1>Criar Nova Tarefa</h1>
    <form method="post">
        {% csrf_token %}
        
        {% if form.non_field_errors %}
            <div class="erros">
                {{ form.non_field_errors }}
            </div>
        {% endif %}
        
        {% for field in form %}
            <div class="campo">
                {{ field.label_tag }}
                {{ field }}
                {% if field.errors %}
                    <div class="erros">
                        <ul>
                            {% for error in field.errors %}
                                <li>{{ error }}</li>
                            {% endfor %}
                        </ul>
                    </div>
                {% endif %}
                {% if field.help_text %}
                    <div class="help-text">{{ field.help_text }}</div>
                {% endif %}
            </div>
        {% endfor %}
        
        <button type="submit">Salvar</button>
    </form>
    <a href="{% url 'core:lista' %}">Voltar para lista</a>
</body>
</html>
```
