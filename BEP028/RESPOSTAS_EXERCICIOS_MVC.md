# Respostas dos Exercícios - BEP-028: Introdução ao MVC

Este arquivo contém as respostas comentadas para os exercícios propostos no slide 10 da BEP-028.

---

## Exercício 1: Identificar Componentes

### Análise do CRUD v2

**Arquivo:** `BEP-016/crud_sistema_v2/sistema.py`

#### Identificação dos Componentes:

**📦 Model:**
- `models.py` → Classe `Aluno` (dados e validações)
- `repository.py` → Classe `AlunoRepository` (persistência)
- `database.py` → Classe `DatabaseManager` (gerenciamento de conexão)

**🖥️ View:**
- `menu.py` → Classe `Menu` (exibição e coleta de dados)
  - Métodos como `exibir_menu()`, `solicitar_dados_aluno()`, `exibir_mensagem()`

**🎮 Controller:**
- `sistema.py` → Classe `SistemaAlunos` (coordenação)
  - Métodos como `_cadastrar_aluno()`, `_listar_alunos()`, `iniciar()`

#### Responsabilidades:

**Model:**
- ✅ Gerencia dados (classe `Aluno`)
- ✅ Valida dados (properties com setters)
- ✅ Interage com banco (via `AlunoRepository`)

**View:**
- ✅ Exibe menu e informações
- ✅ Coleta entrada do usuário
- ✅ Formata saída

**Controller:**
- ✅ Coordena fluxo da aplicação
- ✅ Chama métodos do Model
- ✅ Usa View para exibição

#### Melhorias para seguir MVC:

1. **Separação mais clara:** O `SistemaAlunos` mistura um pouco de lógica que poderia estar no Controller
2. **View mais isolada:** A View já está bem separada, mas poderia ter mais métodos específicos
3. **Controller dedicado:** Criar um `AlunoController` separado do `SistemaAlunos` seria mais claro

---

## Exercício 2: Sistema de Livros

### Estrutura de Pastas

```
livros_mvc/
├── models/
│   ├── __init__.py
│   └── livro.py
├── views/
│   ├── __init__.py
│   └── livro_view.py
├── controllers/
│   ├── __init__.py
│   └── livro_controller.py
└── main.py
```

### Model: `models/livro.py`

```python
class Livro:
    """Model - Gerencia dados de um livro"""
    
    def __init__(self, titulo, autor, ano, isbn):
        if not titulo or not titulo.strip():
            raise ValueError("Título é obrigatório")
        if not autor or not autor.strip():
            raise ValueError("Autor é obrigatório")
        if ano and (ano < 0 or ano > 2100):
            raise ValueError("Ano inválido")
        if isbn and len(isbn.strip()) < 10:
            raise ValueError("ISBN deve ter pelo menos 10 caracteres")
        
        self._titulo = titulo.strip()
        self._autor = autor.strip()
        self._ano = ano
        self._isbn = isbn.strip() if isbn else None
        self._lido = False
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def autor(self):
        return self._autor
    
    @property
    def ano(self):
        return self._ano
    
    @property
    def isbn(self):
        return self._isbn
    
    @property
    def lido(self):
        return self._lido
    
    def marcar_como_lido(self):
        """Marca livro como lido"""
        self._lido = True
    
    def __str__(self):
        status = "✅ Lido" if self._lido else "⏳ Não lido"
        return f"{status} | {self._titulo} - {self._autor} ({self._ano})"


class LivroRepository:
    """Gerencia persistência dos livros"""
    
    def __init__(self):
        self._livros = []
    
    def criar(self, livro):
        """Adiciona novo livro"""
        self._livros.append(livro)
        return len(self._livros) - 1
    
    def listar_todos(self):
        """Retorna todos os livros"""
        return self._livros.copy()
    
    def buscar_por_titulo(self, titulo):
        """Busca livros por título (parcial)"""
        titulo_lower = titulo.lower()
        return [livro for livro in self._livros 
                if titulo_lower in livro.titulo.lower()]
    
    def buscar_por_indice(self, indice):
        """Busca livro por índice"""
        if 0 <= indice < len(self._livros):
            return self._livros[indice]
        return None
```

### View: `views/livro_view.py`

```python
class LivroView:
    """View - Responsável pela apresentação"""
    
    def exibir_menu(self):
        """Exibe menu principal"""
        print("\n" + "="*50)
        print("📚 SISTEMA DE GERENCIAMENTO DE LIVROS")
        print("="*50)
        print("1. 📝 Cadastrar livro")
        print("2. 📋 Listar todos os livros")
        print("3. 🔍 Buscar livro por título")
        print("4. ✅ Marcar livro como lido")
        print("0. 🚪 Sair")
        print("="*50)
    
    def solicitar_dados_livro(self):
        """Coleta dados para novo livro"""
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        ano = input("Ano de publicação: ").strip()
        isbn = input("ISBN (opcional): ").strip()
        
        ano_int = int(ano) if ano else None
        return titulo, autor, ano_int, isbn
    
    def exibir_livros(self, livros):
        """Exibe lista de livros"""
        if not livros:
            print("📭 Nenhum livro cadastrado!")
            return
        
        print(f"\n📚 LISTA DE LIVROS ({len(livros)} encontrados):")
        print("-" * 60)
        for i, livro in enumerate(livros, 1):
            print(f"  {i}. {livro}")
    
    def solicitar_indice(self):
        """Solicita índice do livro"""
        try:
            indice = int(input("Número do livro: ")) - 1
            return indice
        except ValueError:
            return None
    
    def solicitar_titulo_busca(self):
        """Solicita título para busca"""
        return input("Digite o título para buscar: ").strip()
    
    def exibir_mensagem(self, mensagem, tipo="info"):
        """Exibe mensagens"""
        if tipo == "erro":
            print(f"❌ {mensagem}")
        elif tipo == "sucesso":
            print(f"✅ {mensagem}")
        else:
            print(f"ℹ️ {mensagem}")
```

### Controller: `controllers/livro_controller.py`

```python
from models.livro import Livro, LivroRepository
from views.livro_view import LivroView


class LivroController:
    """Controller - Coordena Model e View"""
    
    def __init__(self):
        self.repository = LivroRepository()
        self.view = LivroView()
    
    def iniciar(self):
        """Inicia o sistema"""
        while True:
            self.view.exibir_menu()
            opcao = input("👉 Escolha uma opção: ").strip()
            
            if opcao == '1':
                self.cadastrar_livro()
            elif opcao == '2':
                self.listar_livros()
            elif opcao == '3':
                self.buscar_livro()
            elif opcao == '4':
                self.marcar_como_lido()
            elif opcao == '0':
                self.view.exibir_mensagem("Até logo!", "sucesso")
                break
            else:
                self.view.exibir_mensagem("Opção inválida!", "erro")
    
    def cadastrar_livro(self):
        """Processa cadastro de livro"""
        try:
            titulo, autor, ano, isbn = self.view.solicitar_dados_livro()
            livro = Livro(titulo, autor, ano, isbn)
            self.repository.criar(livro)
            self.view.exibir_mensagem(f"Livro '{titulo}' cadastrado!", "sucesso")
        except ValueError as e:
            self.view.exibir_mensagem(str(e), "erro")
        except Exception as e:
            self.view.exibir_mensagem(f"Erro: {e}", "erro")
    
    def listar_livros(self):
        """Lista todos os livros"""
        livros = self.repository.listar_todos()
        self.view.exibir_livros(livros)
    
    def buscar_livro(self):
        """Busca livro por título"""
        titulo = self.view.solicitar_titulo_busca()
        livros = self.repository.buscar_por_titulo(titulo)
        self.view.exibir_livros(livros)
    
    def marcar_como_lido(self):
        """Marca livro como lido"""
        livros = self.repository.listar_todos()
        self.view.exibir_livros(livros)
        indice = self.view.solicitar_indice()
        livro = self.repository.buscar_por_indice(indice)
        if livro:
            livro.marcar_como_lido()
            self.view.exibir_mensagem("Livro marcado como lido!", "sucesso")
        else:
            self.view.exibir_mensagem("Livro não encontrado!", "erro")
```

### Main: `main.py`

```python
from controllers.livro_controller import LivroController

if __name__ == "__main__":
    controller = LivroController()
    controller.iniciar()
```

---

## Exercício 3: Refatorar Código Existente

### Código Original (Procedural)

```python
# sistema_procedural.py
alunos = []

def cadastrar():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    alunos.append({"nome": nome, "idade": idade})
    print("Cadastrado!")

def listar():
    for aluno in alunos:
        print(f"{aluno['nome']} - {aluno['idade']}")

while True:
    print("1. Cadastrar 2. Listar 0. Sair")
    op = input("Opção: ")
    if op == '1':
        cadastrar()
    elif op == '2':
        listar()
    elif op == '0':
        break
```

### Refatoração com MVC

#### Model: `models/aluno.py`

```python
class Aluno:
    """Model - Gerencia dados de um aluno"""
    
    def __init__(self, nome, idade):
        if not nome or not nome.strip():
            raise ValueError("Nome é obrigatório")
        if idade < 0 or idade > 150:
            raise ValueError("Idade deve estar entre 0 e 150")
        
        self._nome = nome.strip()
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    def __str__(self):
        return f"{self._nome} - {self._idade} anos"


class AlunoRepository:
    """Gerencia persistência dos alunos"""
    
    def __init__(self):
        self._alunos = []
    
    def criar(self, aluno):
        """Adiciona novo aluno"""
        self._alunos.append(aluno)
    
    def listar_todos(self):
        """Retorna todos os alunos"""
        return self._alunos.copy()
```

#### View: `views/aluno_view.py`

```python
class AlunoView:
    """View - Responsável pela apresentação"""
    
    def exibir_menu(self):
        """Exibe menu principal"""
        print("\n" + "="*40)
        print("🎓 SISTEMA DE ALUNOS")
        print("="*40)
        print("1. Cadastrar")
        print("2. Listar")
        print("0. Sair")
        print("="*40)
    
    def solicitar_dados_aluno(self):
        """Coleta dados do usuário"""
        nome = input("Nome: ").strip()
        idade = input("Idade: ").strip()
        return nome, idade
    
    def exibir_alunos(self, alunos):
        """Exibe lista de alunos"""
        if not alunos:
            print("📭 Nenhum aluno cadastrado!")
            return
        
        print("\n📋 LISTA DE ALUNOS:")
        for i, aluno in enumerate(alunos, 1):
            print(f"  {i}. {aluno}")
    
    def exibir_mensagem(self, mensagem, tipo="info"):
        """Exibe mensagens"""
        if tipo == "erro":
            print(f"❌ {mensagem}")
        elif tipo == "sucesso":
            print(f"✅ {mensagem}")
        else:
            print(f"ℹ️ {mensagem}")
```

#### Controller: `controllers/aluno_controller.py`

```python
from models.aluno import Aluno, AlunoRepository
from views.aluno_view import AlunoView


class AlunoController:
    """Controller - Coordena Model e View"""
    
    def __init__(self):
        self.repository = AlunoRepository()
        self.view = AlunoView()
    
    def iniciar(self):
        """Inicia o sistema"""
        while True:
            self.view.exibir_menu()
            opcao = input("Opção: ").strip()
            
            if opcao == '1':
                self.cadastrar()
            elif opcao == '2':
                self.listar()
            elif opcao == '0':
                break
            else:
                self.view.exibir_mensagem("Opção inválida!", "erro")
    
    def cadastrar(self):
        """Processa cadastro de aluno"""
        try:
            nome, idade_str = self.view.solicitar_dados_aluno()
            idade = int(idade_str)
            aluno = Aluno(nome, idade)
            self.repository.criar(aluno)
            self.view.exibir_mensagem("Cadastrado!", "sucesso")
        except ValueError as e:
            self.view.exibir_mensagem(str(e), "erro")
        except Exception as e:
            self.view.exibir_mensagem(f"Erro: {e}", "erro")
    
    def listar(self):
        """Lista todos os alunos"""
        alunos = self.repository.listar_todos()
        self.view.exibir_alunos(alunos)
```

#### Main: `main.py`

```python
from controllers.aluno_controller import AlunoController

if __name__ == "__main__":
    controller = AlunoController()
    controller.iniciar()
```

---

## Exercício 4: Múltiplas Views

### Model: Usando o `Aluno` do CRUD v2

```python
# models/aluno.py (já existe no CRUD v2)
# Reutilizamos a classe Aluno existente
```

### View Console: `views/aluno_view_console.py`

```python
from models.aluno import Aluno

class AlunoViewConsole:
    """View Console - Interface de texto"""
    
    def exibir_menu(self):
        print("\n" + "="*50)
        print("🎓 SISTEMA DE ALUNOS (Console)")
        print("="*50)
        print("1. Cadastrar 2. Listar 0. Sair")
        print("="*50)
    
    def solicitar_dados(self):
        nome = input("Nome: ").strip()
        idade = input("Idade: ").strip()
        curso = input("Curso: ").strip()
        nota = input("Nota: ").strip()
        return nome, idade, curso, nota
    
    def exibir_aluno(self, aluno):
        print(f"  - {aluno.nome} ({aluno.curso})")
    
    def exibir_lista(self, alunos):
        print(f"\n📋 {len(alunos)} alunos:")
        for aluno in alunos:
            self.exibir_aluno(aluno)
```

### View HTML: `views/aluno_view_html.py`

```python
from models.aluno import Aluno

class AlunoViewHTML:
    """View HTML - Gera HTML simples"""
    
    def exibir_menu(self):
        html = """
        <html>
        <head><title>Sistema de Alunos</title></head>
        <body>
            <h1>🎓 Sistema de Alunos</h1>
            <nav>
                <a href="#cadastrar">Cadastrar</a> |
                <a href="#listar">Listar</a>
            </nav>
        """
        print(html)
    
    def solicitar_dados(self):
        # Em uma aplicação web real, isso viria de um formulário
        # Aqui simulamos retornando dados de exemplo
        return "João Silva", "20", "Python", "8.5"
    
    def exibir_aluno(self, aluno):
        html = f"""
        <div class="aluno">
            <h3>{aluno.nome}</h3>
            <p>Curso: {aluno.curso}</p>
            <p>Idade: {aluno.idade}</p>
            {f'<p>Nota: {aluno.nota}</p>' if aluno.nota else ''}
        </div>
        """
        print(html)
    
    def exibir_lista(self, alunos):
        html = f"<h2>📋 Lista de Alunos ({len(alunos)})</h2>"
        print(html)
        for aluno in alunos:
            self.exibir_aluno(aluno)
        print("</body></html>")
```

### Controller: `controllers/aluno_controller.py`

```python
from models.aluno import Aluno
from repositories.aluno_repository import AlunoRepository

class AlunoController:
    """Controller - Funciona com qualquer View"""
    
    def __init__(self, repository, view):
        self.repository = repository
        self.view = view  # Aceita qualquer View!
    
    def iniciar(self):
        """Inicia o sistema"""
        while True:
            self.view.exibir_menu()
            opcao = input("Opção: ").strip()
            
            if opcao == '1:
                self.cadastrar()
            elif opcao == '2':
                self.listar()
            elif opcao == '0':
                break
    
    def cadastrar(self):
        """Processa cadastro"""
        try:
            nome, idade, curso, nota = self.view.solicitar_dados()
            aluno = Aluno(nome, int(idade) if idade else None, 
                         curso, float(nota) if nota else None)
            self.repository.salvar(aluno)
        except ValueError as e:
            print(f"Erro: {e}")
    
    def listar(self):
        """Lista alunos"""
        alunos = self.repository.listar_todos()
        self.view.exibir_lista(alunos)
```

### Uso: `main.py`

```python
from models.aluno import Aluno
from repositories.aluno_repository import AlunoRepository
from views.aluno_view_console import AlunoViewConsole
from views.aluno_view_html import AlunoViewHTML
from controllers.aluno_controller import AlunoController

# Usando View Console
repository = AlunoRepository()
view_console = AlunoViewConsole()
controller_console = AlunoController(repository, view_console)
# controller_console.iniciar()

# Usando View HTML (mesmo Model e Repository!)
view_html = AlunoViewHTML()
controller_html = AlunoController(repository, view_html)
# controller_html.iniciar()

# Demonstração: mesmo Model, diferentes Views!
print("✅ Mesmo Model 'Aluno' funciona com ambas Views!")
```

---

## Exercício 5: Sistema de Contatos

### Estrutura

```
contatos_mvc/
├── models/
│   ├── __init__.py
│   └── contato.py
├── repositories/
│   ├── __init__.py
│   └── contato_repository.py
├── views/
│   ├── __init__.py
│   └── contato_view.py
├── controllers/
│   ├── __init__.py
│   └── contato_controller.py
└── main.py
```

### Model: `models/contato.py`

```python
import re

class Contato:
    """Model - Gerencia dados de um contato"""
    
    def __init__(self, nome, telefone, email):
        if not nome or not nome.strip():
            raise ValueError("Nome é obrigatório")
        if not telefone or not telefone.strip():
            raise ValueError("Telefone é obrigatório")
        if not self._validar_email(email):
            raise ValueError("Email inválido")
        if not self._validar_telefone(telefone):
            raise ValueError("Telefone inválido")
        
        self._nome = nome.strip()
        self._telefone = telefone.strip()
        self._email = email.strip()
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def telefone(self):
        return self._telefone
    
    @property
    def email(self):
        return self._email
    
    def _validar_email(self, email):
        """Valida formato de email"""
        if not email or not email.strip():
            return False
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email.strip()))
    
    def _validar_telefone(self, telefone):
        """Valida formato de telefone"""
        if not telefone:
            return False
        # Remove caracteres não numéricos
        numeros = re.sub(r'\D', '', telefone)
        # Telefone deve ter entre 10 e 11 dígitos
        return 10 <= len(numeros) <= 11
    
    def __str__(self):
        return f"{self._nome} | {self._telefone} | {self._email}"
    
    def to_dict(self):
        """Converte para dicionário (para JSON)"""
        return {
            "nome": self._nome,
            "telefone": self._telefone,
            "email": self._email
        }
    
    @classmethod
    def from_dict(cls, data):
        """Cria instância a partir de dicionário"""
        return cls(data["nome"], data["telefone"], data["email"])
```

### Repository: `repositories/contato_repository.py`

```python
import json
import os
from models.contato import Contato

class ContatoRepository:
    """Gerencia persistência dos contatos em JSON"""
    
    def __init__(self, arquivo="contatos.json"):
        self.arquivo = arquivo
        self._contatos = []
        self._carregar()
    
    def _carregar(self):
        """Carrega contatos do arquivo JSON"""
        if os.path.exists(self.arquivo):
            try:
                with open(self.arquivo, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                    self._contatos = [Contato.from_dict(c) for c in dados]
            except Exception as e:
                print(f"Erro ao carregar: {e}")
                self._contatos = []
    
    def _salvar(self):
        """Salva contatos no arquivo JSON"""
        try:
            dados = [c.to_dict() for c in self._contatos]
            with open(self.arquivo, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar: {e}")
    
    def criar(self, contato):
        """Adiciona novo contato"""
        self._contatos.append(contato)
        self._salvar()
        return len(self._contatos) - 1
    
    def listar_todos(self):
        """Retorna todos os contatos"""
        return self._contatos.copy()
    
    def buscar_por_nome(self, nome):
        """Busca contatos por nome (parcial)"""
        nome_lower = nome.lower()
        return [c for c in self._contatos 
                if nome_lower in c.nome.lower()]
    
    def buscar_por_indice(self, indice):
        """Busca contato por índice"""
        if 0 <= indice < len(self._contatos):
            return self._contatos[indice]
        return None
    
    def atualizar(self, indice, contato):
        """Atualiza contato"""
        if 0 <= indice < len(self._contatos):
            self._contatos[indice] = contato
            self._salvar()
            return True
        return False
    
    def remover(self, indice):
        """Remove contato"""
        if 0 <= indice < len(self._contatos):
            contato = self._contatos.pop(indice)
            self._salvar()
            return contato
        return None
```

### View: `views/contato_view.py`

```python
class ContatoView:
    """View - Responsável pela apresentação"""
    
    def exibir_menu(self):
        """Exibe menu principal"""
        print("\n" + "="*50)
        print("📞 AGENDA DE CONTATOS")
        print("="*50)
        print("1. 📝 Cadastrar contato")
        print("2. 📋 Listar contatos")
        print("3. 🔍 Buscar contato por nome")
        print("4. ✏️ Atualizar contato")
        print("5. 🗑️ Remover contato")
        print("0. 🚪 Sair")
        print("="*50)
    
    def solicitar_dados_contato(self):
        """Coleta dados para novo contato"""
        nome = input("Nome: ").strip()
        telefone = input("Telefone: ").strip()
        email = input("Email: ").strip()
        return nome, telefone, email
    
    def exibir_contatos(self, contatos):
        """Exibe lista de contatos"""
        if not contatos:
            print("📭 Nenhum contato encontrado!")
            return
        
        print(f"\n📞 LISTA DE CONTATOS ({len(contatos)} encontrados):")
        print("-" * 60)
        for i, contato in enumerate(contatos, 1):
            print(f"  {i}. {contato}")
    
    def solicitar_indice(self):
        """Solicita índice do contato"""
        try:
            indice = int(input("Número do contato: ")) - 1
            return indice
        except ValueError:
            return None
    
    def solicitar_nome_busca(self):
        """Solicita nome para busca"""
        return input("Digite o nome para buscar: ").strip()
    
    def exibir_mensagem(self, mensagem, tipo="info"):
        """Exibe mensagens"""
        if tipo == "erro":
            print(f"❌ {mensagem}")
        elif tipo == "sucesso":
            print(f"✅ {mensagem}")
        else:
            print(f"ℹ️ {mensagem}")
```

### Controller: `controllers/contato_controller.py`

```python
from models.contato import Contato
from repositories.contato_repository import ContatoRepository
from views.contato_view import ContatoView


class ContatoController:
    """Controller - Coordena Model e View"""
    
    def __init__(self):
        self.repository = ContatoRepository()
        self.view = ContatoView()
    
    def iniciar(self):
        """Inicia o sistema"""
        while True:
            self.view.exibir_menu()
            opcao = input("👉 Escolha uma opção: ").strip()
            
            if opcao == '1':
                self.cadastrar_contato()
            elif opcao == '2':
                self.listar_contatos()
            elif opcao == '3':
                self.buscar_contato()
            elif opcao == '4':
                self.atualizar_contato()
            elif opcao == '5':
                self.remover_contato()
            elif opcao == '0':
                self.view.exibir_mensagem("Até logo!", "sucesso")
                break
            else:
                self.view.exibir_mensagem("Opção inválida!", "erro")
    
    def cadastrar_contato(self):
        """Processa cadastro de contato"""
        try:
            nome, telefone, email = self.view.solicitar_dados_contato()
            contato = Contato(nome, telefone, email)
            self.repository.criar(contato)
            self.view.exibir_mensagem(f"Contato '{nome}' cadastrado!", "sucesso")
        except ValueError as e:
            self.view.exibir_mensagem(str(e), "erro")
        except Exception as e:
            self.view.exibir_mensagem(f"Erro: {e}", "erro")
    
    def listar_contatos(self):
        """Lista todos os contatos"""
        contatos = self.repository.listar_todos()
        self.view.exibir_contatos(contatos)
    
    def buscar_contato(self):
        """Busca contato por nome"""
        nome = self.view.solicitar_nome_busca()
        contatos = self.repository.buscar_por_nome(nome)
        self.view.exibir_contatos(contatos)
    
    def atualizar_contato(self):
        """Atualiza contato"""
        contatos = self.repository.listar_todos()
        self.view.exibir_contatos(contatos)
        indice = self.view.solicitar_indice()
        
        if indice is None:
            self.view.exibir_mensagem("Índice inválido!", "erro")
            return
        
        contato_antigo = self.repository.buscar_por_indice(indice)
        if not contato_antigo:
            self.view.exibir_mensagem("Contato não encontrado!", "erro")
            return
        
        try:
            nome, telefone, email = self.view.solicitar_dados_contato()
            novo_contato = Contato(nome, telefone, email)
            if self.repository.atualizar(indice, novo_contato):
                self.view.exibir_mensagem("Contato atualizado!", "sucesso")
            else:
                self.view.exibir_mensagem("Erro ao atualizar!", "erro")
        except ValueError as e:
            self.view.exibir_mensagem(str(e), "erro")
    
    def remover_contato(self):
        """Remove contato"""
        contatos = self.repository.listar_todos()
        self.view.exibir_contatos(contatos)
        indice = self.view.solicitar_indice()
        
        if indice is None:
            self.view.exibir_mensagem("Índice inválido!", "erro")
            return
        
        contato = self.repository.remover(indice)
        if contato:
            self.view.exibir_mensagem(f"Contato '{contato.nome}' removido!", "sucesso")
        else:
            self.view.exibir_mensagem("Contato não encontrado!", "erro")
```

### Main: `main.py`

```python
from controllers.contato_controller import ContatoController

if __name__ == "__main__":
    controller = ContatoController()
    controller.iniciar()
```

---

## Conclusão

Estes exercícios demonstram:

1. ✅ **Identificação de componentes MVC** em código existente
2. ✅ **Criação de sistemas MVC** do zero
3. ✅ **Refatoração** de código procedural para MVC
4. ✅ **Múltiplas Views** para o mesmo Model
5. ✅ **Sistema completo** com persistência e validações

O padrão MVC facilita:
- Manutenção do código
- Testes unitários
- Trabalho em equipe
- Escalabilidade
- Reutilização de componentes

