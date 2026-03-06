from django.test import TestCase
from django.urls import reverse


class ExemploTests(TestCase):
    def test_home_status_code(self):
        """
        Exemplo de teste simples de view usando TestCase.
        Ajuste o nome da URL de acordo com seu projeto.
        """
        response = self.client.get("/")
        self.assertIn(response.status_code, (200, 302))


"""
Exemplo de testes usando pytest (coloque em outro arquivo se estiver usando pytest):

import pytest
from core.models import Tarefa


@pytest.mark.django_db
def test_criacao_tarefa():
    tarefa = Tarefa.objects.create(titulo="Estudar pytest")
    assert tarefa.id is not None
"""

