## Soluções - BEP040: Autenticação e Autorização

### Solução Exercício 1: Criar usuários

```python
# No shell: python manage.py shell
from django.contrib.auth.models import User

# Criar usuário comum
user = User.objects.create_user(
    username='joao',
    email='joao@email.com',
    password='senha123'
)

# Criar superusuário
admin = User.objects.create_superuser(
    username='admin',
    email='admin@email.com',
    password='admin123'
)

# Verificar usuários
usuarios = User.objects.all()
for u in usuarios:
    print(f"{u.username} - {u.email}")
```

### Solução Exercício 2: View e template de login

```python
# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('core:home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    
    return render(request, 'login.html')
```

```html
<!-- core/templates/login.html -->
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    
    {% if messages %}
        {% for message in messages %}
            <div style="color: red;">{{ message }}</div>
        {% endfor %}
    {% endif %}
    
    <form method="post">
        {% csrf_token %}
        <div>
            <label>Usuário:</label>
            <input type="text" name="username" required>
        </div>
        <div>
            <label>Senha:</label>
            <input type="password" name="password" required>
        </div>
        <button type="submit">Entrar</button>
    </form>
</body>
</html>
```

```python
# core/urls.py
from django.urls import path
from .views import login_view

app_name = 'core'
urlpatterns = [
    path('login/', login_view, name='login'),
]
```

### Solução Exercício 3: View de logout

```python
# core/views.py
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('core:login')
```

```python
# core/urls.py
from django.urls import path
from .views import login_view, logout_view

app_name = 'core'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
```

```html
<!-- No template (ex: base.html) -->
{% if user.is_authenticated %}
    <a href="{% url 'core:logout' %}">Sair</a>
{% endif %}
```

### Solução Exercício 4: Proteger view com @login_required

```python
# core/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def criar_tarefa(request):
    if request.method == 'POST':
        # ... processar formulário ...
        pass
    return render(request, 'criar_tarefa.html')
```

```python
# meu_projeto/settings.py
LOGIN_URL = '/login/'  # URL para redirecionar usuários não autenticados
LOGIN_REDIRECT_URL = '/'  # URL após login bem-sucedido
LOGOUT_REDIRECT_URL = '/login/'  # URL após logout
```

### Solução Exercício 5: Modelo Perfil

```python
# core/models.py
from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return f"Perfil de {self.user.username}"
```

```bash
# No terminal
python manage.py makemigrations
python manage.py migrate
```

```python
# core/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Perfil

@login_required
def meu_perfil(request):
    perfil, criado = Perfil.objects.get_or_create(user=request.user)
    return render(request, 'perfil.html', {'perfil': perfil})
```

```python
# core/urls.py
from django.urls import path
from .views import meu_perfil

app_name = 'core'
urlpatterns = [
    path('perfil/', meu_perfil, name='perfil'),
]
```

```html
<!-- core/templates/perfil.html -->
<h1>Meu Perfil</h1>
<p>Usuário: {{ perfil.user.username }}</p>
<p>E-mail: {{ perfil.user.email }}</p>
<p>Telefone: {{ perfil.telefone|default:"Não informado" }}</p>
<p>Data de Nascimento: {{ perfil.data_nascimento|default:"Não informado" }}</p>
<p>Bio: {{ perfil.bio|default:"Não informado" }}</p>
```

### Solução Exercício 6: Template com verificação de autenticação

```html
<!-- core/templates/base.html -->
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Meu Site{% endblock %}</title>
</head>
<body>
    <nav>
        {% if user.is_authenticated %}
            <p>Olá, {{ user.username }}!</p>
            <a href="{% url 'core:logout' %}">Sair</a>
        {% else %}
            <a href="{% url 'core:login' %}">Entrar</a>
        {% endif %}
    </nav>
    
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

```html
<!-- core/templates/home.html -->
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
    {% if user.is_authenticated %}
        <h1>Bem-vindo, {{ user.username }}!</h1>
        <p>Você está logado.</p>
    {% else %}
        <h1>Bem-vindo!</h1>
        <p>Por favor, <a href="{% url 'core:login' %}">faça login</a> para continuar.</p>
    {% endif %}
{% endblock %}
```
