## Exercícios - BEP040: Autenticação e Autorização

### Exercício 1: Criar usuários
No shell do Django (`python manage.py shell`):
1. Crie um usuário comum com username 'joao' e senha 'senha123'
2. Crie um superusuário com username 'admin' e senha 'admin123'
3. Verifique se os usuários foram criados usando `User.objects.all()`

### Exercício 2: View e template de login
1. Crie uma view `login_view` que:
   - Exibe formulário vazio no GET
   - Processa credenciais no POST usando `authenticate()` e `login()`
   - Redireciona para home após login bem-sucedido
   - Exibe mensagem de erro se credenciais inválidas
2. Crie template `login.html` com campos username e password
3. Configure a URL `/login/` para a view

### Exercício 3: View de logout
1. Crie uma view `logout_view` que:
   - Usa `logout()` para encerrar a sessão
   - Redireciona para a página de login
2. Configure a URL `/logout/` para a view
3. Adicione um link de logout no template (visível apenas para usuários autenticados)

### Exercício 4: Proteger view com @login_required
1. Proteja a view `criar_tarefa` usando o decorator `@login_required`
2. Configure `LOGIN_URL = '/login/'` no `settings.py`
3. Teste acessando a view sem estar logado (deve redirecionar para login)

### Exercício 5: Modelo Perfil
1. Crie um modelo `Perfil` com relação OneToOne com User
2. Adicione campos: `telefone`, `data_nascimento`, `bio`
3. Crie e aplique migrations
4. Crie uma view que exibe o perfil do usuário logado (criando o perfil se não existir)

### Exercício 6: Template com verificação de autenticação
Crie um template que:
- Mostra "Olá, [username]!" e link de logout se o usuário estiver logado
- Mostra link de login se o usuário não estiver logado
- Use `{% if user.is_authenticated %}` para verificar
