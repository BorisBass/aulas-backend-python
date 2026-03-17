# core/urls.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.login_view, name='login'),  # home = lista ('' mostra a lista)
    path('logout/', views.logout_view, name='logout'),
    path('lista/', views.lista, name='lista'),
    path('criar/', views.criar, name='criar'),
    path('criar_tarefa/', views.criar_tarefa, name='criar_tarefa'),
    path('detalhar/<int:id>/', views.detalhar, name='detalhar'),
    path('editar/<int:id>/', views.editar, name='editar'),
]