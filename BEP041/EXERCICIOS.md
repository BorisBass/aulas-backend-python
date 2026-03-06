# BEP-041 – Testes Automatizados – Exercícios

## Objetivo
Praticar a criação e execução de testes automatizados em aplicações Django.

---

## Exercício 1 – Primeiro teste de modelo

1. Crie um projeto Django simples com um app `core`.
2. Defina um modelo `Tarefa` com os campos:
   - `titulo` (CharField)
   - `concluida` (BooleanField, padrão `False`)
3. Crie um teste em `core/tests.py` que:
   - Cria uma instância de `Tarefa`.
   - Verifica se o valor padrão de `concluida` é `False`.

> Dica: use `from django.test import TestCase`.

---

## Exercício 2 – Testando uma view de lista

1. No mesmo app, crie uma view que lista todas as tarefas.
2. Mapeie a view em `urls.py` com o nome `lista_tarefas`.
3. Crie um teste que:
   - Usa `self.client.get()` para acessar a rota.
   - Verifica se o status code é 200.
   - Garante que o template correto é usado.

---

## Exercício 3 – Testando formulários

1. Crie um `ModelForm` para o modelo `Tarefa`.
2. Escreva um teste que:
   - Envia dados válidos para o formulário e verifica se `form.is_valid()` é `True`.
   - Envia dados inválidos (por exemplo, `titulo=''`) e verifica se `form.is_valid()` é `False`.

---

## Exercício 4 – Introdução ao pytest

1. Instale o `pytest` e o `pytest-django` no seu ambiente.
2. Crie um arquivo `tests_pytest.py` com uma função de teste simples que:
   - Cria uma tarefa.
   - Usa `assert` puro (sem `TestCase`) para verificar um comportamento.

> Dica: configure a variável `DJANGO_SETTINGS_MODULE` no `pytest.ini`.

---

## Exercício 5 – Cobertura de testes

1. Instale a ferramenta de cobertura (`coverage`).
2. Rode a suíte de testes junto com a cobertura.
3. Gere um relatório em HTML e abra no navegador.
4. Identifique pelo menos um trecho de código sem teste e escreva um teste para cobrir esse caso.

