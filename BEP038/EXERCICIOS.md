## Exercícios - BEP038: URLs e Rotas no Django

### Exercício 1: Configurar URLs básicas
Crie rotas no app `core` para:
- `/` → view `home`
- `/lista/` → view `lista`
- `/criar/` → view `criar`
- `/detalhar/<int:id>/` → view `detalhar` (recebe id como parâmetro)

### Exercício 2: Criar app produtos
1. Crie um novo app chamado `produtos` usando `python manage.py startapp produtos`
2. Registre o app em `settings.py` (`INSTALLED_APPS`)
3. Crie um arquivo `produtos/urls.py` com rotas:
   - `/` → view `listar_produtos`
   - `/detalhar/<int:id>/` → view `detalhar_produto`
4. Inclua as URLs do app produtos no `meu_projeto/urls.py` com prefixo `produtos/`

### Exercício 3: Configurar namespaces
1. Adicione `app_name = 'core'` no `core/urls.py`
2. Adicione `app_name = 'produtos'` no `produtos/urls.py`
3. Configure namespaces no `meu_projeto/urls.py` usando `include()` com namespace
4. Atualize um template para usar `{% url 'core:lista' %}` e `{% url 'produtos:lista' %}`

### Exercício 4: Usar reverse()
1. Na view `criar` do app `core`, após criar uma tarefa, use `redirect(reverse('core:lista'))` para redirecionar
2. Na view `detalhar`, gere a URL de edição usando `reverse('core:editar', args=[id])` e passe para o template

### Exercício 5: URLs com parâmetros
Crie uma rota `/produtos/categoria/<str:categoria>/` que filtra produtos por categoria.
Use `reverse()` para gerar links para diferentes categorias em um template.
