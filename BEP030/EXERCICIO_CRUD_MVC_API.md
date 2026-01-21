# Roteiro CRUD utilizando a API do CEP

Objetivo: montar um CRUD em linha de comando seguindo o mesmo MVC das BEPs 23-28 (estrutura igual ao `tarefas_mvc_db`), acrescentando apenas a consulta de CEP via API.

---

## 1) Estrutura final (exemplo)

```
  cep_crud_mvc/
    .venv/
    main.py
    database.py
    models.py
    views.py
    controllers.py
    cep_api.py
    clientes.db
    requirements.txt
```

---

## 2) Criar a pasta do projeto e o venv (PowerShell)

# criar a pasta do projeto

```
mkdir cep_crud_mvc
cd cep_crud_mvc
python -m venv .venv
.venv\Scripts\activate
```

# Instalar dependencias:

```
pip install requests
pip freeze > requirements.txt
```

---

## 3) Banco de dados: `database.py`

import sqlite3

```python
class DatabaseManager:
    def __init__(self, db_name="clientes.db"):
        self.db_name = db_name
        self.connection = None

    def conectar(self):
        if not self.connection:
            self.connection = sqlite3.connect(self.db_name)
            self._criar_tabela()
            print("✅ Banco conectado e tabela criada!")
        return self.connection

    def _criar_tabela(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cep TEXT NOT NULL,
                logradouro TEXT,
                bairro TEXT,
                cidade TEXT,
                uf TEXT,
                numero TEXT,
                complemento TEXT
            )
            """
        )
        self.connection.commit()

    def get_cursor(self):
        if not self.connection:
            self.conectar()
        return self.connection.cursor()

    def fechar(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            print("🔒 Conexao fechada.")
```

---

## 4) Model e Repository: `models.py`

```python
class Cliente:
    def __init__(
        self,
        nome,
        cep,
        logradouro="",
        bairro="",
        cidade="",
        uf="",
        numero="",
        complemento="",
        cliente_id=None,
    ):
        if not nome or not nome.strip():
            raise ValueError("Nome e obrigatorio")
        if not cep or not cep.strip():
            raise ValueError("CEP e obrigatorio")

        self._id = cliente_id
        self._nome = nome.strip()
        self._cep = cep.strip()
        self._logradouro = logradouro
        self._bairro = bairro
        self._cidade = cidade
        self._uf = uf
        self._numero = numero
        self._complemento = complemento

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def cep(self):
        return self._cep

    @property
    def logradouro(self):
        return self._logradouro

    @property
    def bairro(self):
        return self._bairro

    @property
    def cidade(self):
        return self._cidade

    @property
    def uf(self):
        return self._uf

    @property
    def numero(self):
        return self._numero

    @property
    def complemento(self):
        return self._complemento

    def __str__(self):
        return f"{self._id} - {self._nome} ({self._cidade}/{self._uf})"


class ClienteRepository:
    def __init__(self, db_manager):
        self.db = db_manager
        self.db.conectar()

    def criar(self, cliente):
        cursor = self.db.get_cursor()
        cursor.execute(
            """
            INSERT INTO clientes (nome, cep, logradouro, bairro, cidade, uf, numero, complemento)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                cliente.nome,
                cliente.cep,
                cliente.logradouro,
                cliente.bairro,
                cliente.cidade,
                cliente.uf,
                cliente.numero,
                cliente.complemento,
            ),
        )
        self.db.connection.commit()
        return cursor.lastrowid

    def listar_todos(self):
        cursor = self.db.get_cursor()
        cursor.execute(
            """
            SELECT id, nome, cep, logradouro, bairro, cidade, uf, numero, complemento
            FROM clientes
            ORDER BY id
            """
        )
        rows = cursor.fetchall()
        clientes = []
        for row in rows:
            (
                cliente_id,
                nome,
                cep,
                logradouro,
                bairro,
                cidade,
                uf,
                numero,
                complemento,
            ) = row
            clientes.append(
                Cliente(
                    nome=nome,
                    cep=cep,
                    logradouro=logradouro or "",
                    bairro=bairro or "",
                    cidade=cidade or "",
                    uf=uf or "",
                    numero=numero or "",
                    complemento=complemento or "",
                    cliente_id=cliente_id,
                )
            )
        return clientes

    def buscar_por_id(self, cliente_id):
        cursor = self.db.get_cursor()
        cursor.execute(
            """
            SELECT id, nome, cep, logradouro, bairro, cidade, uf, numero, complemento
            FROM clientes
            WHERE id = ?
            """,
            (cliente_id,),
        )
        row = cursor.fetchone()
        if not row:
            return None
        (
            cliente_id,
            nome,
            cep,
            logradouro,
            bairro,
            cidade,
            uf,
            numero,
            complemento,
        ) = row
        return Cliente(
            nome=nome,
            cep=cep,
            logradouro=logradouro or "",
            bairro=bairro or "",
            cidade=cidade or "",
            uf=uf or "",
            numero=numero or "",
            complemento=complemento or "",
            cliente_id=cliente_id,
        )

    def atualizar(self, cliente):
        cursor = self.db.get_cursor()
        cursor.execute(
            """
            UPDATE clientes
            SET nome = ?, cep = ?, logradouro = ?, bairro = ?, cidade = ?, uf = ?,
                numero = ?, complemento = ?
            WHERE id = ?
            """,
            (
                cliente.nome,
                cliente.cep,
                cliente.logradouro,
                cliente.bairro,
                cliente.cidade,
                cliente.uf,
                cliente.numero,
                cliente.complemento,
                cliente.id,
            ),
        )
        self.db.connection.commit()
        return cursor.rowcount > 0

    def remover(self, cliente_id):
        cursor = self.db.get_cursor()
        cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
        self.db.connection.commit()
        return cursor.rowcount > 0
```

---

## 5) Consulta CEP (API): `cep_api.py`

```python
import requests


def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException:
        raise RuntimeError("Erro ao consultar CEP")

    if data.get("erro"):
        raise ValueError("CEP nao encontrado")

    return {
        "logradouro": data.get("logradouro", ""),
        "bairro": data.get("bairro", ""),
        "cidade": data.get("localidade", ""),
        "uf": data.get("uf", ""),
    }
```

---

## 6) View (CLI): `views.py`

```python
class ClienteView:
    def exibir_menu(self):
        print("\n=== CRUD CEP (MVC) ===")
        print("1. Criar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Atualizar cliente")
        print("5. Remover cliente")
        print("0. Sair")

    def solicitar_dados(self):
        nome = input("Nome: ").strip()
        cep = input("CEP (8 digitos): ").strip()
        numero = input("Numero: ").strip()
        complemento = input("Complemento: ").strip()
        return nome, cep, numero, complemento

    def solicitar_id(self):
        try:
            return int(input("ID: ").strip())
        except ValueError:
            return None

    def solicitar_atualizacao(self):
        nome = input("Novo nome (enter p/ manter): ").strip()
        cep = input("Novo CEP (enter p/ manter): ").strip()
        numero = input("Novo numero (enter p/ manter): ").strip()
        complemento = input("Novo complemento (enter p/ manter): ").strip()
        return nome, cep, numero, complemento

    def exibir_cliente(self, cliente):
        print(cliente)

    def exibir_mensagem(self, mensagem):
        print(mensagem)
```

---

## 7) Controller: `controllers.py`

```python
from models import Cliente, ClienteRepository
from views import ClienteView
from cep_api import buscar_cep


class ClienteController:
    def __init__(self, repository, view):
        self.repository = repository
        self.view = view

    def iniciar(self):
        while True:
            self.view.exibir_menu()
            opcao = input("👉 Escolha: ").strip()

            if opcao == "1":
                self.criar_cliente()
            elif opcao == "2":
                self.listar_clientes()
            elif opcao == "3":
                self.buscar_cliente()
            elif opcao == "4":
                self.atualizar_cliente()
            elif opcao == "5":
                self.remover_cliente()
            elif opcao == "0":
                break
            else:
                self.view.exibir_mensagem("Opcao invalida.")

    def criar_cliente(self):
        try:
            nome, cep, numero, complemento = self.view.solicitar_dados()
            endereco = buscar_cep(cep)
            cliente = Cliente(
                nome=nome,
                cep=cep,
                logradouro=endereco["logradouro"],
                bairro=endereco["bairro"],
                cidade=endereco["cidade"],
                uf=endereco["uf"],
                numero=numero,
                complemento=complemento,
            )
            cliente_id = self.repository.criar(cliente)
            self.view.exibir_mensagem(f"Cliente criado! ID: {cliente_id}")
        except ValueError as e:
            self.view.exibir_mensagem(str(e))
        except RuntimeError as e:
            self.view.exibir_mensagem(str(e))

    def listar_clientes(self):
        clientes = self.repository.listar_todos()
        if not clientes:
            self.view.exibir_mensagem("Nenhum cliente cadastrado.")
            return
        for c in clientes:
            self.view.exibir_cliente(c)

    def buscar_cliente(self):
        cliente_id = self.view.solicitar_id()
        if cliente_id is None:
            self.view.exibir_mensagem("ID invalido.")
            return
        cliente = self.repository.buscar_por_id(cliente_id)
        if cliente:
            self.view.exibir_cliente(cliente)
        else:
            self.view.exibir_mensagem("Cliente nao encontrado.")

    def atualizar_cliente(self):
        cliente_id = self.view.solicitar_id()
        if cliente_id is None:
            self.view.exibir_mensagem("ID invalido.")
            return
        cliente = self.repository.buscar_por_id(cliente_id)
        if not cliente:
            self.view.exibir_mensagem("Cliente nao encontrado.")
            return

        nome, cep, numero, complemento = self.view.solicitar_atualizacao()
        if nome:
            cliente._nome = nome
        if numero:
            cliente._numero = numero
        if complemento:
            cliente._complemento = complemento

        if cep:
            try:
                endereco = buscar_cep(cep)
                cliente._cep = cep
                cliente._logradouro = endereco["logradouro"]
                cliente._bairro = endereco["bairro"]
                cliente._cidade = endereco["cidade"]
                cliente._uf = endereco["uf"]
            except Exception as e:
                self.view.exibir_mensagem(str(e))
                return

        ok = self.repository.atualizar(cliente)
        self.view.exibir_mensagem("Atualizado!" if ok else "Falha ao atualizar.")

    def remover_cliente(self):
        cliente_id = self.view.solicitar_id()
        if cliente_id is None:
            self.view.exibir_mensagem("ID invalido.")
            return
        ok = self.repository.remover(cliente_id)
        self.view.exibir_mensagem("Removido!" if ok else "Cliente nao encontrado.")
```

---

## 8) Main: `main.py`

```python
from database import DatabaseManager
from models import ClienteRepository
from views import ClienteView
from controllers import ClienteController


if __name__ == "__main__":
    db_manager = DatabaseManager("clientes.db")
    repository = ClienteRepository(db_manager)
    view = ClienteView()
    controller = ClienteController(repository, view)

    try:
        controller.iniciar()
    finally:
        db_manager.fechar()
```

---

## 9) Executar

```
python main.py
```

---
