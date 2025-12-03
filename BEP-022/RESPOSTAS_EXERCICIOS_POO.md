# ✅ Respostas dos Exercícios de Programação Orientada a Objetos (POO)

## BEP-017 a BEP-022

Este documento contém as respostas dos exercícios práticos de POO em Python.

---

## 🎯 Respostas - Exercícios Básicos (BEP-017 e BEP-018)

### Exercício 1: Classe Retângulo

```python
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
    
    def __str__(self):
        return f"Retângulo: largura={self.largura}, altura={self.altura}"


# Teste
r1 = Retangulo(5, 3)
print(r1)  # Retângulo: largura=5, altura=3
print(f"Área: {r1.calcular_area()}")  # Área: 15
print(f"Perímetro: {r1.calcular_perimetro()}")  # Perímetro: 16
```

---

### Exercício 2: Classe Livro

```python
class Livro:
    def __init__(self, titulo, autor, ano_publicacao, preco):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.preco = preco
    
    def informacoes(self):
        return (f"Livro: {self.titulo}\n"
                f"Autor: {self.autor}\n"
                f"Ano: {self.ano_publicacao}\n"
                f"Preço: R$ {self.preco:.2f}")
    
    def calcular_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        return self.preco - desconto


# Teste
livro1 = Livro("Python para Iniciantes", "João Silva", 2023, 50.00)
print(livro1.informacoes())
print(f"Preço com 10% de desconto: R$ {livro1.calcular_desconto(10):.2f}")
```

---

### Exercício 3: Classe Conta Bancária (Básica)

```python
class ContaBancaria:
    def __init__(self, numero_conta, titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor de depósito deve ser positivo!")
    
    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
            else:
                print("Saldo insuficiente!")
        else:
            print("Valor de saque deve ser positivo!")
    
    def consultar_saldo(self):
        return self.saldo


# Teste
conta = ContaBancaria("12345", "Maria Santos")
conta.depositar(1000)
conta.sacar(300)
print(f"Saldo: R$ {conta.consultar_saldo():.2f}")  # Saldo: R$ 700.00
```

---

### Exercício 4: Classe Aluno

```python
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
    
    def adicionar_nota(self, nota):
        self.notas.append(nota)
    
    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def situacao(self):
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"


# Teste
aluno = Aluno("Pedro", "2024001")
aluno.adicionar_nota(8.5)
aluno.adicionar_nota(7.0)
aluno.adicionar_nota(9.0)
print(f"Média: {aluno.calcular_media():.2f}")  # Média: 8.17
print(f"Situação: {aluno.situacao()}")  # Situação: Aprovado
```

---

## 🔒 Respostas - Exercícios de Encapsulamento (BEP-019)

### Exercício 5: Conta Bancária com Encapsulamento

```python
class ContaBancaria:
    def __init__(self, numero_conta, titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.__saldo = 0  # Atributo privado
    
    @property
    def saldo(self):
        """Getter para saldo"""
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        """Setter para saldo - não permite saldo negativo"""
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo!")
        self.__saldo = valor
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor  # Usa o setter
        else:
            raise ValueError("Valor de depósito deve ser positivo!")
    
    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor  # Usa o setter
            else:
                raise ValueError("Saldo insuficiente!")
        else:
            raise ValueError("Valor de saque deve ser positivo!")


# Teste
conta = ContaBancaria("12345", "Maria Santos")
conta.depositar(1000)
print(f"Saldo: R$ {conta.saldo:.2f}")  # Saldo: R$ 1000.00
conta.sacar(300)
print(f"Saldo: R$ {conta.saldo:.2f}")  # Saldo: R$ 700.00
```

---

### Exercício 6: Classe Produto com Validação

```python
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = ""
        self.__preco = 0
        self.__quantidade = 0
        # Usa os setters para validar
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        if not valor or not valor.strip():
            raise ValueError("Nome não pode ser vazio!")
        self.__nome = valor
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("Preço deve ser >= 0!")
        self.__preco = valor
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, valor):
        if valor < 0:
            raise ValueError("Quantidade deve ser >= 0!")
        self.__quantidade = valor
    
    def valor_total(self):
        return self.__preco * self.__quantidade


# Teste
produto = Produto("Notebook", 2500.00, 5)
print(f"Produto: {produto.nome}")  # Produto: Notebook
print(f"Valor total: R$ {produto.valor_total():.2f}")  # Valor total: R$ 12500.00
# produto.preco = -100  # ValueError: Preço deve ser >= 0!
```

---

### Exercício 7: Classe Pessoa com Idade

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.__idade = 0
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, valor):
        if valor < 0 or valor > 150:
            raise ValueError("Idade deve estar entre 0 e 150 anos!")
        self.__idade = valor
    
    def eh_maior_idade(self):
        return self.__idade >= 18


# Teste
pessoa = Pessoa("João")
pessoa.idade = 25
print(f"{pessoa.nome} tem {pessoa.idade} anos")  # João tem 25 anos
print(f"É maior de idade? {pessoa.eh_maior_idade()}")  # É maior de idade? True
```

---

## 🔗 Respostas - Exercícios de Herança e Polimorfismo (BEP-020)

### Exercício 8: Hierarquia de Veículos

```python
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def informacoes(self):
        return f"{self.marca} {self.modelo} ({self.ano})"


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas
    
    def informacoes(self):
        return f"{super().informacoes()} - {self.portas} portas"


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    
    def informacoes(self):
        return f"{super().informacoes()} - {self.cilindradas}cc"


# Teste
carro = Carro("Toyota", "Corolla", 2023, 4)
moto = Moto("Honda", "CB600", 2023, 600)
print(carro.informacoes())  # Toyota Corolla (2023) - 4 portas
print(moto.informacoes())   # Honda CB600 (2023) - 600cc
```

---

### Exercício 9: Sistema de Formas Geométricas

```python
class Forma:
    def calcular_area(self):
        return 0


class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return 3.14159 * self.raio ** 2


class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2


def calcular_area_total(formas):
    """Demonstra polimorfismo - funciona com qualquer Forma"""
    total = 0
    for forma in formas:
        total += forma.calcular_area()
    return total


# Teste
formas = [
    Retangulo(5, 3),
    Circulo(4),
    Triangulo(6, 8)
]
for forma in formas:
    print(f"Área: {forma.calcular_area():.2f}")
# Área: 15.00
# Área: 50.27
# Área: 24.00
print(f"Área total: {calcular_area_total(formas):.2f}")  # Área total: 89.27
```

---

### Exercício 10: Sistema de Funcionários

```python
class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base
    
    def calcular_salario(self):
        return self.salario_base


class Gerente(Funcionario):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)
    
    def calcular_salario(self):
        bonus = self.salario_base * 0.20  # 20% de bônus
        return self.salario_base + bonus


class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, vendas):
        super().__init__(nome, salario_base)
        self.vendas = vendas
    
    def calcular_salario(self):
        comissao = self.vendas * 0.1  # 10% de comissão
        return self.salario_base + comissao


# Teste
gerente = Gerente("Ana", 5000)
vendedor = Vendedor("Carlos", 3000, 10000)
print(f"Salário do gerente: R$ {gerente.calcular_salario():.2f}")  # R$ 6000.00
print(f"Salário do vendedor: R$ {vendedor.calcular_salario():.2f}")  # R$ 4000.00
```

---

## 🔄 Respostas - Exercícios de Composição e Associação (BEP-021)

### Exercício 11: Sistema de Biblioteca (Associação)

```python
class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn


class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula


class Emprestimo:
    def __init__(self, aluno, livro, data_emprestimo):
        self.aluno = aluno  # Associação - objeto Aluno
        self.livro = livro  # Associação - objeto Livro
        self.data_emprestimo = data_emprestimo
    
    def informacoes(self):
        return (f"Empréstimo:\n"
                f"Aluno: {self.aluno.nome} (Matrícula: {self.aluno.matricula})\n"
                f"Livro: {self.livro.titulo} - {self.livro.autor}\n"
                f"ISBN: {self.livro.isbn}\n"
                f"Data: {self.data_emprestimo}")


# Teste
livro = Livro("Python Avançado", "Maria Silva", "978-1234567890")
aluno = Aluno("João", "2024001")
emprestimo = Emprestimo(aluno, livro, "2025-01-15")
print(emprestimo.informacoes())
```

---

### Exercício 12: Sistema de Carro e Motor (Composição)

```python
class Motor:
    def __init__(self, potencia, tipo_combustivel):
        self.potencia = potencia
        self.tipo_combustivel = tipo_combustivel
    
    def ligar(self):
        return "Motor ligado"
    
    def desligar(self):
        return "Motor desligado"


class Carro:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor  # Composição - motor pertence ao carro
    
    def ligar_carro(self):
        return self.motor.ligar()


# Teste
motor = Motor(150, "Gasolina")
carro = Carro("Toyota", "Corolla", motor)
print(carro.ligar_carro())  # Motor ligado
```

---

### Exercício 13: Sistema de E-commerce (Múltiplas Relações)

```python
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Pedido:
    def __init__(self, cliente, data):
        self.cliente = cliente  # Associação - objeto Cliente
        self.produtos = []  # Associação - lista de objetos Produto
        self.data = data
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total


# Teste
cliente = Cliente("Maria", "maria@email.com")
produto1 = Produto("Notebook", 2500.00)
produto2 = Produto("Mouse", 50.00)
pedido = Pedido(cliente, "2025-01-15")
pedido.adicionar_produto(produto1)
pedido.adicionar_produto(produto2)
print(f"Total do pedido: R$ {pedido.calcular_total():.2f}")  # R$ 2550.00
```

---

## ⚠️ Respostas - Exercícios de Tratamento de Exceções (BEP-022)

### Exercício 14: Conta Bancária com Exceções

```python
class SaldoInsuficienteError(Exception):
    """Exceção customizada para saldo insuficiente"""
    pass


class ContaBancaria:
    def __init__(self, numero_conta, titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.__saldo = 0
    
    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        try:
            if valor <= 0:
                raise ValueError("Valor de depósito deve ser positivo!")
            self.__saldo += valor
        except ValueError as e:
            print(f"Erro no depósito: {e}")
    
    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor de saque deve ser positivo!")
        if self.__saldo < valor:
            raise SaldoInsuficienteError(f"Saldo insuficiente! Saldo atual: R$ {self.__saldo:.2f}")
        self.__saldo -= valor


# Teste
conta = ContaBancaria("12345", "Maria")
conta.depositar(1000)
try:
    conta.sacar(1500)  # Deve gerar SaldoInsuficienteError
except SaldoInsuficienteError as e:
    print(f"Erro: {e}")  # Erro: Saldo insuficiente! Saldo atual: R$ 1000.00
```

---

### Exercício 15: Validação de Dados com Exceções

```python
class NomeInvalidoError(Exception):
    pass


class EmailInvalidoError(Exception):
    pass


class IdadeInvalidaError(Exception):
    pass


class Usuario:
    def __init__(self, nome, email, idade):
        # Validações
        if not nome or not nome.strip():
            raise NomeInvalidoError("Nome não pode ser vazio!")
        
        if "@" not in email:
            raise EmailInvalidoError("Email deve conter '@'!")
        
        if idade < 0 or idade > 150:
            raise IdadeInvalidaError("Idade deve estar entre 0 e 150 anos!")
        
        self.nome = nome
        self.email = email
        self.idade = idade


# Teste
try:
    usuario = Usuario("", "email@test.com", 25)  # Nome inválido
except NomeInvalidoError as e:
    print(f"Erro: {e}")  # Erro: Nome não pode ser vazio!

try:
    usuario = Usuario("João", "email_sem_arroba", 25)  # Email inválido
except EmailInvalidoError as e:
    print(f"Erro: {e}")  # Erro: Email deve conter '@'!
```

---

### Exercício 16: Sistema de Divisão com Tratamento de Erros

```python
class Calculadora:
    def dividir(self, a, b):
        try:
            resultado = a / b
            return resultado
        except ZeroDivisionError:
            return "Erro: Divisão por zero não permitida!"
        except TypeError:
            return "Erro: Valores devem ser numéricos!"


# Teste
calc = Calculadora()
print(calc.dividir(10, 2))  # 5.0
print(calc.dividir(10, 0))  # Erro: Divisão por zero não permitida!
print(calc.dividir(10, "2"))  # Erro: Valores devem ser numéricos!
```

---

## 🎓 Respostas - Exercícios Integrados

### Exercício 17: Sistema Completo de Biblioteca

```python
# Exceções customizadas
class LivroJaEmprestadoError(Exception):
    pass


class EmprestimosEmAtrasoError(Exception):
    pass


class LivroNaoEncontradoError(Exception):
    pass


# Classe base
class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf


# Herança
class Usuario(Pessoa):
    def __init__(self, nome, cpf, matricula):
        super().__init__(nome, cpf)
        self.__matricula = matricula
        self.__emprestimos = []
    
    @property
    def matricula(self):
        return self.__matricula
    
    def adicionar_emprestimo(self, emprestimo):
        self.__emprestimos.append(emprestimo)
    
    def verificar_atrasos(self):
        # Lógica simplificada - verifica se há empréstimos em atraso
        for emp in self.__emprestimos:
            # Aqui você implementaria a lógica de verificação de data
            pass
        return False


class Bibliotecario(Usuario):
    def __init__(self, nome, cpf, matricula, registro):
        super().__init__(nome, cpf, matricula)
        self.__registro = registro
    
    def emprestar_livro(self, livro, usuario):
        if livro.emprestado:
            raise LivroJaEmprestadoError(f"Livro '{livro.titulo}' já está emprestado!")
        if usuario.verificar_atrasos():
            raise EmprestimosEmAtrasoError("Usuário possui empréstimos em atraso!")
        # Lógica de empréstimo
        livro.emprestado = True


# Encapsulamento
class Livro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__emprestado = False
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def isbn(self):
        return self.__isbn
    
    @property
    def emprestado(self):
        return self.__emprestado
    
    @emprestado.setter
    def emprestado(self, valor):
        self.__emprestado = valor


# Associação
class Emprestimo:
    def __init__(self, usuario, livro, data):
        self.usuario = usuario  # Associação
        self.livro = livro  # Associação
        self.data = data


# Teste
usuario = Usuario("João", "123.456.789-00", "2024001")
bibliotecario = Bibliotecario("Maria", "987.654.321-00", "BIB001", "REG123")
livro = Livro("Python Avançado", "Autor X", "978-1234567890")

try:
    bibliotecario.emprestar_livro(livro, usuario)
    print("Livro emprestado com sucesso!")
except LivroJaEmprestadoError as e:
    print(f"Erro: {e}")
except EmprestimosEmAtrasoError as e:
    print(f"Erro: {e}")
```

---

### Exercício 18: Sistema de Controle de Estoque

```python
# Exceções
class ProdutoSemEstoqueError(Exception):
    pass


class QuantidadeInvalidaError(Exception):
    pass


class FornecedorNaoEncontradoError(Exception):
    pass


# Encapsulamento
class Produto:
    def __init__(self, nome, preco, quantidade_inicial=0):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade_inicial
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    def adicionar_estoque(self, quantidade):
        if quantidade <= 0:
            raise QuantidadeInvalidaError("Quantidade deve ser positiva!")
        self.__quantidade += quantidade
    
    def remover_estoque(self, quantidade):
        if quantidade <= 0:
            raise QuantidadeInvalidaError("Quantidade deve ser positiva!")
        if self.__quantidade < quantidade:
            raise ProdutoSemEstoqueError(f"Estoque insuficiente! Disponível: {self.__quantidade}")
        self.__quantidade -= quantidade


# Associação
class Fornecedor:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj


# Composição
class Estoque:
    def __init__(self):
        self.__produtos = []  # Composição - lista de produtos
    
    def adicionar_produto(self, produto):
        self.__produtos.append(produto)
    
    def buscar_produto(self, nome):
        for produto in self.__produtos:
            if produto.nome == nome:
                return produto
        raise ProdutoSemEstoqueError(f"Produto '{nome}' não encontrado!")
    
    def listar_produtos(self):
        return self.__produtos


# Associação
class Venda:
    def __init__(self, cliente, produtos):
        self.cliente = cliente  # Associação
        self.produtos = produtos  # Associação - lista de produtos
        self.total = self._calcular_total()
    
    def _calcular_total(self):
        total = 0
        for produto, quantidade in self.produtos:
            total += produto.preco * quantidade
        return total


# Teste
estoque = Estoque()
produto1 = Produto("Notebook", 2500.00, 10)
produto2 = Produto("Mouse", 50.00, 20)
estoque.adicionar_produto(produto1)
estoque.adicionar_produto(produto2)

try:
    produto = estoque.buscar_produto("Notebook")
    produto.remover_estoque(5)
    print(f"Estoque atual: {produto.quantidade}")  # 5
except ProdutoSemEstoqueError as e:
    print(f"Erro: {e}")
```

---

### Exercício 19: Sistema de Gerenciamento de Projetos

```python
# Exceções
class ProjetoSemGerenteError(Exception):
    pass


class TarefaSemDesenvolvedorError(Exception):
    pass


class DataInvalidaError(Exception):
    pass


# Classe base com encapsulamento
class Pessoa:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email


# Herança
class Desenvolvedor(Pessoa):
    def __init__(self, nome, email, especialidade):
        super().__init__(nome, email)
        self.especialidade = especialidade


class GerenteProjeto(Pessoa):
    def __init__(self, nome, email, experiencia_anos):
        super().__init__(nome, email)
        self.experiencia_anos = experiencia_anos


# Composição
class Tarefa:
    def __init__(self, titulo, descricao, projeto):
        self.titulo = titulo
        self.descricao = descricao
        self.projeto = projeto  # Composição - tarefa pertence ao projeto
        self.desenvolvedor = None  # Associação
        self.concluida = False
    
    def atribuir_desenvolvedor(self, desenvolvedor):
        if not desenvolvedor:
            raise TarefaSemDesenvolvedorError("Tarefa deve ter um desenvolvedor atribuído!")
        self.desenvolvedor = desenvolvedor


# Associação
class Projeto:
    def __init__(self, nome, gerente):
        if not gerente:
            raise ProjetoSemGerenteError("Projeto deve ter um gerente!")
        self.nome = nome
        self.gerente = gerente  # Associação
        self.desenvolvedores = []  # Associação - lista de desenvolvedores
        self.tarefas = []  # Composição - lista de tarefas
    
    def adicionar_desenvolvedor(self, desenvolvedor):
        self.desenvolvedores.append(desenvolvedor)
    
    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
    
    def listar_tarefas(self):
        return self.tarefas


# Teste
gerente = GerenteProjeto("Ana", "ana@empresa.com", 5)
projeto = Projeto("Sistema Web", gerente)

dev1 = Desenvolvedor("João", "joao@empresa.com", "Backend")
dev2 = Desenvolvedor("Maria", "maria@empresa.com", "Frontend")

projeto.adicionar_desenvolvedor(dev1)
projeto.adicionar_desenvolvedor(dev2)

tarefa1 = Tarefa("API REST", "Criar endpoints", projeto)
tarefa1.atribuir_desenvolvedor(dev1)

projeto.adicionar_tarefa(tarefa1)

print(f"Projeto: {projeto.nome}")
print(f"Gerente: {projeto.gerente.nome}")
print(f"Desenvolvedores: {[d.nome for d in projeto.desenvolvedores]}")
```

---

## 📝 Observações Finais

1. **As soluções apresentadas são exemplos** - existem múltiplas formas de resolver cada exercício
2. **Validações podem ser mais robustas** - adicione mais verificações conforme necessário
3. **Documentação** - adicione docstrings para melhorar a documentação do código
4. **Testes** - crie mais casos de teste para garantir que o código funciona corretamente
5. **Refatoração** - sempre revise o código e procure melhorias

**Bons estudos! 🚀**

