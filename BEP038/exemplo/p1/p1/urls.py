# meu_projeto/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # inclui as URLs do app core com namespace
    path('', include(('core.urls', 'core'), namespace='core')),
]