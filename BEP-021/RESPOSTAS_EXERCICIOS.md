# 📚 BEP-021: Respostas dos Exercícios e Desafios

## Composição e Associação entre Objetos

---

## 📋 Exercício 1: Sistema de Conta Bancária

### Enunciado
1. Crie a classe `ContaBancaria` com atributos `numero`, `saldo` e `titular`.
2. Crie a classe `Cliente` com atributos `nome` e `cpf`.
3. Estabeleça uma **associação** entre Cliente e ContaBancaria.
4. Um cliente pode ter várias contas bancárias.
5. Implemente métodos para criar conta, listar contas do cliente e mostrar saldo.

### ✅ Resposta Completa

```python
class Cliente:
    """Classe Cliente - pode ter várias contas"""
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []  # Lista de contas (associação)
    
    def criar_conta(self, numero, saldo_inicial=0):
        """Cria uma nova conta para o cliente"""
        conta = ContaBancaria(numero, saldo_inicial, self)
        self.contas.append(conta)
        return conta
    
    def listar_contas(self):
        """Lista todas as contas do cliente"""
        print(f"\n📋 Contas de {self.nome} (CPF: {self.cpf}):")
        if not self.contas:
            print("  Nenhuma conta cadastrada.")
        else:
            for conta in self.contas:
                print(f"  Conta {conta.numero}: R$ {conta.saldo:.2f}")
    
    def saldo_total(self):
        """Calcula o saldo total de todas as contas"""
        total = sum(conta.saldo for conta in self.contas)
        return total
    
    def __str__(self):
        return f"Cliente: {self.nome} (CPF: {self.cpf})"

class ContaBancaria:
    """Classe ContaBancaria - associada a um Cliente"""
    def __init__(self, numero, saldo_inicial, titular):
        self.numero = numero
        self.saldo = saldo_inicial
        self.titular = titular  # Associação com Cliente
    
    def depositar(self, valor):
        """Deposita um valor na conta"""
        if valor > 0:
            self.saldo += valor
            print(f"✅ Depósito de R$ {valor:.2f} realizado na conta {self.numero}")
            return True
        print("❌ Valor inválido!")
        return False
    
    def sacar(self, valor):
        """Saca um valor da conta"""
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"✅ Saque de R$ {valor:.2f} realizado da conta {self.numero}")
            return True
        print("❌ Saldo insuficiente ou valor inválido!")
        return False
    
    def consultar_saldo(self):
        """Consulta o saldo atual"""
        return self.saldo
    
    def __str__(self):
        return f"Conta {self.numero} - Titular: {self.titular.nome} - Saldo: R$ {self.saldo:.2f}"

# ===== TESTE =====

print("=" * 60)
print("SISTEMA DE CONTA BANCÁRIA - ASSOCIAÇÃO")
print("=" * 60)

# Criar cliente
cliente1 = Cliente("Ana Silva", "123.456.789-00")
print(f"\n✅ {cliente1} criado")

# Cliente cria várias contas (associação)
conta1 = cliente1.criar_conta("001", 1000)
conta2 = cliente1.criar_conta("002", 500)
conta3 = cliente1.criar_conta("003", 2000)

print(f"\n✅ {len(cliente1.contas)} contas criadas para {cliente1.nome}")

# Operações nas contas
conta1.depositar(500)
conta2.sacar(100)
conta3.depositar(1000)

# Listar contas do cliente
cliente1.listar_contas()

# Saldo total
print(f"\n💰 Saldo total: R$ {cliente1.saldo_total():.2f}")

# Criar outro cliente
cliente2 = Cliente("João Santos", "987.654.321-00")
cliente2.criar_conta("004", 3000)
print(f"\n✅ {cliente2}")
cliente2.listar_contas()
```

### 📊 Saída Esperada
```
============================================================
SISTEMA DE CONTA BANCÁRIA - ASSOCIAÇÃO
============================================================

✅ Cliente: Ana Silva (CPF: 123.456.789-00) criado

✅ 3 contas criadas para Ana Silva
✅ Depósito de R$ 500.00 realizado na conta 001
✅ Saque de R$ 100.00 realizado da conta 002
✅ Depósito de R$ 1000.00 realizado na conta 003

📋 Contas de Ana Silva (CPF: 123.456.789-00):
  Conta 001: R$ 1500.00
  Conta 002: R$ 400.00
  Conta 003: R$ 3000.00

💰 Saldo total: R$ 4900.00

✅ Cliente: João Santos (CPF: 987.654.321-00)
📋 Contas de João Santos (CPF: 987.654.321-00):
  Conta 004: R$ 3000.00
```

### 🔑 Conceitos Aplicados
- **Associação**: Cliente e ContaBancaria são independentes
- **Relação 1 para muitos**: Um cliente pode ter várias contas
- **Referência**: ContaBancaria guarda referência ao Cliente
- **Lista**: Cliente mantém lista de suas contas

---

## 📋 Exercício 2: Sistema de Computador

### Enunciado
1. Crie a classe `Processador` com atributos `marca` e `velocidade`.
2. Crie a classe `Memoria` com atributos `capacidade` e `tipo`.
3. Crie a classe `Computador` que possui um Processador e uma Memoria.
4. Use **composição** para relacionar Computador com Processador e Memoria.
5. O processador e a memória devem ser criados dentro do construtor do Computador.

### ✅ Resposta Completa

```python
class Processador:
    """Classe Processador - parte de um Computador"""
    def __init__(self, marca, velocidade):
        self.marca = marca
        self.velocidade = velocidade  # em GHz
    
    def __str__(self):
        return f"Processador {self.marca} {self.velocidade}GHz"

class Memoria:
    """Classe Memoria - parte de um Computador"""
    def __init__(self, capacidade, tipo):
        self.capacidade = capacidade  # em GB
        self.tipo = tipo  # DDR3, DDR4, DDR5, etc.
    
    def __str__(self):
        return f"Memória {self.capacidade}GB {self.tipo}"

class Computador:
    """Classe Computador - usa COMPOSIÇÃO com Processador e Memoria"""
    def __init__(self, marca_pc, modelo, proc_marca, proc_velocidade, 
                 mem_capacidade, mem_tipo):
        self.marca = marca_pc
        self.modelo = modelo
        
        # COMPOSIÇÃO: Processador e Memoria são criados DENTRO do Computador
        # Eles não existem sem o computador!
        self.processador = Processador(proc_marca, proc_velocidade)
        self.memoria = Memoria(mem_capacidade, mem_tipo)
    
    def informacoes(self):
        """Mostra informações completas do computador"""
        print(f"\n💻 Computador: {self.marca} {self.modelo}")
        print(f"   {self.processador}")
        print(f"   {self.memoria}")
    
    def upgrade_memoria(self, nova_capacidade):
        """Atualiza a memória do computador"""
        self.memoria = Memoria(nova_capacidade, self.memoria.tipo)
        print(f"✅ Memória atualizada para {nova_capacidade}GB")
    
    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.processador} - {self.memoria}"

# ===== TESTE =====

print("=" * 60)
print("SISTEMA DE COMPUTADOR - COMPOSIÇÃO")
print("=" * 60)

# Criar computador (processador e memória são criados automaticamente)
pc1 = Computador(
    marca_pc="Dell",
    modelo="Inspiron 15",
    proc_marca="Intel",
    proc_velocidade=2.5,
    mem_capacidade=8,
    mem_tipo="DDR4"
)

pc1.informacoes()

# Criar outro computador
pc2 = Computador(
    marca_pc="HP",
    modelo="Pavilion",
    proc_marca="AMD",
    proc_velocidade=3.2,
    mem_capacidade=16,
    mem_tipo="DDR5"
)

pc2.informacoes()

# Upgrade de memória
pc1.upgrade_memoria(16)
pc1.informacoes()

# Tentar acessar processador e memória diretamente
print(f"\n🔍 Acessando componentes:")
print(f"   Processador: {pc1.processador}")
print(f"   Memória: {pc1.memoria}")
```

### 📊 Saída Esperada
```
============================================================
SISTEMA DE COMPUTADOR - COMPOSIÇÃO
============================================================

💻 Computador: Dell Inspiron 15
   Processador Intel 2.5GHz
   Memória 8GB DDR4

💻 Computador: HP Pavilion
   Processador AMD 3.2GHz
   Memória 16GB DDR5

✅ Memória atualizada para 16GB

💻 Computador: Dell Inspiron 15
   Processador Intel 2.5GHz
   Memória 16GB DDR4

🔍 Acessando componentes:
   Processador: Processador Intel 2.5GHz
   Memória: Memória 16GB DDR4
```

### 🔑 Conceitos Aplicados
- **Composição**: Processador e Memoria são criados DENTRO do Computador
- **Dependência forte**: Processador e Memoria não existem sem o Computador
- **Criação no construtor**: Objetos parte são criados quando o todo é criado
- **Não podem existir separadamente**: Se o computador for destruído, processador e memória também são

---

## 📋 Exercício 3: Sistema de Escola

### Enunciado
1. Crie a classe `Aluno` com atributos `nome` e `matricula`.
2. Crie a classe `Disciplina` com atributos `nome` e `codigo`.
3. Crie a classe `Professor` com atributos `nome` e `especialidade`.
4. Estabeleça **associações**:
   - Aluno pode estar em várias Disciplinas
   - Professor pode lecionar várias Disciplinas
   - Disciplina pode ter vários Alunos e um Professor
5. Implemente métodos para matricular aluno, atribuir professor e listar alunos de uma disciplina.

### ✅ Resposta Completa

```python
class Aluno:
    """Classe Aluno - pode estar em várias disciplinas"""
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.disciplinas = []  # Associação: lista de disciplinas
    
    def matricular(self, disciplina):
        """Matricula o aluno em uma disciplina"""
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
            disciplina.adicionar_aluno(self)
            print(f"✅ {self.nome} matriculado em {disciplina.nome}")
        else:
            print(f"⚠️ {self.nome} já está matriculado em {disciplina.nome}")
    
    def listar_disciplinas(self):
        """Lista todas as disciplinas do aluno"""
        print(f"\n📚 Disciplinas de {self.nome} ({self.matricula}):")
        if not self.disciplinas:
            print("  Nenhuma disciplina matriculada.")
        else:
            for disc in self.disciplinas:
                print(f"  - {disc.nome} ({disc.codigo})")
    
    def __str__(self):
        return f"Aluno: {self.nome} - Matrícula: {self.matricula}"

class Professor:
    """Classe Professor - pode lecionar várias disciplinas"""
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade
        self.disciplinas = []  # Associação: lista de disciplinas
    
    def atribuir_disciplina(self, disciplina):
        """Atribui uma disciplina ao professor"""
        if disciplina.professor is None:
            disciplina.professor = self
            self.disciplinas.append(disciplina)
            print(f"✅ Professor {self.nome} atribuído à disciplina {disciplina.nome}")
        else:
            print(f"⚠️ Disciplina {disciplina.nome} já tem professor!")
    
    def listar_disciplinas(self):
        """Lista todas as disciplinas do professor"""
        print(f"\n📖 Disciplinas lecionadas por {self.nome}:")
        if not self.disciplinas:
            print("  Nenhuma disciplina atribuída.")
        else:
            for disc in self.disciplinas:
                print(f"  - {disc.nome} ({disc.codigo})")
    
    def __str__(self):
        return f"Professor: {self.nome} - Especialidade: {self.especialidade}"

class Disciplina:
    """Classe Disciplina - tem alunos e professor"""
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.alunos = []  # Associação: lista de alunos
        self.professor = None  # Associação: um professor
    
    def adicionar_aluno(self, aluno):
        """Adiciona um aluno à disciplina"""
        if aluno not in self.alunos:
            self.alunos.append(aluno)
    
    def listar_alunos(self):
        """Lista todos os alunos da disciplina"""
        print(f"\n👥 Alunos de {self.nome} ({self.codigo}):")
        if not self.alunos:
            print("  Nenhum aluno matriculado.")
        else:
            for aluno in self.alunos:
                print(f"  - {aluno.nome} ({aluno.matricula})")
    
    def informacoes(self):
        """Mostra informações completas da disciplina"""
        print(f"\n📋 Disciplina: {self.nome} ({self.codigo})")
        if self.professor:
            print(f"   Professor: {self.professor.nome}")
        else:
            print(f"   Professor: Não atribuído")
        print(f"   Alunos matriculados: {len(self.alunos)}")
    
    def __str__(self):
        return f"Disciplina: {self.nome} ({self.codigo})"

# ===== TESTE =====

print("=" * 60)
print("SISTEMA DE ESCOLA - ASSOCIAÇÕES MÚLTIPLAS")
print("=" * 60)

# Criar alunos
aluno1 = Aluno("Ana Silva", "2025A001")
aluno2 = Aluno("João Santos", "2025A002")
aluno3 = Aluno("Maria Costa", "2025A003")

# Criar professor
prof1 = Professor("Dr. Carlos", "Programação")
prof2 = Professor("Dra. Paula", "Matemática")

# Criar disciplinas
disc1 = Disciplina("Python Básico", "BEP-001")
disc2 = Disciplina("Estruturas de Dados", "BEP-002")
disc3 = Disciplina("Cálculo I", "MAT-001")

# Atribuir professores às disciplinas
prof1.atribuir_disciplina(disc1)
prof1.atribuir_disciplina(disc2)
prof2.atribuir_disciplina(disc3)

# Matricular alunos
aluno1.matricular(disc1)
aluno1.matricular(disc2)
aluno2.matricular(disc1)
aluno2.matricular(disc3)
aluno3.matricular(disc2)
aluno3.matricular(disc3)

# Listar informações
disc1.informacoes()
disc1.listar_alunos()

aluno1.listar_disciplinas()
prof1.listar_disciplinas()
```

### 📊 Saída Esperada
```
============================================================
SISTEMA DE ESCOLA - ASSOCIAÇÕES MÚLTIPLAS
============================================================

✅ Professor Dr. Carlos atribuído à disciplina Python Básico
✅ Professor Dr. Carlos atribuído à disciplina Estruturas de Dados
✅ Professor Dra. Paula atribuído à disciplina Cálculo I
✅ Ana Silva matriculado em Python Básico
✅ Ana Silva matriculado em Estruturas de Dados
✅ João Santos matriculado em Python Básico
✅ João Santos matriculado em Cálculo I
✅ Maria Costa matriculado em Estruturas de Dados
✅ Maria Costa matriculado em Cálculo I

📋 Disciplina: Python Básico (BEP-001)
   Professor: Dr. Carlos
   Alunos matriculados: 2

👥 Alunos de Python Básico (BEP-001):
  - Ana Silva (2025A001)
  - João Santos (2025A002)

📚 Disciplinas de Ana Silva (2025A001):
  - Python Básico (BEP-001)
  - Estruturas de Dados (BEP-002)

📖 Disciplinas lecionadas por Dr. Carlos:
  - Python Básico (BEP-001)
  - Estruturas de Dados (BEP-002)
```

### 🔑 Conceitos Aplicados
- **Associação 1 para muitos**: Professor → Disciplinas
- **Associação muitos para muitos**: Alunos ↔ Disciplinas
- **Associação bidirecional**: Mantida sincronizada
- **Relações independentes**: Objetos podem existir separadamente

---

## 📋 Exercício 4: Sistema de Restaurante

### Enunciado
1. Crie a classe `Ingrediente` com atributos `nome` e `quantidade`.
2. Crie a classe `Prato` que possui vários Ingredientes (use **composição**).
3. Crie a classe `Cliente` com atributos `nome` e `telefone`.
4. Crie a classe `Pedido` que contém Pratos (use **associação**).
5. Estabeleça **associação** entre Cliente e Pedido.
6. Implemente métodos para calcular total do pedido e listar ingredientes de um prato.

### ✅ Resposta Completa

```python
class Ingrediente:
    """Classe Ingrediente - parte de um Prato (composição)"""
    def __init__(self, nome, quantidade, unidade="un"):
        self.nome = nome
        self.quantidade = quantidade
        self.unidade = unidade
    
    def __str__(self):
        return f"{self.nome}: {self.quantidade} {self.unidade}"

class Prato:
    """Classe Prato - usa COMPOSIÇÃO com Ingredientes"""
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.ingredientes = []  # Lista de ingredientes (composição)
    
    def adicionar_ingrediente(self, nome, quantidade, unidade="un"):
        """Adiciona um ingrediente ao prato"""
        ingrediente = Ingrediente(nome, quantidade, unidade)
        self.ingredientes.append(ingrediente)
    
    def listar_ingredientes(self):
        """Lista todos os ingredientes do prato"""
        print(f"\n🍽️ Ingredientes de {self.nome}:")
        if not self.ingredientes:
            print("  Nenhum ingrediente cadastrado.")
        else:
            for ing in self.ingredientes:
                print(f"  - {ing}")
    
    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"

class Cliente:
    """Classe Cliente - pode fazer vários pedidos"""
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.pedidos = []  # Associação: lista de pedidos
    
    def fazer_pedido(self, pedido):
        """Associa um pedido ao cliente"""
        self.pedidos.append(pedido)
        pedido.cliente = self
    
    def __str__(self):
        return f"Cliente: {self.nome} - Tel: {self.telefone}"

class Pedido:
    """Classe Pedido - usa ASSOCIAÇÃO com Pratos e Cliente"""
    def __init__(self, numero):
        self.numero = numero
        self.pratos = []  # Associação: lista de pratos
        self.cliente = None  # Associação: um cliente
    
    def adicionar_prato(self, prato):
        """Adiciona um prato ao pedido"""
        self.pratos.append(prato)
    
    def calcular_total(self):
        """Calcula o total do pedido"""
        total = sum(prato.preco for prato in self.pratos)
        return total
    
    def listar_pratos(self):
        """Lista todos os pratos do pedido"""
        print(f"\n📋 Pedido #{self.numero}:")
        if self.cliente:
            print(f"   Cliente: {self.cliente.nome}")
        if not self.pratos:
            print("   Nenhum prato no pedido.")
        else:
            for prato in self.pratos:
                print(f"   - {prato}")
            print(f"   💰 Total: R$ {self.calcular_total():.2f}")
    
    def __str__(self):
        return f"Pedido #{self.numero} - Total: R$ {self.calcular_total():.2f}"

# ===== TESTE =====

print("=" * 60)
print("SISTEMA DE RESTAURANTE - COMPOSIÇÃO E ASSOCIAÇÃO")
print("=" * 60)

# Criar pratos (com ingredientes - composição)
prato1 = Prato("Macarronada", 25.00)
prato1.adicionar_ingrediente("Macarrão", 200, "g")
prato1.adicionar_ingrediente("Molho de tomate", 150, "ml")
prato1.adicionar_ingrediente("Queijo", 50, "g")

prato2 = Prato("Salada Caesar", 18.00)
prato2.adicionar_ingrediente("Alface", 100, "g")
prato2.adicionar_ingrediente("Frango grelhado", 150, "g")
prato2.adicionar_ingrediente("Molho caesar", 30, "ml")

prato3 = Prato("Suco de Laranja", 8.00)
prato3.adicionar_ingrediente("Laranja", 3, "un")
prato3.adicionar_ingrediente("Açúcar", 10, "g")

# Listar ingredientes dos pratos
prato1.listar_ingredientes()
prato2.listar_ingredientes()

# Criar cliente
cliente1 = Cliente("Ana Silva", "(71) 99999-9999")
print(f"\n✅ {cliente1}")

# Criar pedido (associação com pratos)
pedido1 = Pedido(1)
pedido1.adicionar_prato(prato1)
pedido1.adicionar_prato(prato3)

# Associar pedido ao cliente
cliente1.fazer_pedido(pedido1)

# Mostrar pedido
pedido1.listar_pratos()

# Criar outro pedido
pedido2 = Pedido(2)
pedido2.adicionar_prato(prato2)
pedido2.adicionar_prato(prato3)
cliente1.fazer_pedido(pedido2)

print(f"\n📊 Total de pedidos de {cliente1.nome}: {len(cliente1.pedidos)}")
for pedido in cliente1.pedidos:
    pedido.listar_pratos()
```

### 📊 Saída Esperada
```
============================================================
SISTEMA DE RESTAURANTE - COMPOSIÇÃO E ASSOCIAÇÃO
============================================================

🍽️ Ingredientes de Macarronada:
  - Macarrão: 200 g
  - Molho de tomate: 150 ml
  - Queijo: 50 g

🍽️ Ingredientes de Salada Caesar:
  - Alface: 100 g
  - Frango grelhado: 150 g
  - Molho caesar: 30 ml

✅ Cliente: Ana Silva - Tel: (71) 99999-9999

📋 Pedido #1:
   Cliente: Ana Silva
   - Macarronada - R$ 25.00
   - Suco de Laranja - R$ 8.00
   💰 Total: R$ 33.00

📊 Total de pedidos de Ana Silva: 2
📋 Pedido #1:
   Cliente: Ana Silva
   - Macarronada - R$ 25.00
   - Suco de Laranja - R$ 8.00
   💰 Total: R$ 33.00

📋 Pedido #2:
   Cliente: Ana Silva
   - Salada Caesar - R$ 18.00
   - Suco de Laranja - R$ 8.00
   💰 Total: R$ 26.00
```

### 🔑 Conceitos Aplicados
- **Composição**: Ingredientes são parte de Prato (criados dentro)
- **Associação**: Pratos são associados a Pedido (podem existir separadamente)
- **Associação**: Cliente e Pedido são independentes
- **Relação 1 para muitos**: Cliente pode ter vários Pedidos

---

## 📋 Exercício 5: Sistema de Hotel

### Enunciado
1. Crie a classe `Cama` com atributos `tipo` e `tamanho`.
2. Crie a classe `Quarto` que possui uma Cama (use **composição**).
3. Crie a classe `Hospede` com atributos `nome` e `documento`.
4. Crie a classe `Reserva` que relaciona Hospede e Quarto (use **associação**).
5. Um hospede pode ter várias reservas, e um quarto pode ter várias reservas (muitos para muitos).
6. Implemente métodos para fazer reserva, cancelar reserva e listar reservas de um hospede.

### ✅ Resposta Completa

```python
class Cama:
    """Classe Cama - parte de um Quarto (composição)"""
    def __init__(self, tipo, tamanho):
        self.tipo = tipo  # Solteiro, Casal, Queen, King
        self.tamanho = tamanho  # em cm
    
    def __str__(self):
        return f"Cama {self.tipo} ({self.tamanho}cm)"

class Quarto:
    """Classe Quarto - usa COMPOSIÇÃO com Cama"""
    def __init__(self, numero, tipo_cama, tamanho_cama):
        self.numero = numero
        self.cama = Cama(tipo_cama, tamanho_cama)  # Composição
        self.reservas = []  # Associação: lista de reservas
    
    def adicionar_reserva(self, reserva):
        """Adiciona uma reserva ao quarto"""
        if reserva not in self.reservas:
            self.reservas.append(reserva)
    
    def listar_reservas(self):
        """Lista todas as reservas do quarto"""
        print(f"\n🏨 Reservas do Quarto {self.numero}:")
        if not self.reservas:
            print("  Nenhuma reserva.")
        else:
            for reserva in self.reservas:
                print(f"  - {reserva}")
    
    def __str__(self):
        return f"Quarto {self.numero} - {self.cama}"

class Hospede:
    """Classe Hospede - pode ter várias reservas"""
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento
        self.reservas = []  # Associação: lista de reservas
    
    def fazer_reserva(self, reserva):
        """Associa uma reserva ao hospede"""
        if reserva not in self.reservas:
            self.reservas.append(reserva)
            reserva.hospede = self
            reserva.quarto.adicionar_reserva(reserva)
    
    def cancelar_reserva(self, reserva):
        """Cancela uma reserva"""
        if reserva in self.reservas:
            self.reservas.remove(reserva)
            if reserva in reserva.quarto.reservas:
                reserva.quarto.reservas.remove(reserva)
            reserva.hospede = None
            print(f"✅ Reserva #{reserva.numero} cancelada")
        else:
            print(f"❌ Reserva não encontrada")
    
    def listar_reservas(self):
        """Lista todas as reservas do hospede"""
        print(f"\n📋 Reservas de {self.nome} ({self.documento}):")
        if not self.reservas:
            print("  Nenhuma reserva.")
        else:
            for reserva in self.reservas:
                print(f"  - {reserva}")
    
    def __str__(self):
        return f"Hóspede: {self.nome} - Doc: {self.documento}"

class Reserva:
    """Classe Reserva - ASSOCIAÇÃO com Hospede e Quarto"""
    contador = 1
    
    def __init__(self, quarto, data_entrada, data_saida):
        self.numero = Reserva.contador
        Reserva.contador += 1
        self.quarto = quarto  # Associação
        self.hospede = None  # Associação
        self.data_entrada = data_entrada
        self.data_saida = data_saida
    
    def informacoes(self):
        """Mostra informações completas da reserva"""
        print(f"\n📋 Reserva #{self.numero}:")
        print(f"   Quarto: {self.quarto.numero} ({self.quarto.cama})")
        if self.hospede:
            print(f"   Hóspede: {self.hospede.nome}")
        print(f"   Entrada: {self.data_entrada}")
        print(f"   Saída: {self.data_saida}")
    
    def __str__(self):
        hospede_nome = self.hospede.nome if self.hospede else "Sem hóspede"
        return f"Reserva #{self.numero} - Quarto {self.quarto.numero} - {hospede_nome}"

# ===== TESTE =====

print("=" * 60)
print("SISTEMA DE HOTEL - COMPOSIÇÃO E ASSOCIAÇÃO")
print("=" * 60)

# Criar quartos (com camas - composição)
quarto1 = Quarto(101, "Casal", 160)
quarto2 = Quarto(102, "Solteiro", 90)
quarto3 = Quarto(201, "Queen", 180)

print(f"✅ {quarto1}")
print(f"✅ {quarto2}")
print(f"✅ {quarto3}")

# Criar hóspedes
hospede1 = Hospede("Ana Silva", "123.456.789-00")
hospede2 = Hospede("João Santos", "987.654.321-00")

print(f"\n✅ {hospede1}")
print(f"✅ {hospede2}")

# Criar reservas
reserva1 = Reserva(quarto1, "2025-01-15", "2025-01-20")
reserva2 = Reserva(quarto2, "2025-01-18", "2025-01-22")
reserva3 = Reserva(quarto1, "2025-02-01", "2025-02-05")

# Associar reservas aos hóspedes
hospede1.fazer_reserva(reserva1)
hospede1.fazer_reserva(reserva3)
hospede2.fazer_reserva(reserva2)

# Listar reservas
hospede1.listar_reservas()
hospede2.listar_reservas()

# Mostrar informações detalhadas
reserva1.informacoes()

# Listar reservas dos quartos
quarto1.listar_reservas()

# Cancelar reserva
hospede1.cancelar_reserva(reserva3)
hospede1.listar_reservas()
```

### 📊 Saída Esperada
```
============================================================
SISTEMA DE HOTEL - COMPOSIÇÃO E ASSOCIAÇÃO
============================================================

✅ Quarto 101 - Cama Casal (160cm)
✅ Quarto 102 - Cama Solteiro (90cm)
✅ Quarto 201 - Cama Queen (180cm)

✅ Hóspede: Ana Silva - Doc: 123.456.789-00
✅ Hóspede: João Santos - Doc: 987.654.321-00

📋 Reservas de Ana Silva (123.456.789-00):
  - Reserva #1 - Quarto 101 - Ana Silva
  - Reserva #3 - Quarto 101 - Ana Silva

📋 Reservas de João Santos (987.654.321-00):
  - Reserva #2 - Quarto 102 - João Santos

📋 Reserva #1:
   Quarto: 101 (Cama Casal (160cm))
   Hóspede: Ana Silva
   Entrada: 2025-01-15
   Saída: 2025-01-20

🏨 Reservas do Quarto 101:
  - Reserva #1 - Quarto 101 - Ana Silva
  - Reserva #3 - Quarto 101 - Ana Silva

✅ Reserva #3 cancelada

📋 Reservas de Ana Silva (123.456.789-00):
  - Reserva #1 - Quarto 101 - Ana Silva
```

### 🔑 Conceitos Aplicados
- **Composição**: Cama é parte de Quarto (criada dentro)
- **Associação muitos para muitos**: Hospede ↔ Quarto (através de Reserva)
- **Relação intermediária**: Reserva conecta Hospede e Quarto
- **Bidirecional**: Mantida sincronizada em ambos os lados

---

## 📋 Exercício 6: Sistema de Rede Social

### Enunciado
1. Crie a classe `Post` com atributos `conteudo` e `data`.
2. Crie a classe `Comentario` que é parte de um Post (use **composição**).
3. Crie a classe `Usuario` com atributos `nome` e `email`.
4. Estabeleça **associações**:
   - Usuario pode criar vários Posts
   - Usuario pode seguir outros Usuarios (muitos para muitos)
   - Post pertence a um Usuario
5. Implemente métodos para criar post, adicionar comentário, seguir usuário e listar posts de um usuário.

### ✅ Resposta Completa

```python
from datetime import datetime

class Comentario:
    """Classe Comentario - parte de um Post (composição)"""
    def __init__(self, autor, texto):
        self.autor = autor
        self.texto = texto
        self.data = datetime.now()
    
    def __str__(self):
        return f"{self.autor}: {self.texto}"

class Post:
    """Classe Post - usa COMPOSIÇÃO com Comentarios e ASSOCIAÇÃO com Usuario"""
    def __init__(self, conteudo, autor):
        self.conteudo = conteudo
        self.autor = autor  # Associação com Usuario
        self.data = datetime.now()
        self.comentarios = []  # Composição: lista de comentários
    
    def adicionar_comentario(self, autor, texto):
        """Adiciona um comentário ao post (composição)"""
        comentario = Comentario(autor, texto)
        self.comentarios.append(comentario)
        print(f"✅ Comentário adicionado por {autor}")
    
    def listar_comentarios(self):
        """Lista todos os comentários do post"""
        print(f"\n💬 Comentários do post:")
        if not self.comentarios:
            print("  Nenhum comentário.")
        else:
            for comentario in self.comentarios:
                print(f"  - {comentario}")
    
    def informacoes(self):
        """Mostra informações completas do post"""
        print(f"\n📝 Post de {self.autor.nome}:")
        print(f"   {self.conteudo}")
        print(f"   Data: {self.data.strftime('%d/%m/%Y %H:%M')}")
        print(f"   Comentários: {len(self.comentarios)}")
        if self.comentarios:
            self.listar_comentarios()
    
    def __str__(self):
        return f"Post de {self.autor.nome}: {self.conteudo[:50]}..."

class Usuario:
    """Classe Usuario - pode criar posts e seguir outros usuários"""
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.posts = []  # Associação: lista de posts
        self.seguindo = []  # Associação: lista de usuários seguidos
        self.seguidores = []  # Associação: lista de seguidores
    
    def criar_post(self, conteudo):
        """Cria um novo post"""
        post = Post(conteudo, self)
        self.posts.append(post)
        print(f"✅ Post criado por {self.nome}")
        return post
    
    def seguir(self, outro_usuario):
        """Segue outro usuário (associação muitos para muitos)"""
        if outro_usuario not in self.seguindo and outro_usuario != self:
            self.seguindo.append(outro_usuario)
            outro_usuario.seguidores.append(self)
            print(f"✅ {self.nome} começou a seguir {outro_usuario.nome}")
        elif outro_usuario == self:
            print(f"❌ Você não pode seguir a si mesmo!")
        else:
            print(f"⚠️ {self.nome} já segue {outro_usuario.nome}")
    
    def deixar_de_seguir(self, outro_usuario):
        """Para de seguir outro usuário"""
        if outro_usuario in self.seguindo:
            self.seguindo.remove(outro_usuario)
            outro_usuario.seguidores.remove(self)
            print(f"✅ {self.nome} deixou de seguir {outro_usuario.nome}")
        else:
            print(f"❌ {self.nome} não segue {outro_usuario.nome}")
    
    def listar_posts(self):
        """Lista todos os posts do usuário"""
        print(f"\n📝 Posts de {self.nome}:")
        if not self.posts:
            print("  Nenhum post.")
        else:
            for post in self.posts:
                print(f"  - {post}")
    
    def listar_seguindo(self):
        """Lista usuários que este usuário segue"""
        print(f"\n👥 {self.nome} está seguindo:")
        if not self.seguindo:
            print("  Ninguém.")
        else:
            for usuario in self.seguindo:
                print(f"  - {usuario.nome}")
    
    def listar_seguidores(self):
        """Lista seguidores deste usuário"""
        print(f"\n👥 Seguidores de {self.nome}:")
        if not self.seguidores:
            print("  Nenhum seguidor.")
        else:
            for usuario in self.seguidores:
                print(f"  - {usuario.nome}")
    
    def estatisticas(self):
        """Mostra estatísticas do usuário"""
        print(f"\n📊 Estatísticas de {self.nome}:")
        print(f"   Posts: {len(self.posts)}")
        print(f"   Seguindo: {len(self.seguindo)}")
        print(f"   Seguidores: {len(self.seguidores)}")
    
    def __str__(self):
        return f"Usuário: {self.nome} ({self.email})"

# ===== TESTE =====

print("=" * 60)
print("SISTEMA DE REDE SOCIAL - COMPOSIÇÃO E ASSOCIAÇÃO")
print("=" * 60)

# Criar usuários
usuario1 = Usuario("Ana Silva", "ana@email.com")
usuario2 = Usuario("João Santos", "joao@email.com")
usuario3 = Usuario("Maria Costa", "maria@email.com")

print(f"✅ {usuario1}")
print(f"✅ {usuario2}")
print(f"✅ {usuario3}")

# Criar posts
post1 = usuario1.criar_post("Aprendendo Python é incrível! 🐍")
post2 = usuario1.criar_post("Hoje fiz meu primeiro projeto completo!")
post3 = usuario2.criar_post("Dica: sempre use versionamento Git")
post4 = usuario3.criar_post("Novo framework lançado!")

# Adicionar comentários aos posts (composição)
post1.adicionar_comentario("João Santos", "Parabéns! Continue assim!")
post1.adicionar_comentario("Maria Costa", "Muito bom! 👏")
post2.adicionar_comentario("João Santos", "Compartilha o código!")

# Mostrar informações dos posts
post1.informacoes()

# Seguir usuários (associação muitos para muitos)
usuario1.seguir(usuario2)
usuario1.seguir(usuario3)
usuario2.seguir(usuario1)
usuario3.seguir(usuario1)

# Listar informações
usuario1.listar_posts()
usuario1.listar_seguindo()
usuario1.listar_seguidores()
usuario1.estatisticas()

# Tentar seguir a si mesmo
usuario1.seguir(usuario1)
```

### 📊 Saída Esperada
```
============================================================
SISTEMA DE REDE SOCIAL - COMPOSIÇÃO E ASSOCIAÇÃO
============================================================

✅ Usuário: Ana Silva (ana@email.com)
✅ Usuário: João Santos (joao@email.com)
✅ Usuário: Maria Costa (maria@email.com)
✅ Post criado por Ana Silva
✅ Post criado por Ana Silva
✅ Post criado por João Santos
✅ Post criado por Maria Costa
✅ Comentário adicionado por João Santos
✅ Comentário adicionado por Maria Costa
✅ Comentário adicionado por João Santos

📝 Post de Ana Silva:
   Aprendendo Python é incrível! 🐍
   Data: 18/11/2025 23:30
   Comentários: 2

💬 Comentários do post:
  - João Santos: Parabéns! Continue assim!
  - Maria Costa: Muito bom! 👏

✅ Ana Silva começou a seguir João Santos
✅ Ana Silva começou a seguir Maria Costa
✅ João Santos começou a seguir Ana Silva
✅ Maria Costa começou a seguir Ana Silva

📝 Posts de Ana Silva:
  - Post de Ana Silva: Aprendendo Python é incrível! 🐍...
  - Post de Ana Silva: Hoje fiz meu primeiro projeto completo!...

👥 Ana Silva está seguindo:
  - João Santos
  - Maria Costa

👥 Seguidores de Ana Silva:
  - João Santos
  - Maria Costa

📊 Estatísticas de Ana Silva:
   Posts: 2
   Seguindo: 2
   Seguidores: 2

❌ Você não pode seguir a si mesmo!
```

### 🔑 Conceitos Aplicados
- **Composição**: Comentarios são parte de Post (criados dentro)
- **Associação 1 para muitos**: Usuario → Posts
- **Associação muitos para muitos**: Usuarios ↔ Usuarios (seguir/seguidores)
- **Bidirecional**: Mantida sincronizada em ambos os lados
- **Relações complexas**: Múltiplas associações no mesmo sistema

---

## 🎓 Exercícios Extras (Desafios Avançados)

### Desafio 1: Sistema de Biblioteca

```python
class Livro:
    """Classe Livro - pode ser emprestado"""
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.emprestado = False
        self.emprestimos = []  # Associação
    
    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class Emprestimo:
    """Classe Emprestimo - associação entre Usuario e Livro"""
    def __init__(self, livro, usuario, data_emprestimo, data_devolucao):
        self.livro = livro  # Associação
        self.usuario = usuario  # Associação
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.devolvido = False

class UsuarioBiblioteca:
    """Classe UsuarioBiblioteca - pode emprestar vários livros"""
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.emprestimos = []  # Associação
    
    def emprestar_livro(self, livro, data_emprestimo, data_devolucao):
        """Empresta um livro"""
        if not livro.emprestado:
            emprestimo = Emprestimo(livro, self, data_emprestimo, data_devolucao)
            self.emprestimos.append(emprestimo)
            livro.emprestimos.append(emprestimo)
            livro.emprestado = True
            print(f"✅ {self.nome} emprestou {livro.titulo}")
        else:
            print(f"❌ Livro {livro.titulo} já está emprestado")
```

### Desafio 2: Sistema de E-commerce

```python
class Item:
    """Classe Item - parte de um Pedido (composição)"""
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = produto.preco
    
    def subtotal(self):
        return self.preco_unitario * self.quantidade

class PedidoEcommerce:
    """Classe PedidoEcommerce - usa composição com Items"""
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente  # Associação
        self.itens = []  # Composição: lista de items
    
    def adicionar_item(self, produto, quantidade):
        """Adiciona item ao pedido (composição)"""
        item = Item(produto, quantidade)
        self.itens.append(item)
    
    def total(self):
        return sum(item.subtotal() for item in self.itens)
```

---

## 📝 Dicas para Resolver os Exercícios

### 1. **Identifique o Tipo de Relação**
- Faça a pergunta-chave: "O objeto parte pode existir sem o objeto todo?"
- **SIM** → Use **Associação**
- **NÃO** → Use **Composição**

### 2. **Implemente Composição**
- Crie o objeto parte DENTRO do construtor do objeto todo
- O objeto parte não existe antes do objeto todo
- Exemplo: `self.cama = Cama(...)` dentro de `__init__` de Quarto

### 3. **Implemente Associação**
- Use referências ou listas
- Os objetos podem existir independentemente
- Exemplo: `self.contas = []` em Cliente

### 4. **Mantenha Relações Bidirecionais Sincronizadas**
- Quando A se relaciona com B, atualize B também
- Exemplo: Se aluno se matricula em disciplina, adicione aluno à disciplina

### 5. **Crie Métodos para Gerenciar Relações**
- Não acesse listas diretamente
- Crie métodos como `adicionar()`, `remover()`, `listar()`

### 6. **Teste Sempre**
- Crie objetos de cada classe
- Estabeleça relações
- Verifique se tudo funciona corretamente

---

## ✅ Checklist de Aprendizado

Após resolver os exercícios, você deve ser capaz de:

- [ ] Diferenciar composição de associação
- [ ] Implementar composição criando objetos dentro do construtor
- [ ] Implementar associação usando referências e listas
- [ ] Criar relações 1 para muitos
- [ ] Criar relações muitos para muitos
- [ ] Manter relações bidirecionais sincronizadas
- [ ] Identificar quando usar cada tipo de relação
- [ ] Modelar sistemas complexos usando relações

---

## 🔍 Comparação: Composição vs Associação

| Característica | Composição | Associação |
|----------------|------------|------------|
| **Dependência** | Forte | Fraca |
| **Existência** | Parte não existe sem todo | Podem existir separadamente |
| **Criação** | Dentro do construtor | Fora, depois associada |
| **Destruição** | Parte é destruída com todo | Parte continua existindo |
| **Exemplo** | Motor → Carro | Aluno ↔ Curso |
| **Implementação** | `self.parte = Parte(...)` | `self.lista = []` ou `self.ref = obj` |

---

**Bons estudos! 🚀**

