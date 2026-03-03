# core/urls.py
from django.urls import path
from . import views

# sem app_name
urlpatterns = [
    path('', views.lista),
    path('criar/', views.criar),
    path('detalhar/<int:id>/', views.detalhar),
    path('editar/<int:id>/', views.editar),
]