# BEP-041 – Testes Automatizados – Soluções (Sugestões)

Estas são soluções **sugeridas** para os exercícios. Há várias formas corretas de implementar testes.

---

## Exercício 1 – Primeiro teste de modelo

```python
from django.test import TestCase
from core.models import Tarefa


class TarefaModelTest(TestCase):
    def test_concluida_padrao_false(self):
        tarefa = Tarefa.objects.create(titulo="Estudar Django")
        self.assertFalse(tarefa.concluida)
```

---

## Exercício 2 – Testando uma view de lista

```python
from django.test import TestCase
from django.urls import reverse
from core.models import Tarefa


class ListaTarefasViewTest(TestCase):
    def test_view_lista_tarefas_status_template(self):
        Tarefa.objects.create(titulo="Tarefa 1")
        url = reverse("core:lista_tarefas")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/lista_tarefas.html")
        self.assertContains(response, "Tarefa 1")
```

---

## Exercício 3 – Testando formulários

```python
from django.test import TestCase
from core.forms import TarefaForm


class TarefaFormTest(TestCase):
    def test_form_valido(self):
        form = TarefaForm(data={"titulo": "Estudar testes"})
        self.assertTrue(form.is_valid())

    def test_form_invalido_sem_titulo(self):
        form = TarefaForm(data={"titulo": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("titulo", form.errors)
```

---

## Exercício 4 – Introdução ao pytest

Exemplo simples de uso de pytest:

```python
import pytest
from core.models import Tarefa


@pytest.mark.django_db
def test_criacao_tarefa_pytest():
    tarefa = Tarefa.objects.create(titulo="Estudar pytest")
    assert tarefa.id is not None
    assert tarefa.concluida is False
```

Configuração básica em `pytest.ini`:

```ini
[pytest]
DJANGO_SETTINGS_MODULE = meu_projeto.settings
python_files = tests.py test_*.py *_tests.py
```

---

## Exercício 5 – Cobertura de testes

Comandos sugeridos:

```bash
coverage run manage.py test
coverage html
```

Depois, abrir o arquivo `htmlcov/index.html` no navegador e analisar os arquivos com menor cobertura, escrevendo testes adicionais para eles.

