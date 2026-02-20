## Solucoes - BEP035: Introducao ao Django

### Exercicio 1: Projeto e ambiente
```bash
python -m venv .venv
source .venv/bin/activate  # Linux
pip install django
django-admin startproject meu_projeto
cd meu_projeto
python manage.py runserver
```

### Exercicio 2: Estrutura
- `manage.py`: executa comandos do Django.
- `settings.py`: configuracoes do projeto.
- `urls.py`: mapeia URLs para views.
- `wsgi.py`: entrada para servidores WSGI.
- `asgi.py`: entrada para servidores ASGI.

### Exercicio 3: Criar app
```bash
python manage.py startapp core
```
Em `settings.py`:
```python
INSTALLED_APPS = [
    # apps padrao
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # meu app
    "core",
]
```

### Exercicio 4: Primeira view
```python
# core/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Ola Django!")
```

### Exercicio 5: URLs
```python
# core/urls.py
from django.urls import path
from .views import home

urlpatterns = [
    path("", home),
]
```

```python
# meu_projeto/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
]
```

### Exercicio 6: Teste
```bash
python manage.py runserver
```
Acesse `http://127.0.0.1:8000` e verifique a mensagem.
