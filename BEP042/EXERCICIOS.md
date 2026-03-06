# BEP-042 – Deploy de Aplicações Django – Exercícios

## Objetivo
Praticar os passos principais para publicar uma aplicação Django em produção.

---

## Exercício 1 – Separando configurações de produção

1. Crie um arquivo de configurações específicas para produção (por exemplo, `settings_producao.py`).
2. Configure:
   - `DEBUG = False`
   - `ALLOWED_HOSTS` com o domínio ou IP do servidor.
   - Leitura de `SECRET_KEY` a partir de variável de ambiente.

---

## Exercício 2 – Configurando Gunicorn localmente

1. Instale o Gunicorn no seu ambiente virtual.
2. Rode o servidor com:
   - `gunicorn meu_projeto.wsgi:application`
3. Acesse o endereço configurado e verifique se a aplicação responde.

---

## Exercício 3 – Arquivo Procfile para Heroku

1. Crie um arquivo `Procfile` na raiz do projeto.
2. Configure um comando de web process usando Gunicorn.
3. Adicione também um arquivo `requirements.txt` contendo Django e Gunicorn.

---

## Exercício 4 – Deploy em uma plataforma gratuita (simulado)

1. Escolha uma plataforma (Heroku, Render, Railway etc.).
2. Faça o passo a passo (mesmo que apenas simulado/anotado), incluindo:
   - Criação do app/projeto na plataforma.
   - Configuração de variáveis de ambiente.
   - Deploy do código (por exemplo, via Git).
3. Registre por escrito o fluxo que você seguiu.

---

## Exercício 5 – Checklist de produção

Monte um checklist para qualquer projeto Django ir para produção contendo itens como:

- Configurações de segurança.
- Configuração de logs.
- Configuração de arquivos estáticos e mídia.
- Monitoramento básico (logs de erro, alerta de downtime).

