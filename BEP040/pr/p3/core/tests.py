from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from core.models import Tarefa

User = get_user_model()

#1. Anônimo não acessa a lista
class ListaAuthTest(TestCase):
    def test_anonimo_redireciona_para_login(self):
        resp = self.client.get(reverse("core:criar"))
        self.assertEqual(resp.status_code, 302)
        self.assertIn(reverse("core:lista"), resp["Location"])

# python manage.py test core.tests.ListaAuthTest
# python manage.py test core
#2. Usuário vê apenas as próprias tarefas
class MultiUserListaTest(TestCase):
    def setUp(self):
        self.u1 = User.objects.create_user(username="u1", password="pass123")
        self.u2 = User.objects.create_user(username="u2", password="pass123")

        Tarefa.objects.create(
            titulo="T1", descricao="d1", prioridade="alta", status=10,
            concluida=False, usuario=self.u1
        )
        Tarefa.objects.create(
            titulo="T2", descricao="d2", prioridade="media", status=20,
            concluida=False, usuario=self.u2
        )

    def test_u1_ve_so_tarefas_de_u1(self):
        self.client.login(username="u1", password="pass123")
        resp = self.client.get(reverse("core:lista"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "T1")
        self.assertNotContains(resp, "T2")

#3. Criar tarefa associa automaticamente ao usuário logado
class CriarTarefaTest(TestCase):
    def test_criar_associa_usuario(self):
        u1 = User.objects.create_user(username="u1", password="pass123")
        self.client.login(username="u1", password="pass123")

        resp = self.client.post(reverse("core:criar"), data={
            "titulo": "Nova tarefa",
            "descricao": "Descricao qualquer",
            "prioridade": "alta",
            "status": 50,
            "concluida": False,
        })
        self.assertEqual(resp.status_code, 302)

        tarefa = Tarefa.objects.get(titulo="Nova tarefa")
        self.assertEqual(tarefa.usuario, u1)

#4. Editar/excluir não deixa mexer na tarefa de outro usuário
class ProtecaoEditarExcluirTest(TestCase):
    def setUp(self):
        self.u1 = User.objects.create_user(username="u1", password="pass123")
        self.u2 = User.objects.create_user(username="u2", password="pass123")

        self.t2 = Tarefa.objects.create(
            titulo="T2", descricao="d2", prioridade="media", status=20,
            concluida=False, usuario=self.u2
        )

    def test_editar_outro_usuario_404(self):
        self.client.login(username="u1", password="pass123")
        resp = self.client.get(reverse("core:editar", kwargs={"pk": self.t2.pk})) #/tarefas/1/editar/
        self.assertEqual(resp.status_code, 404)

    def test_excluir_outro_usuario_404(self):
        self.client.login(username="u1", password="pass123")
        resp = self.client.post(reverse("core:excluir", kwargs={"pk": self.t2.pk}))
        self.assertEqual(resp.status_code, 404)        

# 5. Staff consegue ver tarefas de todos
class StaffVeTudoTest(TestCase):
    def test_staff_ve_todas(self):
        staff = User.objects.create_user(username="admin", password="pass123", is_staff=True)
        staff.is_staff = True
        staff.save()

        u2 = User.objects.create_user(username="u2", password="pass123")

        Tarefa.objects.create(
            titulo="T1", descricao="d1", prioridade="alta", status=10,
            concluida=False, usuario=staff
        )
        Tarefa.objects.create(
            titulo="T2", descricao="d2", prioridade="media", status=20,
            concluida=False, usuario=u2
        )

        self.client.login(username="admin", password="pass123")
        resp = self.client.get(reverse("core:tarefas_todos"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "T1")
        self.assertContains(resp, "T2")
