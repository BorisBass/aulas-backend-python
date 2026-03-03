from django.urls import path
from .views import home, lista

app_name='core'

urlpatterns = [
    path("", home, name='home'),
    path("lista/", lista, name='lista'),
]