## Solucoes - BEP036: Modelos e Migrations

### Exercicio 1: Model Produto
```python
# core/models.py
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
```

### Exercicio 2: Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Exercicio 3: Admin
```python
# core/admin.py
from django.contrib import admin
from .models import Produto

admin.site.register(Produto)
```
```bash
python manage.py createsuperuser
```

### Exercicio 4: Consultas
```python
from core.models import Produto

# criar
Produto.objects.create(nome="Mouse", preco=49.90, estoque=10)

# listar
Produto.objects.all()

# filtrar
Produto.objects.filter(nome="Mouse")

# atualizar
p = Produto.objects.get(id=1)
p.estoque = 20
p.save()

# remover
p.delete()
```
