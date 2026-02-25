from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('criar/', views.criar, name='criar'),
    path('detalhar/<int:id>/', views.detalhar, name='detalhar'),
    path('editar/<int:id>/', views.editar, name='editar'),
]