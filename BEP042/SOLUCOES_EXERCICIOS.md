# BEP-042 – Deploy de Aplicações Django – Soluções (Sugestões)

Estas são soluções **sugeridas** para os exercícios. Adapte conforme o contexto do seu projeto.

---

## Exercício 1 – Separando configurações de produção

Exemplo de `settings_producao.py`:

```python
from .settings import *
import os

DEBUG = False

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = ["meu-dominio.com", "meu-ip-publico"]
```

---

## Exercício 2 – Configurando Gunicorn localmente

Instalação:

```bash
pip install gunicorn
```

Execução:

```bash
gunicorn meu_projeto.wsgi:application --bind 0.0.0.0:8000
```

Depois, acesse `http://localhost:8000/` e verifique se a aplicação responde.

---

## Exercício 3 – Arquivo Procfile para Heroku

`Procfile`:

```txt
web: gunicorn meu_projeto.wsgi --log-file -
```

`requirements.txt` (mínimo):

```txt
Django>=4.0,<5.0
gunicorn
psycopg2-binary
```

---

## Exercício 4 – Deploy em plataforma gratuita (exemplo com Render)

Fluxo típico:

1. Subir o projeto para um repositório Git (GitHub, GitLab).
2. Criar um novo serviço web na Render apontando para o repositório.
3. Definir as variáveis de ambiente:
   - `DJANGO_SECRET_KEY`
   - `DJANGO_SETTINGS_MODULE` (se necessário)
   - Credenciais de banco de dados, se for o caso.
4. Definir o comando de start:
   - `gunicorn meu_projeto.wsgi:application`
5. Aguardar o deploy e acessar a URL gerada.

---

## Exercício 5 – Checklist de produção (exemplo)

- [ ] `DEBUG = False`
- [ ] `SECRET_KEY` vindo de variável de ambiente
- [ ] `ALLOWED_HOSTS` configurado corretamente
- [ ] Uso de HTTPS (TLS) habilitado pela plataforma ou servidor
- [ ] Arquivos estáticos coletados (`python manage.py collectstatic`)
- [ ] Logs configurados (console, arquivo ou serviço externo)
- [ ] Banco de dados de produção configurado (PostgreSQL, por exemplo)
- [ ] Backup e/ou exportação de dados planejados
- [ ] Monitoramento básico (acesso a logs de erro e de acesso)

