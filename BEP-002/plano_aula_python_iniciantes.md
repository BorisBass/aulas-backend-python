# Plano de Aula: Variáveis, Tipos de Dados e Entrada de Dados em Python

## Informações Gerais
- **Duração**: 3 horas (180 minutos)
- **Nível**: Iniciante
- **Plataforma**: Google Colab
- **Objetivo**: Ensinar os conceitos fundamentais de variáveis, tipos de dados em Python e como receber dados do usuário

---

## Cronograma da Aula

### **1ª Hora (0-60 min): Fundamentos e Tipos de Dados**

#### **Abertura (10 min)**
- Apresentação do professor e dos alunos
- Explicação do ambiente Google Colab
- Objetivos da aula

#### **Conceitos Fundamentais (20 min)**
- O que são variáveis?
- Diferença entre variáveis e constantes
- Nomenclatura de variáveis em Python
- Conceito de tipos de dados

#### **Tipos de Dados Primitivos (30 min)**
- **int** (números inteiros)
- **float** (números decimais)
- **str** (strings/texto)
- **bool** (valores booleanos)
- **None** (valor nulo)

---

### **2ª Hora (60-120 min): Declaração e Manipulação de Variáveis**

#### **Declaração de Variáveis (20 min)**
- Sintaxe básica
- Atribuição de valores
- Múltiplas atribuições
- Verificação de tipos com `type()`

#### **Entrada e Saída de Dados (25 min)**
- Função `print()` para saída
- Função `input()` para entrada
- Formatação de saída
- Interação com o usuário

#### **Exercícios Práticos (15 min)**
- Exercícios 1-3 do Google Colab

---

### **3ª Hora (120-180 min): Casting e Aplicações Práticas**

#### **Casting de Dados (25 min)**
- Conversão entre tipos
- `int()`, `float()`, `str()`, `bool()`
- Tratamento de erros de conversão
- Casos especiais

#### **Exercícios Avançados (30 min)**
- Exercícios 4-6 do Google Colab
- Projeto prático: Calculadora simples

#### **Encerramento (5 min)**
- Resumo dos conceitos
- Próximos passos
- Dúvidas e feedback

---

## Conteúdo Detalhado

### **1. Tipos de Dados Primitivos**

#### **Números Inteiros (int)**
```python
idade = 25
quantidade = 100
temperatura = -10
```

#### **Números Decimais (float)**
```python
altura = 1.75
peso = 68.5
pi = 3.14159
```

#### **Strings (str)**
```python
nome = "João"
sobrenome = 'Silva'
frase = """Esta é uma
frase em múltiplas linhas"""
```

#### **Booleanos (bool)**
```python
aprovado = True
reprovado = False
```

#### **Valor Nulo (None)**
```python
valor = None
```

### **2. Declaração e Uso de Variáveis**

#### **Regras de Nomenclatura**
- Começar com letra ou underscore
- Não pode começar com número
- Case-sensitive
- Não usar palavras reservadas

#### **Exemplos de Nomes Válidos**
```python
nome = "Maria"
_idade = 30
altura2 = 1.65
```

#### **Exemplos de Nomes Inválidos**
```python
# 2nome = "João"  # Erro: começa com número
# class = "A"     # Erro: palavra reservada
```

### **3. Entrada e Saída de Dados**

#### **Saída com print()**
```python
print("Olá, mundo!")
print("Nome:", nome)
print(f"Idade: {idade} anos")
```

#### **Entrada com input()**
```python
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
```

### **4. Casting de Dados**

#### **Conversões Básicas**
```python
# String para int
idade_str = "25"
idade_int = int(idade_str)

# Int para string
numero = 42
numero_str = str(numero)

# String para float
preco_str = "19.99"
preco_float = float(preco_str)
```

---

## Exercícios para Google Colab

### **Exercício 1: Declaração de Variáveis**
```python
# Declare variáveis para armazenar:
# - Seu nome (string)
# - Sua idade (int)
# - Sua altura (float)
# - Se você gosta de programação (bool)

# Seu código aqui:

# Verifique os tipos das variáveis
print("Tipos das variáveis:")
# Seu código aqui:
```

### **Exercício 2: Calculadora de IMC**
```python
# Crie um programa que calcule o IMC (Índice de Massa Corporal)
# Fórmula: IMC = peso / (altura * altura)

# Solicite ao usuário:
# - Peso (em kg)
# - Altura (em metros)

# Seu código aqui:

# Calcule e exiba o IMC
# Seu código aqui:
```

### **Exercício 3: Conversor de Temperatura**
```python
# Crie um conversor de Celsius para Fahrenheit
# Fórmula: F = (C * 9/5) + 32

# Solicite a temperatura em Celsius
# Seu código aqui:

# Converta e exiba em Fahrenheit
# Seu código aqui:
```

### **Exercício 4: Calculadora de Área**
```python
# Crie um programa que calcule a área de um retângulo
# Fórmula: área = base * altura

# Solicite ao usuário:
# - Base do retângulo
# - Altura do retângulo

# Seu código aqui:

# Calcule e exiba a área
# Seu código aqui:
```

### **Exercício 5: Conversor de Medidas**
```python
# Crie um conversor de metros para centímetros
# Fórmula: centímetros = metros * 100

# Solicite a medida em metros
# Seu código aqui:

# Converta e exiba em centímetros
# Seu código aqui:
```

### **Exercício 6: Projeto Final - Perfil do Usuário**
```python
# Crie um programa que colete informações pessoais e faça cálculos simples:
# 1. Solicite nome, idade, altura e peso
# 2. Calcule o IMC
# 3. Calcule quantos dias a pessoa já viveu (idade * 365)
# 4. Exiba um resumo formatado dos dados

# Seu código aqui:
```

---

## Recursos Complementares

### **Links Úteis**
- [Documentação oficial do Python](https://docs.python.org/3/)
- [Tutorial Python para iniciantes](https://docs.python.org/3/tutorial/)
- [Google Colab - Guia de uso](https://colab.research.google.com/)

### **Material de Apoio**
- Slides com conceitos principais
- Lista de exercícios extras
- Glossário de termos técnicos

### **Avaliação**
- Participação ativa nos exercícios
- Completude dos exercícios propostos
- Demonstração de entendimento dos conceitos

---

## Dicas para o Professor

### **Durante a Aula**
1. **Pace adequado**: Reserve tempo para dúvidas
2. **Exemplos práticos**: Use situações do cotidiano
3. **Interação**: Incentive perguntas e discussões
4. **Demonstração**: Mostre o código funcionando

### **Gerenciamento de Tempo**
- **1ª hora**: Foco na teoria e conceitos básicos
- **2ª hora**: Prática com exercícios simples
- **3ª hora**: Aplicações mais complexas e projeto final

### **Adaptações Possíveis**
- Se a turma for muito rápida: adicione exercícios extras
- Se houver dificuldades: reduza o número de exercícios e foque na prática
- Para turmas avançadas: inclua conceitos de listas e dicionários

---

## Objetivos de Aprendizagem

Ao final da aula, os alunos devem ser capazes de:

1. **Identificar** os tipos de dados primitivos em Python
2. **Declarar** variáveis seguindo as regras de nomenclatura
3. **Utilizar** as funções `print()` e `input()` corretamente
4. **Realizar** conversões entre tipos de dados (casting)
5. **Criar** programas simples que interagem com o usuário
6. **Resolver** problemas básicos usando variáveis e tipos de dados

---

*Este plano de aula foi desenvolvido para uma turma iniciante e pode ser adaptado conforme as necessidades específicas da turma e do tempo disponível.*
