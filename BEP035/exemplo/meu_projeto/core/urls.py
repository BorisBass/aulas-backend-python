from django.urls import path
from .views import home, lista

urlpatterns = [
    path("", home),
    path("lista/", lista),
]