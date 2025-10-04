# Soluções dos Exercícios - Variáveis, Tipos de Dados e Entrada de Dados

## Exercício 1: Declaração de Variáveis

```python
# Declare variáveis para armazenar:
# - Seu nome (string)
# - Sua idade (int)
# - Sua altura (float)
# - Se você gosta de programação (bool)

nome = "João Silva"
idade = 25
altura = 1.75
gosta_programacao = True

# Verifique os tipos das variáveis
print("Tipos das variáveis:")
print(f"Nome: {type(nome)}")
print(f"Idade: {type(idade)}")
print(f"Altura: {type(altura)}")
print(f"Gosta de programação: {type(gosta_programacao)}")
```

## Exercício 2: Calculadora de IMC

```python
# Crie um programa que calcule o IMC (Índice de Massa Corporal)
# Fórmula: IMC = peso / (altura * altura)

# Solicite ao usuário:
# - Peso (em kg)
# - Altura (em metros)

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcule e exiba o IMC
imc = peso / (altura * altura)
print(f"Seu IMC é: {imc:.2f}")
```

## Exercício 3: Conversor de Temperatura

```python
# Crie um conversor de Celsius para Fahrenheit
# Fórmula: F = (C * 9/5) + 32

# Solicite a temperatura em Celsius
celsius = float(input("Digite a temperatura em Celsius: "))

# Converta e exiba em Fahrenheit
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equivale a {fahrenheit}°F")
```

## Exercício 4: Calculadora de Área

```python
# Crie um programa que calcule a área de um retângulo
# Fórmula: área = base * altura

# Solicite ao usuário:
# - Base do retângulo
# - Altura do retângulo

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

# Calcule e exiba a área
area = base * altura
print(f"A área do retângulo é: {area:.2f}")
```

## Exercício 5: Conversor de Medidas

```python
# Crie um conversor de metros para centímetros
# Fórmula: centímetros = metros * 100

# Solicite a medida em metros
metros = float(input("Digite a medida em metros: "))

# Converta e exiba em centímetros
centimetros = metros * 100
print(f"{metros} metros = {centimetros} centímetros")
```

## Exercício 6: Projeto Final - Perfil do Usuário

```python
# Crie um programa que colete informações pessoais e faça cálculos simples:
# 1. Solicite nome, idade, altura e peso
# 2. Calcule o IMC
# 3. Calcule quantos dias a pessoa já viveu (idade * 365)
# 4. Exiba um resumo formatado dos dados

print("=== PERFIL DO USUÁRIO ===")

# Entrada de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))

# Cálculos
imc = peso / (altura * altura)
dias_vividos = idade * 365

# Exibição do resumo
print("\n" + "="*40)
print("RESUMO DO PERFIL")
print("="*40)
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura} metros")
print(f"Peso: {peso} kg")
print(f"IMC: {imc:.2f}")
print(f"Dias vividos: {dias_vividos} dias")
print("="*40)
```

## Exercícios Extras (Para Prática Adicional)

### Exercício Extra 1: Calculadora de Média

```python
# Crie uma calculadora que:
# 1. Solicite 3 notas
# 2. Calcule a média

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Sua média é: {media:.2f}")
```

### Exercício Extra 2: Conversor de Moedas

```python
# Crie um conversor de reais para dólares
# Taxa de câmbio: 1 USD = 5.20 BRL

valor_reais = float(input("Digite o valor em reais: "))
taxa_cambio = 5.20

valor_dolares = valor_reais / taxa_cambio

print(f"R$ {valor_reais:.2f} = US$ {valor_dolares:.2f}")
```

### Exercício Extra 3: Calculadora de Volume

```python
# Crie um programa que calcule o volume de uma caixa
# Fórmula: volume = comprimento * largura * altura

comprimento = float(input("Digite o comprimento: "))
largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))

volume = comprimento * largura * altura

print(f"O volume da caixa é: {volume:.2f}")
```

## Dicas para o Professor

### **Durante a Correção dos Exercícios:**

1. **Exercício 1**: Enfatize a importância de verificar tipos com `type()`
2. **Exercício 2**: Mostre como usar formatação de números decimais
3. **Exercício 3**: Demonstre a precedência de operadores matemáticos
4. **Exercício 4**: Explique operações matemáticas básicas
5. **Exercício 5**: Mostre conversões simples de unidades
6. **Exercício 6**: Integre múltiplos conceitos em um projeto

### **Conceitos Importantes a Destacar:**

- **Casting**: Sempre necessário ao usar `input()` para números
- **Formatação**: Uso de f-strings para saída mais elegante
- **Operadores matemáticos**: +, -, *, /, ** (potência)
- **Variáveis**: Armazenamento e reutilização de valores
- **Entrada/Saída**: Interação básica com o usuário

### **Adaptações por Nível:**

- **Iniciantes**: Foque nos exercícios 1-3
- **Intermediários**: Inclua exercícios 4-6
- **Prática extra**: Adicione os exercícios extras
