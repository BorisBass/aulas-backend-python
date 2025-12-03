# 📚 Exercícios de Programação Orientada a Objetos (POO)

## BEP-017 a BEP-022

Este documento contém exercícios práticos para fixar os conceitos de Programação Orientada a Objetos em Python, cobrindo os tópicos das aulas BEP-017 a BEP-022.

---

## 📋 Índice

1. [Exercícios Básicos - Classes e Objetos (BEP-017 e BEP-018)](#exercícios-básicos)
2. [Exercícios de Encapsulamento (BEP-019)](#exercícios-de-encapsulamento)
3. [Exercícios de Herança e Polimorfismo (BEP-020)](#exercícios-de-herança-e-polimorfismo)
4. [Exercícios de Composição e Associação (BEP-021)](#exercícios-de-composição-e-associação)
5. [Exercícios de Tratamento de Exceções (BEP-022)](#exercícios-de-tratamento-de-exceções)
6. [Exercícios Integrados (Todos os Conceitos)](#exercícios-integrados)

---

## 🎯 Exercícios Básicos - Classes e Objetos (BEP-017 e BEP-018)

### Exercício 1: Classe Retângulo
Crie uma classe `Retangulo` que:
- Possui atributos `largura` e `altura`
- Possui um método `calcular_area()` que retorna a área do retângulo
- Possui um método `calcular_perimetro()` que retorna o perímetro do retângulo
- Possui um método `__str__()` que retorna uma string formatada: `"Retângulo: largura={largura}, altura={altura}"`

**Teste sua classe:**
```python
r1 = Retangulo(5, 3)
print(r1)
print(f"Área: {r1.calcular_area()}")
print(f"Perímetro: {r1.calcular_perimetro()}")
```

---

### Exercício 2: Classe Livro
Crie uma classe `Livro` que:
- Possui atributos: `titulo`, `autor`, `ano_publicacao`, `preco`
- Possui um método `informacoes()` que retorna uma string com todas as informações do livro
- Possui um método `calcular_desconto(percentual)` que retorna o preço com desconto aplicado

**Teste sua classe:**
```python
livro1 = Livro("Python para Iniciantes", "João Silva", 2023, 50.00)
print(livro1.informacoes())
print(f"Preço com 10% de desconto: R$ {livro1.calcular_desconto(10):.2f}")
```

---

### Exercício 3: Classe Conta Bancária (Básica)
Crie uma classe `ContaBancaria` que:
- Possui atributos: `numero_conta`, `titular`, `saldo` (inicializado com 0)
- Possui um método `depositar(valor)` que adiciona valor ao saldo
- Possui um método `sacar(valor)` que subtrai valor do saldo (não permitir saldo negativo)
- Possui um método `consultar_saldo()` que retorna o saldo atual

**Teste sua classe:**
```python
conta = ContaBancaria("12345", "Maria Santos")
conta.depositar(1000)
conta.sacar(300)
print(f"Saldo: R$ {conta.consultar_saldo():.2f}")
```

---

### Exercício 4: Classe Aluno
Crie uma classe `Aluno` que:
- Possui atributos: `nome`, `matricula`, `notas` (lista de notas)
- Possui um método `adicionar_nota(nota)` que adiciona uma nota à lista
- Possui um método `calcular_media()` que retorna a média das notas
- Possui um método `situacao()` que retorna "Aprovado" se média >= 7, senão "Reprovado"

**Teste sua classe:**
```python
aluno = Aluno("Pedro", "2024001")
aluno.adicionar_nota(8.5)
aluno.adicionar_nota(7.0)
aluno.adicionar_nota(9.0)
print(f"Média: {aluno.calcular_media():.2f}")
print(f"Situação: {aluno.situacao()}")
```

---

## 🔒 Exercícios de Encapsulamento (BEP-019)

### Exercício 5: Conta Bancária com Encapsulamento
Refaça a classe `ContaBancaria` do Exercício 3, mas agora:
- Torne o atributo `saldo` privado (use `__saldo`)
- Crie uma propriedade `saldo` usando `@property` para leitura
- Crie um setter `@saldo.setter` que não permita saldo negativo
- Mantenha os métodos `depositar()` e `sacar()`

**Teste sua classe:**
```python
conta = ContaBancaria("12345", "Maria Santos")
conta.depositar(1000)
print(f"Saldo: R$ {conta.saldo:.2f}")  # Acesso via property
conta.sacar(300)
print(f"Saldo: R$ {conta.saldo:.2f}")
```

---

### Exercício 6: Classe Produto com Validação
Crie uma classe `Produto` que:
- Possui atributos privados: `__nome`, `__preco`, `__quantidade`
- Use `@property` e `@setter` para `nome` (não pode ser vazio)
- Use `@property` e `@setter` para `preco` (deve ser >= 0)
- Use `@property` e `@setter` para `quantidade` (deve ser >= 0)
- Possui um método `valor_total()` que retorna preço × quantidade

**Teste sua classe:**
```python
produto = Produto("Notebook", 2500.00, 5)
print(f"Produto: {produto.nome}")
print(f"Valor total: R$ {produto.valor_total():.2f}")
# Teste de validação:
# produto.preco = -100  # Deve gerar erro
```

---

### Exercício 7: Classe Pessoa com Idade
Crie uma classe `Pessoa` que:
- Possui atributos: `nome` (público) e `__idade` (privado)
- Use `@property` e `@setter` para `idade` que valida:
  - Idade deve ser entre 0 e 150
  - Se inválida, levanta `ValueError` com mensagem apropriada
- Possui um método `eh_maior_idade()` que retorna `True` se idade >= 18

**Teste sua classe:**
```python
pessoa = Pessoa("João")
pessoa.idade = 25
print(f"{pessoa.nome} tem {pessoa.idade} anos")
print(f"É maior de idade? {pessoa.eh_maior_idade()}")
```

---

## 🔗 Exercícios de Herança e Polimorfismo (BEP-020)

### Exercício 8: Hierarquia de Veículos
Crie uma hierarquia de classes:
- Classe base `Veiculo` com atributos: `marca`, `modelo`, `ano`
- Método `informacoes()` que retorna string com marca, modelo e ano
- Classe `Carro` que herda de `Veiculo` e adiciona atributo `portas`
- Classe `Moto` que herda de `Veiculo` e adiciona atributo `cilindradas`
- Ambas sobrescrevem `informacoes()` para incluir seus atributos específicos

**Teste suas classes:**
```python
carro = Carro("Toyota", "Corolla", 2023, 4)
moto = Moto("Honda", "CB600", 2023, 600)
print(carro.informacoes())
print(moto.informacoes())
```

---

### Exercício 9: Sistema de Formas Geométricas
Crie uma hierarquia de classes para formas geométricas:
- Classe abstrata base `Forma` com método `calcular_area()` (retorna 0)
- Classe `Retangulo` que herda de `Forma` e implementa `calcular_area()`
- Classe `Circulo` que herda de `Forma` e implementa `calcular_area()`
- Classe `Triangulo` que herda de `Forma` e implementa `calcular_area()`
- Crie uma função `calcular_area_total(formas)` que recebe uma lista de formas e retorna a soma das áreas (demonstrando polimorfismo)

**Teste suas classes:**
```python
formas = [
    Retangulo(5, 3),
    Circulo(4),
    Triangulo(6, 8)
]
for forma in formas:
    print(f"Área: {forma.calcular_area():.2f}")
print(f"Área total: {calcular_area_total(formas):.2f}")
```

---

### Exercício 10: Sistema de Funcionários
Crie uma hierarquia de classes para funcionários:
- Classe base `Funcionario` com atributos: `nome`, `salario_base`
- Método `calcular_salario()` que retorna o salário base
- Classe `Gerente` que herda de `Funcionario` e adiciona bônus de 20% ao salário
- Classe `Vendedor` que herda de `Funcionario` e adiciona comissão (atributo `vendas` × 0.1)
- Use `super()` para chamar o método da classe pai quando necessário

**Teste suas classes:**
```python
gerente = Gerente("Ana", 5000)
vendedor = Vendedor("Carlos", 3000, 10000)  # vendas = 10000
print(f"Salário do gerente: R$ {gerente.calcular_salario():.2f}")
print(f"Salário do vendedor: R$ {vendedor.calcular_salario():.2f}")
```

---

## 🔄 Exercícios de Composição e Associação (BEP-021)

### Exercício 11: Sistema de Biblioteca (Associação)
Crie um sistema de biblioteca com:
- Classe `Livro` com atributos: `titulo`, `autor`, `isbn`
- Classe `Aluno` com atributos: `nome`, `matricula`
- Classe `Emprestimo` que representa a associação entre `Aluno` e `Livro`
  - Atributos: `aluno` (objeto Aluno), `livro` (objeto Livro), `data_emprestimo`
  - Método `informacoes()` que retorna detalhes do empréstimo

**Teste suas classes:**
```python
livro = Livro("Python Avançado", "Maria Silva", "978-1234567890")
aluno = Aluno("João", "2024001")
emprestimo = Emprestimo(aluno, livro, "2025-01-15")
print(emprestimo.informacoes())
```

---

### Exercício 12: Sistema de Carro e Motor (Composição)
Crie um sistema onde:
- Classe `Motor` com atributos: `potencia`, `tipo_combustivel`
- Método `ligar()` que retorna "Motor ligado"
- Método `desligar()` que retorna "Motor desligado"
- Classe `Carro` que possui um `Motor` (composição - o motor não existe sem o carro)
- Classe `Carro` com atributos: `marca`, `modelo`, `motor` (objeto Motor)
- Método `ligar_carro()` que chama `motor.ligar()`

**Teste suas classes:**
```python
motor = Motor(150, "Gasolina")
carro = Carro("Toyota", "Corolla", motor)
print(carro.ligar_carro())
```

---

### Exercício 13: Sistema de E-commerce (Múltiplas Relações)
Crie um sistema de e-commerce com:
- Classe `Cliente` com atributos: `nome`, `email`
- Classe `Produto` com atributos: `nome`, `preco`
- Classe `Pedido` que associa `Cliente` e uma lista de `Produto`
  - Atributos: `cliente` (objeto Cliente), `produtos` (lista de Produto), `data`
  - Método `calcular_total()` que retorna a soma dos preços dos produtos
  - Método `adicionar_produto(produto)` que adiciona um produto à lista

**Teste suas classes:**
```python
cliente = Cliente("Maria", "maria@email.com")
produto1 = Produto("Notebook", 2500.00)
produto2 = Produto("Mouse", 50.00)
pedido = Pedido(cliente, "2025-01-15")
pedido.adicionar_produto(produto1)
pedido.adicionar_produto(produto2)
print(f"Total do pedido: R$ {pedido.calcular_total():.2f}")
```

---

## ⚠️ Exercícios de Tratamento de Exceções (BEP-022)

### Exercício 14: Conta Bancária com Exceções
Melhore a classe `ContaBancaria` do Exercício 5 adicionando:
- Exceção customizada `SaldoInsuficienteError` que herda de `Exception`
- No método `sacar()`, levante `SaldoInsuficienteError` se o saldo for insuficiente
- No método `depositar()`, use `try-except` para garantir que o valor seja positivo
- Trate exceções no código de teste

**Teste sua classe:**
```python
conta = ContaBancaria("12345", "Maria")
conta.depositar(1000)
try:
    conta.sacar(1500)  # Deve gerar SaldoInsuficienteError
except SaldoInsuficienteError as e:
    print(f"Erro: {e}")
```

---

### Exercício 15: Validação de Dados com Exceções
Crie uma classe `Usuario` que:
- Possui atributos: `nome`, `email`, `idade`
- Crie exceções customizadas: `NomeInvalidoError`, `EmailInvalidoError`, `IdadeInvalidaError`
- No construtor, valide:
  - Nome não pode ser vazio
  - Email deve conter "@"
  - Idade deve ser entre 0 e 150
- Levante as exceções apropriadas se a validação falhar

**Teste sua classe:**
```python
try:
    usuario = Usuario("", "email@test.com", 25)  # Nome inválido
except NomeInvalidoError as e:
    print(f"Erro: {e}")
```

---

### Exercício 16: Sistema de Divisão com Tratamento de Erros
Crie uma classe `Calculadora` que:
- Possui um método `dividir(a, b)` que retorna a / b
- Use `try-except` para tratar:
  - Divisão por zero (`ZeroDivisionError`)
  - Valores não numéricos (`TypeError`)
- Retorne mensagens de erro apropriadas

**Teste sua classe:**
```python
calc = Calculadora()
try:
    resultado = calc.dividir(10, 0)
except ZeroDivisionError:
    print("Erro: Divisão por zero não permitida!")
```

---

## 🎓 Exercícios Integrados (Todos os Conceitos)

### Exercício 17: Sistema Completo de Biblioteca
Crie um sistema completo de biblioteca que integre todos os conceitos:
- Classe `Livro` com encapsulamento (atributos privados, @property/@setter)
- Classe `Usuario` (herda de uma classe base `Pessoa`)
- Classe `Bibliotecario` (herda de `Usuario` com métodos adicionais)
- Classe `Emprestimo` (associação entre Usuario e Livro)
- Tratamento de exceções para:
  - Livro já emprestado
  - Usuário com empréstimos em atraso
  - Livro não encontrado

**Requisitos:**
- Use herança para Usuario e Bibliotecario
- Use encapsulamento em todas as classes
- Use associação para Emprestimo
- Use exceções customizadas
- Implemente métodos polimórficos

---

### Exercício 18: Sistema de Controle de Estoque
Crie um sistema de controle de estoque completo:
- Classe `Produto` com encapsulamento e validação
- Classe `Fornecedor` (associação com Produto)
- Classe `Estoque` (composição - gerencia uma lista de Produto)
- Classe `Venda` (associação entre Cliente e lista de Produto)
- Tratamento de exceções para:
  - Produto sem estoque
  - Quantidade inválida
  - Fornecedor não encontrado

**Requisitos:**
- Use todos os conceitos aprendidos
- Implemente validações adequadas
- Use exceções customizadas
- Crie métodos polimórficos quando apropriado

---

### Exercício 19: Sistema de Gerenciamento de Projetos
Crie um sistema de gerenciamento de projetos:
- Classe base `Pessoa` com atributos comuns
- Classe `Desenvolvedor` e `GerenteProjeto` (herdam de Pessoa)
- Classe `Projeto` (associação com GerenteProjeto e lista de Desenvolvedor)
- Classe `Tarefa` (composição - pertence a um Projeto)
- Tratamento de exceções para:
  - Projeto sem gerente
  - Tarefa sem desenvolvedor atribuído
  - Data inválida

**Requisitos:**
- Use herança e polimorfismo
- Use composição e associação
- Use encapsulamento
- Implemente exceções customizadas

---

## 📝 Dicas para Resolução

1. **Comece pelos exercícios básicos** e vá progredindo gradualmente
2. **Teste cada método** após implementá-lo
3. **Use nomes descritivos** para classes, métodos e variáveis
4. **Documente seu código** com docstrings
5. **Valide entradas** usando encapsulamento e exceções
6. **Pense na relação** entre classes antes de implementar (herança vs composição vs associação)

---

## ✅ Checklist de Revisão

Após resolver os exercícios, verifique se você:
- [ ] Entende como criar classes e instanciar objetos
- [ ] Sabe usar `__init__` e `self`
- [ ] Compreende encapsulamento com atributos privados
- [ ] Domina `@property` e `@setter`
- [ ] Sabe criar hierarquias com herança
- [ ] Entende polimorfismo e sobrescrita de métodos
- [ ] Sabe diferenciar composição de associação
- [ ] Consegue criar e tratar exceções customizadas
- [ ] Integra todos os conceitos em sistemas completos

---

**Boa sorte com os exercícios! 🚀**

