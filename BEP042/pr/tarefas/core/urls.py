from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('tarefas/', views.lista_tarefas, name='lista'),
    path('tarefas/nova/', views.criar_tarefa, name='criar'),
    path('tarefas/<int:pk>/editar/', views.editar_tarefa, name='editar'),
    path('tarefas/<int:pk>/excluir/', views.excluir_tarefa, name='excluir'),
    path('staff/tarefas/', views.tarefas_todos_usuarios, name='tarefas_todos'),
]