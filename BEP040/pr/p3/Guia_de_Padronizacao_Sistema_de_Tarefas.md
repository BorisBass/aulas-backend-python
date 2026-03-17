## Guia de Padronização: Sistema de Tarefas (Django + Bootstrap 5)
Este documento descreve a nova estrutura visual do sistema, focada em sobriedade, responsividade e manutenibilidade através da herança de templates.

---
1. Estrutura de Pastas Recomendada
Para centralizar o visual, criamos uma pasta templates na raiz do projeto:

```
Y:.
│   manage.py
│   db.sqlite3
│
├───templates/          # Pasta global para o layout base
│       base.html       # O esqueleto do sistema
│
├───p1/                 # Pasta de configuração do projeto
│       settings.py
│
└───core/               # App do sistema
    └───templates/
        └───core/       # Telas específicas herdando da base
                home.html
                lista.html
                ...
```
---
2. Configuração no settings.py
Para que o Django reconheça a pasta global de templates, adicione o caminho em DIRS:

```Python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Busca na pasta raiz
        'APP_DIRS': True,
        # ...
    },
]
```
---
3. O Template Base (base.html)
Este arquivo contém o CSS do Bootstrap 5 e a barra de navegação. Todas as outras páginas serão inseridas dentro do bloco {% block content %}.

```HTML
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}TaskAdmin{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f4f7f6; color: #333; }
        .navbar { margin-bottom: 30px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .card { border: none; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand fw-bold" href="{% url 'core:home' %}">TaskAdmin</a>
            <div class="navbar-nav ms-auto text-light small">
                Olá, {{ request.user.username }}
            </div>
        </div>
    </nav>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```
---
4. Templates Refatorados (Exemplos)
Home (Dashboard Sóbrio)
A home agora conta com cards dinâmicos que se adaptam se o usuário for administrador.
```HTML
{% extends "base.html" %}
{% block content %}
<div class="text-center mb-5">
    <h1 class="display-5 fw-bold">Bem-vindo, {{ nome }}!</h1>
</div>
<div class="row g-4 justify-content-center">
    <div class="col-md-{% if request.user.is_staff %}6{% else %}8{% endif %}">
        <div class="card h-100 p-4">
            <h3>📝 Minhas Tarefas</h3>
            <p class="text-muted">Gerencie sua lista pessoal de afazeres.</p>
            <a href="{% url 'core:lista' %}" class="btn btn-primary mt-auto">Acessar Lista</a>
        </div>
    </div>
    {% if request.user.is_staff %}
    <div class="col-md-6">
        <div class="card h-100 p-4 border-top border-info border-4">
            <h3>🌐 Painel Admin</h3>
            <p class="text-muted">Visualize as tarefas de todos os usuários.</p>
            <a href="{% url 'core:tarefas_todos' %}" class="btn btn-outline-dark mt-auto">Ver Tudo</a>
        </div>
    </div>
    {% endif %}
</div>
{% endblock %}
```

Confirmação de Exclusão
Um modal de aviso estilizado para evitar erros acidentais.
```HTML
{% extends "base.html" %}
{% block content %}
<div class="card border-danger mx-auto text-center" style="max-width: 500px;">
    <div class="card-body p-5">
        <h2 class="text-danger">Excluir Tarefa?</h2>
        <p>Deseja realmente apagar <strong>{{ tarefa.titulo }}</strong>?</p>
        <form method="post">
            {% csrf_token %}
            <button type="submit" class="btn btn-danger px-4">Sim, excluir</button>
            <a href="{% url 'core:lista' %}" class="btn btn-secondary px-4">Cancelar</a>
        </form>
    </div>
</div>
{% endblock %}
```
Dica para a equipe: Ao criar novas telas, lembrem-se de sempre começar o arquivo com {% extends "base.html" %} e colocar o conteúdo dentro de {% block content %}. Isso garante que o sistema inteiro mude de visual apenas alterando um único arquivo!