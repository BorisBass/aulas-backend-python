# 📚 BEP-020: Respostas dos Exercícios e Desafios

## Herança e Polimorfismo

---

## 📋 Exercício 1: Hierarquia de Funcionários

### Enunciado
1. Crie a classe `Funcionario` com atributos `nome`, `salario` e método `calcular_salario()`.
2. Crie a subclasse `Gerente` que herda de Funcionario e adiciona bônus de 20%.
3. Crie a subclasse `Vendedor` que herda de Funcionario e adiciona comissão baseada em vendas.
4. Sobrescreva `calcular_salario()` em cada subclasse.

### ✅ Resposta Completa

```python
class Funcionario:
    """Classe base para funcionários"""
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base
    
    def calcular_salario(self):
        """Calcula o salário base"""
        return self.salario_base
    
    def __str__(self):
        return f"{self.nome} - Salário: R$ {self.calcular_salario():.2f}"

class Gerente(Funcionario):
    """Gerente herda de Funcionario e adiciona bônus de 20%"""
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)
    
    def calcular_salario(self):
        """Sobrescreve o método para adicionar bônus de 20%"""
        return self.salario_base * 1.20  # 20% de bônus

class Vendedor(Funcionario):
    """Vendedor herda de Funcionario e adiciona comissão"""
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)
        self.vendas = 0  # Total de vendas
    
    def adicionar_venda(self, valor):
        """Adiciona uma venda ao total"""
        if valor > 0:
            self.vendas += valor
    
    def calcular_salario(self):
        """Sobrescreve o método para adicionar comissão de 10%"""
        comissao = self.vendas * 0.10  # 10% de comissão sobre vendas
        return self.salario_base + comissao

# ===== TESTE =====

# Criar funcionários
gerente = Gerente("Maria Silva", 5000)
vendedor = Vendedor("João Santos", 2000)

# Vendedor faz vendas
vendedor.adicionar_venda(5000)
vendedor.adicionar_venda(10000)

# Exibir salários
print("=" * 50)
print("SISTEMA DE FUNCIONÁRIOS")
print("=" * 50)
print(f"\n{gerente}")
print(f"  Salário base: R$ {gerente.salario_base:.2f}")
print(f"  Bônus (20%): R$ {gerente.salario_base * 0.20:.2f}")
print(f"  Salário final: R$ {gerente.calcular_salario():.2f}")

print(f"\n{vendedor}")
print(f"  Salário base: R$ {vendedor.salario_base:.2f}")
print(f"  Vendas totais: R$ {vendedor.vendas:.2f}")
print(f"  Comissão (10%): R$ {vendedor.vendas * 0.10:.2f}")
print(f"  Salário final: R$ {vendedor.calcular_salario():.2f}")
```

### 📊 Saída Esperada
```
==================================================
SISTEMA DE FUNCIONÁRIOS
==================================================

Maria Silva - Salário: R$ 6000.00
  Salário base: R$ 5000.00
  Bônus (20%): R$ 1000.00
  Salário final: R$ 6000.00

João Santos - Salário: R$ 3500.00
  Salário base: R$ 2000.00
  Vendas totais: R$ 15000.00
  Comissão (10%): R$ 1500.00
  Salário final: R$ 3500.00
```

---

## 📋 Exercício 2: Hierarquia de Contas Bancárias

### Enunciado
1. Crie a classe `Conta` com `titular`, `saldo`, métodos `depositar()` e `sacar()`.
2. Crie `ContaCorrente` que herda de Conta e cobra taxa de 2% em cada saque.
3. Crie `ContaPoupanca` que herda de Conta e adiciona método `aplicar_juros()`.
4. Sobrescreva `sacar()` em ContaCorrente para aplicar a taxa.

### ✅ Resposta Completa

```python
class Conta:
    """Classe base para contas bancárias"""
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        """Deposita um valor na conta"""
        if valor > 0:
            self.saldo += valor
            print(f"✅ Depósito de R$ {valor:.2f} realizado. Saldo: R$ {self.saldo:.2f}")
            return True
        print("❌ Valor inválido para depósito!")
        return False
    
    def sacar(self, valor):
        """Saca um valor da conta (sem taxa)"""
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"✅ Saque de R$ {valor:.2f} realizado. Saldo: R$ {self.saldo:.2f}")
            return True
        print("❌ Saldo insuficiente ou valor inválido!")
        return False
    
    def consultar_saldo(self):
        """Consulta o saldo atual"""
        return self.saldo
    
    def __str__(self):
        return f"Conta de {self.titular} - Saldo: R$ {self.saldo:.2f}"

class ContaCorrente(Conta):
    """Conta Corrente com taxa de 2% em cada saque"""
    TAXA_SAQUE = 0.02  # 2% de taxa
    
    def sacar(self, valor):
        """Sobrescreve o método para aplicar taxa de 2%"""
        if valor > 0:
            taxa = valor * self.TAXA_SAQUE
            valor_total = valor + taxa
            
            if valor_total <= self.saldo:
                self.saldo -= valor_total
                print(f"✅ Saque de R$ {valor:.2f} realizado.")
                print(f"   Taxa: R$ {taxa:.2f} (2%)")
                print(f"   Total debitado: R$ {valor_total:.2f}")
                print(f"   Saldo: R$ {self.saldo:.2f}")
                return True
            else:
                print(f"❌ Saldo insuficiente! Necessário: R$ {valor_total:.2f}")
                return False
        print("❌ Valor inválido!")
        return False

class ContaPoupanca(Conta):
    """Conta Poupança com aplicação de juros"""
    def aplicar_juros(self, taxa=0.5):
        """Aplica juros sobre o saldo atual"""
        if self.saldo > 0:
            juros = self.saldo * (taxa / 100)
            self.saldo += juros
            print(f"✅ Juros de {taxa}% aplicado: R$ {juros:.2f}")
            print(f"   Novo saldo: R$ {self.saldo:.2f}")
            return juros
        print("❌ Não há saldo para aplicar juros!")
        return 0

# ===== TESTE =====

print("=" * 50)
print("SISTEMA BANCÁRIO")
print("=" * 50)

# Criar contas
conta_corrente = ContaCorrente("Ana", 1000)
conta_poupanca = ContaPoupanca("Pedro", 5000)

print(f"\n{conta_corrente}")
conta_corrente.depositar(500)
conta_corrente.sacar(100)  # Será cobrada taxa de 2%

print(f"\n{conta_poupanca}")
conta_poupanca.aplicar_juros(0.5)  # 0.5% de juros
conta_poupanca.sacar(200)  # Sem taxa
```

### 📊 Saída Esperada
```
==================================================
SISTEMA BANCÁRIO
==================================================

Conta de Ana - Saldo: R$ 1000.00
✅ Depósito de R$ 500.00 realizado. Saldo: R$ 1500.00
✅ Saque de R$ 100.00 realizado.
   Taxa: R$ 2.00 (2%)
   Total debitado: R$ 102.00
   Saldo: R$ 1398.00

Conta de Pedro - Saldo: R$ 5000.00
✅ Juros de 0.5% aplicado: R$ 25.00
   Novo saldo: R$ 5025.00
✅ Saque de R$ 200.00 realizado. Saldo: R$ 4825.00
```

---

## 📋 Exercício 3: Sistema de Notificações (Polimorfismo)

### Enunciado
1. Crie a classe `Notificacao` com método `enviar()`.
2. Crie subclasses: `Email`, `SMS`, `Push`.
3. Cada subclasse sobrescreve `enviar()` com comportamento específico.
4. Demonstre polimorfismo enviando todas as notificações de forma uniforme.

### ✅ Resposta Completa

```python
class Notificacao:
    """Classe base para notificações"""
    def __init__(self, destinatario, mensagem):
        self.destinatario = destinatario
        self.mensagem = mensagem
    
    def enviar(self):
        """Método base que será sobrescrito"""
        return f"Enviando notificação genérica para {self.destinatario}..."
    
    def __str__(self):
        return f"Notificação para {self.destinatario}"

class Email(Notificacao):
    """Notificação por Email"""
    def enviar(self):
        """Sobrescreve o método para enviar email"""
        return f"📧 Email enviado para {self.destinatario}:\n   Assunto: {self.mensagem}"
    
    def __str__(self):
        return f"Email para {self.destinatario}"

class SMS(Notificacao):
    """Notificação por SMS"""
    def enviar(self):
        """Sobrescreve o método para enviar SMS"""
        return f"📱 SMS enviado para {self.destinatario}:\n   Mensagem: {self.mensagem}"
    
    def __str__(self):
        return f"SMS para {self.destinatario}"

class Push(Notificacao):
    """Notificação Push"""
    def enviar(self):
        """Sobrescreve o método para enviar push notification"""
        return f"🔔 Push notification enviada para {self.destinatario}:\n   Conteúdo: {self.mensagem}"
    
    def __str__(self):
        return f"Push para {self.destinatario}"

# ===== DEMONSTRAÇÃO DE POLIMORFISMO =====

print("=" * 50)
print("SISTEMA DE NOTIFICAÇÕES - POLIMORFISMO")
print("=" * 50)

# Criar diferentes tipos de notificações
notificacoes = [
    Email("ana@email.com", "Bem-vindo ao sistema!"),
    SMS("11999999999", "Seu código de verificação é 1234"),
    Push("user123", "Você tem uma nova mensagem"),
    Email("joao@email.com", "Lembrete: Reunião às 15h"),
    SMS("11888888888", "Pagamento recebido: R$ 500,00")
]

# POLIMORFISMO: Tratamos todos os objetos da mesma forma
print("\n📬 Enviando notificações...\n")
for i, notif in enumerate(notificacoes, 1):
    print(f"{i}. {notif.enviar()}\n")

# Outro exemplo de polimorfismo: função genérica
def enviar_todas_notificacoes(lista_notificacoes):
    """Função que funciona com qualquer tipo de notificação"""
    print("=" * 50)
    print("ENVIANDO TODAS AS NOTIFICAÇÕES")
    print("=" * 50)
    for notif in lista_notificacoes:
        resultado = notif.enviar()  # Polimorfismo em ação!
        print(resultado)
        print()

enviar_todas_notificacoes(notificacoes)
```

### 📊 Saída Esperada
```
==================================================
SISTEMA DE NOTIFICAÇÕES - POLIMORFISMO
==================================================

📬 Enviando notificações...

1. 📧 Email enviado para ana@email.com:
   Assunto: Bem-vindo ao sistema!

2. 📱 SMS enviado para 11999999999:
   Mensagem: Seu código de verificação é 1234

3. 🔔 Push notification enviada para user123:
   Conteúdo: Você tem uma nova mensagem

4. 📧 Email enviado para joao@email.com:
   Assunto: Lembrete: Reunião às 15h

5. 📱 SMS enviado para 11888888888:
   Mensagem: Pagamento recebido: R$ 500,00
```

---

## 📋 Exercício 4: Hierarquia de Produtos

### Enunciado
1. Crie a classe `Produto` com `nome`, `preco` e método `calcular_desconto()`.
2. Crie `ProdutoEletronico` com desconto de 10%.
3. Crie `ProdutoAlimenticio` com desconto de 5%.
4. Crie `ProdutoVestuario` com desconto de 15%.
5. Demonstre polimorfismo calculando descontos de uma lista de produtos.

### ✅ Resposta Completa

```python
class Produto:
    """Classe base para produtos"""
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def calcular_desconto(self):
        """Calcula desconto (sem desconto padrão)"""
        return 0
    
    def preco_final(self):
        """Calcula o preço final com desconto"""
        desconto = self.calcular_desconto()
        return self.preco - desconto
    
    def __str__(self):
        desconto = self.calcular_desconto()
        return (f"{self.nome}\n"
                f"  Preço original: R$ {self.preco:.2f}\n"
                f"  Desconto: R$ {desconto:.2f}\n"
                f"  Preço final: R$ {self.preco_final():.2f}")

class ProdutoEletronico(Produto):
    """Produto eletrônico com desconto de 10%"""
    DESCONTO = 0.10
    
    def calcular_desconto(self):
        """Sobrescreve para calcular desconto de 10%"""
        return self.preco * self.DESCONTO

class ProdutoAlimenticio(Produto):
    """Produto alimentício com desconto de 5%"""
    DESCONTO = 0.05
    
    def calcular_desconto(self):
        """Sobrescreve para calcular desconto de 5%"""
        return self.preco * self.DESCONTO

class ProdutoVestuario(Produto):
    """Produto de vestuário com desconto de 15%"""
    DESCONTO = 0.15
    
    def calcular_desconto(self):
        """Sobrescreve para calcular desconto de 15%"""
        return self.preco * self.DESCONTO

# ===== DEMONSTRAÇÃO DE POLIMORFISMO =====

print("=" * 50)
print("SISTEMA DE PRODUTOS - POLIMORFISMO")
print("=" * 50)

# Criar lista de produtos diferentes
produtos = [
    ProdutoEletronico("Notebook", 3000),
    ProdutoAlimenticio("Arroz 5kg", 20),
    ProdutoVestuario("Camiseta", 50),
    ProdutoEletronico("Smartphone", 1500),
    ProdutoAlimenticio("Feijão 1kg", 8),
    ProdutoVestuario("Calça Jeans", 120)
]

# POLIMORFISMO: Tratamos todos os produtos da mesma forma
print("\n🛒 CARRINHO DE COMPRAS\n")
total_original = 0
total_desconto = 0
total_final = 0

for i, produto in enumerate(produtos, 1):
    print(f"{i}. {produto}\n")
    total_original += produto.preco
    total_desconto += produto.calcular_desconto()
    total_final += produto.preco_final()

print("=" * 50)
print("RESUMO DO PEDIDO")
print("=" * 50)
print(f"Total original: R$ {total_original:.2f}")
print(f"Total de descontos: R$ {total_desconto:.2f}")
print(f"Total a pagar: R$ {total_final:.2f}")

# Função genérica usando polimorfismo
def calcular_total_carrinho(lista_produtos):
    """Função que funciona com qualquer tipo de produto"""
    total = 0
    for produto in lista_produtos:
        total += produto.preco_final()  # Polimorfismo!
    return total

print(f"\nTotal calculado pela função: R$ {calcular_total_carrinho(produtos):.2f}")
```

### 📊 Saída Esperada
```
==================================================
SISTEMA DE PRODUTOS - POLIMORFISMO
==================================================

🛒 CARRINHO DE COMPRAS

1. Notebook
  Preço original: R$ 3000.00
  Desconto: R$ 300.00
  Preço final: R$ 2700.00

2. Arroz 5kg
  Preço original: R$ 20.00
  Desconto: R$ 1.00
  Preço final: R$ 19.00

3. Camiseta
  Preço original: R$ 50.00
  Desconto: R$ 7.50
  Preço final: R$ 42.50

...

==================================================
RESUMO DO PEDIDO
==================================================
Total original: R$ 4698.00
Total de descontos: R$ 469.80
Total a pagar: R$ 4228.20
```

---

## 🎯 Desafio: Sistema de Pagamento

### Enunciado
1. Crie a classe `Pagamento` com método `processar(valor)`.
2. Crie subclasses: `CartaoCredito`, `Boleto`, `Pix`.
3. Cada forma de pagamento processa de forma diferente (com taxas diferentes).
4. Crie uma função que processa qualquer tipo de pagamento usando polimorfismo.

### ✅ Resposta Completa

```python
class Pagamento:
    """Classe base para formas de pagamento"""
    def __init__(self, descricao=""):
        self.descricao = descricao
        self.processado = False
    
    def processar(self, valor):
        """Processa o pagamento (método base)"""
        if valor > 0:
            self.processado = True
            return f"Pagamento de R$ {valor:.2f} processado"
        return "❌ Valor inválido!"
    
    def calcular_taxa(self, valor):
        """Calcula taxa (será sobrescrito)"""
        return 0
    
    def valor_final(self, valor):
        """Calcula valor final com taxa"""
        return valor + self.calcular_taxa(valor)

class CartaoCredito(Pagamento):
    """Pagamento com cartão de crédito (taxa de 3%)"""
    TAXA = 0.03
    
    def calcular_taxa(self, valor):
        """Calcula taxa de 3%"""
        return valor * self.TAXA
    
    def processar(self, valor):
        """Sobrescreve para processar com taxa"""
        if valor > 0:
            taxa = self.calcular_taxa(valor)
            valor_final = valor + taxa
            self.processado = True
            return (f"💳 Pagamento com Cartão de Crédito\n"
                   f"   Valor: R$ {valor:.2f}\n"
                   f"   Taxa (3%): R$ {taxa:.2f}\n"
                   f"   Total: R$ {valor_final:.2f}\n"
                   f"   ✅ Processado com sucesso!")
        return "❌ Valor inválido!"

class Boleto(Pagamento):
    """Pagamento com boleto (taxa de 1.5%)"""
    TAXA = 0.015
    
    def calcular_taxa(self, valor):
        """Calcula taxa de 1.5%"""
        return valor * self.TAXA
    
    def processar(self, valor):
        """Sobrescreve para processar com taxa"""
        if valor > 0:
            taxa = self.calcular_taxa(valor)
            valor_final = valor + taxa
            self.processado = True
            return (f"📄 Pagamento com Boleto\n"
                   f"   Valor: R$ {valor:.2f}\n"
                   f"   Taxa (1.5%): R$ {taxa:.2f}\n"
                   f"   Total: R$ {valor_final:.2f}\n"
                   f"   ⏳ Vencimento em 3 dias úteis")
        return "❌ Valor inválido!"

class Pix(Pagamento):
    """Pagamento com PIX (sem taxa)"""
    def processar(self, valor):
        """Sobrescreve para processar sem taxa"""
        if valor > 0:
            self.processado = True
            return (f"⚡ Pagamento com PIX\n"
                   f"   Valor: R$ {valor:.2f}\n"
                   f"   Taxa: R$ 0.00 (sem taxa)\n"
                   f"   Total: R$ {valor:.2f}\n"
                   f"   ✅ Processado instantaneamente!")
        return "❌ Valor inválido!"

# ===== FUNÇÃO COM POLIMORFISMO =====

def processar_pagamento(pagamento, valor):
    """
    Função genérica que processa qualquer tipo de pagamento.
    Demonstra polimorfismo!
    """
    print("=" * 50)
    print(f"PROCESSANDO PAGAMENTO")
    print("=" * 50)
    resultado = pagamento.processar(valor)
    print(resultado)
    return pagamento.processado

# ===== TESTE =====

print("=" * 50)
print("SISTEMA DE PAGAMENTO - POLIMORFISMO")
print("=" * 50)

# Criar diferentes formas de pagamento
pagamentos = [
    CartaoCredito("Visa"),
    Boleto("Boleto Bancário"),
    Pix("PIX")
]

valor_compra = 1000.00

print(f"\n💰 Valor da compra: R$ {valor_compra:.2f}\n")

# POLIMORFISMO: Processamos todos da mesma forma
for pagamento in pagamentos:
    processar_pagamento(pagamento, valor_compra)
    print()

# Comparação de taxas
print("=" * 50)
print("COMPARAÇÃO DE TAXAS")
print("=" * 50)
print(f"Valor: R$ {valor_compra:.2f}\n")

for pagamento in pagamentos:
    taxa = pagamento.calcular_taxa(valor_compra)
    total = pagamento.valor_final(valor_compra)
    tipo = pagamento.__class__.__name__
    print(f"{tipo}:")
    print(f"  Taxa: R$ {taxa:.2f}")
    print(f"  Total: R$ {total:.2f}\n")
```

### 📊 Saída Esperada
```
==================================================
SISTEMA DE PAGAMENTO - POLIMORFISMO
==================================================

💰 Valor da compra: R$ 1000.00

==================================================
PROCESSANDO PAGAMENTO
==================================================
💳 Pagamento com Cartão de Crédito
   Valor: R$ 1000.00
   Taxa (3%): R$ 30.00
   Total: R$ 1030.00
   ✅ Processado com sucesso!

==================================================
PROCESSANDO PAGAMENTO
==================================================
📄 Pagamento com Boleto
   Valor: R$ 1000.00
   Taxa (1.5%): R$ 15.00
   Total: R$ 1015.00
   ⏳ Vencimento em 3 dias úteis

==================================================
PROCESSANDO PAGAMENTO
==================================================
⚡ Pagamento com PIX
   Valor: R$ 1000.00
   Taxa: R$ 0.00 (sem taxa)
   Total: R$ 1000.00
   ✅ Processado instantaneamente!

==================================================
COMPARAÇÃO DE TAXAS
==================================================
Valor: R$ 1000.00

CartaoCredito:
  Taxa: R$ 30.00
  Total: R$ 1030.00

Boleto:
  Taxa: R$ 15.00
  Total: R$ 1015.00

Pix:
  Taxa: R$ 0.00
  Total: R$ 1000.00
```

---

## 🎓 Exercícios Extras (Desafios Avançados)

### Desafio 1: Sistema de Formas Geométricas

```python
class Forma:
    """Classe base para formas geométricas"""
    def __init__(self, nome):
        self.nome = nome
    
    def calcular_area(self):
        """Método abstrato (será sobrescrito)"""
        raise NotImplementedError("Subclasse deve implementar calcular_area()")
    
    def calcular_perimetro(self):
        """Método abstrato (será sobrescrito)"""
        raise NotImplementedError("Subclasse deve implementar calcular_perimetro()")

class Retangulo(Forma):
    def __init__(self, largura, altura):
        super().__init__("Retângulo")
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

class Circulo(Forma):
    def __init__(self, raio):
        super().__init__("Círculo")
        self.raio = raio
    
    def calcular_area(self):
        return 3.14159 * self.raio ** 2
    
    def calcular_perimetro(self):
        return 2 * 3.14159 * self.raio

# Polimorfismo
formas = [Retangulo(5, 3), Circulo(4), Retangulo(10, 2)]

for forma in formas:
    print(f"{forma.nome}:")
    print(f"  Área: {forma.calcular_area():.2f}")
    print(f"  Perímetro: {forma.calcular_perimetro():.2f}\n")
```

### Desafio 2: Sistema de Veículos com Polimorfismo Avançado

```python
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0
    
    def acelerar(self):
        self.velocidade += 10
        return f"{self.modelo} acelerou para {self.velocidade} km/h"
    
    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
        return f"{self.modelo} freou para {self.velocidade} km/h"

class Carro(Veiculo):
    def acelerar(self):
        self.velocidade += 15
        return f"🚗 {self.modelo} acelerou para {self.velocidade} km/h"

class Moto(Veiculo):
    def acelerar(self):
        self.velocidade += 25
        return f"🏍️ {self.modelo} acelerou para {self.velocidade} km/h"

class Caminhao(Veiculo):
    def acelerar(self):
        self.velocidade += 5
        return f"🚚 {self.modelo} acelerou para {self.velocidade} km/h"

# Polimorfismo
veiculos = [
    Carro("Toyota", "Corolla"),
    Moto("Honda", "CB600"),
    Caminhao("Volvo", "FH")
]

for veiculo in veiculos:
    print(veiculo.acelerar())
    print(veiculo.acelerar())
    print(veiculo.frear())
    print()
```

---

## 📝 Dicas para Resolver os Exercícios

### 1. **Entenda a Hierarquia**
- Identifique qual é a classe pai (superclasse)
- Identifique quais são as classes filhas (subclasses)
- Pense no que é comum e no que é específico

### 2. **Use `super()`**
- Sempre use `super().__init__()` no construtor da subclasse
- Isso garante que a classe pai seja inicializada corretamente

### 3. **Sobrescreva Métodos**
- Use o mesmo nome do método da classe pai
- Implemente o comportamento específico da subclasse

### 4. **Aplique Polimorfismo**
- Crie listas com objetos de diferentes tipos
- Trate todos da mesma forma
- O Python chama o método correto automaticamente

### 5. **Teste Sempre**
- Crie objetos de cada classe
- Teste os métodos herdados e sobrescritos
- Verifique se o polimorfismo está funcionando

---

## ✅ Checklist de Aprendizado

Após resolver os exercícios, você deve ser capaz de:

- [ ] Criar classes pai e subclasses
- [ ] Usar `super()` corretamente
- [ ] Sobrescrever métodos (override)
- [ ] Aplicar polimorfismo em listas
- [ ] Criar funções genéricas que funcionam com diferentes tipos
- [ ] Entender quando usar herança vs composição

---

**Bons estudos! 🚀**

