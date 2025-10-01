# Plano de Aula: Estruturas Condicionais em Python

## Informações Gerais
- **Duração**: 3 horas (180 minutos)
- **Nível**: Iniciante
- **Plataforma**: Google Colab
- **Objetivo**: Ensinar como implementar decisões e diferentes fluxos de execução baseados em condições

---

## Cronograma da Aula

### **1ª Hora (0-60 min): Fundamentos das Estruturas Condicionais**

#### **Abertura (10 min)**
- Apresentação do professor e dos alunos
- Revisão rápida dos conceitos anteriores (variáveis, tipos de dados)
- Objetivos da aula

#### **Conceitos Fundamentais (20 min)**
- O que são estruturas condicionais?
- Quando usar condicionais na programação
- Conceito de fluxo de execução
- Operadores de comparação

#### **Estrutura Básica IF (30 min)**
- Sintaxe básica do `if`
- Indentação em Python
- Operadores de comparação (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Exemplos práticos

---

### **2ª Hora (60-120 min): Estruturas Condicionais Avançadas**

#### **Estrutura IF-ELSE (25 min)**
- Sintaxe do `if-else`
- Quando usar cada estrutura
- Exemplos práticos
- Exercícios básicos

#### **Estrutura IF-ELIF-ELSE (25 min)**
- Sintaxe do `if-elif-else`
- Múltiplas condições
- Ordem de avaliação
- Exemplos práticos

#### **Exercícios Práticos (10 min)**
- Exercícios 1-3 do Google Colab

---

### **3ª Hora (120-180 min): Aplicações Práticas e Boas Práticas**

#### **Operadores Lógicos (20 min)**
- `and`, `or`, `not`
- Combinação de condições
- Precedência de operadores

#### **Boas Práticas (15 min)**
- Indentação correta
- Nomes de variáveis descritivos
- Evitar condições aninhadas excessivas
- Comentários em condicionais

#### **Projetos Práticos (35 min)**
- Exercícios 4-6 do Google Colab
- Projeto: Sistema de notas
- Projeto: Calculadora com operações

#### **Encerramento (10 min)**
- Resumo dos conceitos
- Próximos passos
- Dúvidas e feedback

---

## Conteúdo Detalhado

### **1. Estruturas Condicionais Básicas**

#### **Estrutura IF Simples**
```python
# Sintaxe básica
if condição:
    # código executado se a condição for verdadeira
    print("Condição verdadeira!")

# Exemplo prático
idade = 18
if idade >= 18:
    print("Você é maior de idade!")
```

#### **Estrutura IF-ELSE**
```python
# Sintaxe
if condição:
    # código se verdadeiro
    print("Condição verdadeira!")
else:
    # código se falso
    print("Condição falsa!")

# Exemplo prático
nota = 7.5
if nota >= 7.0:
    print("Aprovado!")
else:
    print("Reprovado!")
```

#### **Estrutura IF-ELIF-ELSE**
```python
# Sintaxe
if condição1:
    # código se condição1 for verdadeira
    print("Primeira condição!")
elif condição2:
    # código se condição2 for verdadeira
    print("Segunda condição!")
else:
    # código se nenhuma condição for verdadeira
    print("Nenhuma condição!")

# Exemplo prático
nota = 8.5
if nota >= 9.0:
    print("Conceito A")
elif nota >= 7.0:
    print("Conceito B")
elif nota >= 5.0:
    print("Conceito C")
else:
    print("Conceito D")
```

### **2. Operadores de Comparação**

#### **Operadores Básicos**
```python
# Igualdade
x == y  # x é igual a y

# Diferença
x != y  # x é diferente de y

# Maior que
x > y   # x é maior que y

# Menor que
x < y   # x é menor que y

# Maior ou igual
x >= y  # x é maior ou igual a y

# Menor ou igual
x <= y  # x é menor ou igual a y
```

#### **Operadores Lógicos**
```python
# E lógico (and)
if idade >= 18 and tem_carteira:
    print("Pode dirigir!")

# OU lógico (or)
if chuva or vento_forte:
    print("Não é um bom dia para sair!")

# NÃO lógico (not)
if not estudou:
    print("Você deveria estudar mais!")
```

### **3. Boas Práticas**

#### **Indentação Correta**
```python
# CORRETO
if condição:
    print("Linha 1")
    print("Linha 2")
    if outra_condição:
        print("Linha 3")

# INCORRETO
if condição:
print("Linha 1")  # Erro de indentação!
```

#### **Nomes Descritivos**
```python
# BOM
if idade >= 18:
    print("Maior de idade")

# RUIM
if i >= 18:
    print("Maior de idade")
```

#### **Evitar Condições Aninhadas Excessivas**
```python
# BOM
if idade >= 18:
    if tem_carteira:
        print("Pode dirigir!")
    else:
        print("Precisa de carteira!")
else:
    print("Muito jovem para dirigir!")

# MELHOR (usando operadores lógicos)
if idade >= 18 and tem_carteira:
    print("Pode dirigir!")
elif idade >= 18:
    print("Precisa de carteira!")
else:
    print("Muito jovem para dirigir!")
```

---

## Exercícios para Google Colab

### **Exercício 1: Verificação de Idade**
```python
# Crie um programa que verifique se uma pessoa é maior de idade
# Solicite a idade do usuário
# Exiba "Maior de idade" ou "Menor de idade"

# Seu código aqui:
```

### **Exercício 2: Sistema de Notas**
```python
# Crie um sistema de notas com os seguintes critérios:
# 9.0 - 10.0: A
# 7.0 - 8.9: B
# 5.0 - 6.9: C
# 0.0 - 4.9: D

# Solicite a nota do usuário e exiba o conceito correspondente

# Seu código aqui:
```

### **Exercício 3: Calculadora de IMC com Classificação**
```python
# Crie um programa que calcule o IMC e classifique:
# IMC < 18.5: Abaixo do peso
# 18.5 <= IMC < 25: Peso normal
# 25 <= IMC < 30: Sobrepeso
# IMC >= 30: Obesidade

# Solicite peso e altura
# Calcule o IMC
# Exiba o resultado e a classificação

# Seu código aqui:
```

### **Exercício 4: Verificação de Acesso**
```python
# Crie um sistema de verificação de acesso:
# Solicite idade e se tem carteira de identidade
# Regras:
# - Menor de 18 anos: "Acesso negado - menor de idade"
# - Maior de 18 anos sem carteira: "Acesso negado - sem documento"
# - Maior de 18 anos com carteira: "Acesso liberado"

# Seu código aqui:
```

### **Exercício 5: Calculadora de Desconto**
```python
# Crie uma calculadora de desconto baseada no valor da compra:
# - Compras até R$ 100: sem desconto
# - Compras de R$ 100 a R$ 500: 5% de desconto
# - Compras de R$ 500 a R$ 1000: 10% de desconto
# - Compras acima de R$ 1000: 15% de desconto

# Solicite o valor da compra
# Calcule o desconto
# Exiba o valor original, desconto e valor final

# Seu código aqui:
```

### **Exercício 6: Projeto Final - Sistema de Login**
```python
# Crie um sistema de login simples:
# 1. Solicite usuário e senha
# 2. Verifique se o usuário existe (usuário: "admin", senha: "123456")
# 3. Exiba mensagens apropriadas:
#    - "Login realizado com sucesso!"
#    - "Usuário incorreto!"
#    - "Senha incorreta!"

# Seu código aqui:
```

---

## Sugestão de Slides

### **Slide 1: Título**
- **Estruturas Condicionais em Python**
- **Decisões na Programação**
- **Professor: [Seu Nome]**
- **Data: [Data da Aula]**

### **Slide 2: Objetivos**
- Compreender o conceito de estruturas condicionais
- Implementar decisões em programas Python
- Usar operadores de comparação e lógicos
- Aplicar boas práticas na escrita de código

### **Slide 3: O que são Condicionais?**
- **Definição**: Estruturas que permitem ao programa tomar decisões
- **Analogia**: Semáforo de trânsito
- **Exemplo**: "Se chover, leve guarda-chuva"

### **Slide 4: Estrutura IF Simples**
```python
if condição:
    # código executado se verdadeiro
```
- **Indentação**: 4 espaços ou 1 tab
- **Dois pontos**: Obrigatório após a condição

### **Slide 5: Operadores de Comparação**
- `==` (igual)
- `!=` (diferente)
- `<` (menor)
- `>` (maior)
- `<=` (menor ou igual)
- `>=` (maior ou igual)

### **Slide 6: Estrutura IF-ELSE**
```python
if condição:
    # código se verdadeiro
else:
    # código se falso
```

### **Slide 7: Estrutura IF-ELIF-ELSE**
```python
if condição1:
    # código 1
elif condição2:
    # código 2
else:
    # código 3
```

### **Slide 8: Operadores Lógicos**
- `and` (E): ambas condições devem ser verdadeiras
- `or` (OU): pelo menos uma condição deve ser verdadeira
- `not` (NÃO): inverte o resultado da condição

### **Slide 9: Boas Práticas**
- **Indentação consistente**
- **Nomes de variáveis descritivos**
- **Evitar condições aninhadas excessivas**
- **Comentários explicativos**

### **Slide 10: Exemplo Prático**
```python
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Maior de idade!")
else:
    print("Menor de idade!")
```

### **Slide 11: Exercícios**
- Lista dos exercícios propostos
- Tempo estimado para cada exercício
- Dicas para resolução

### **Slide 12: Resumo**
- Estruturas condicionais permitem decisões
- `if`, `elif`, `else` para diferentes cenários
- Operadores de comparação e lógicos
- Indentação é fundamental em Python

### **Slide 13: Próximos Passos**
- Estruturas de repetição (loops)
- Listas e dicionários
- Funções
- Projetos mais complexos

### **Slide 14: Dúvidas e Feedback**
- Espaço para perguntas
- Feedback da aula
- Contato para dúvidas

---

## Recursos Complementares

### **Links Úteis**
- [Documentação oficial do Python - Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Tutorial Python - Estruturas Condicionais](https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming)
- [Google Colab - Guia de uso](https://colab.research.google.com/)

### **Material de Apoio**
- Slides com conceitos principais
- Lista de exercícios extras
- Glossário de termos técnicos
- Exemplos de código comentados

### **Avaliação**
- Participação ativa nos exercícios
- Completude dos exercícios propostos
- Demonstração de entendimento dos conceitos
- Qualidade do código produzido

---

## Dicas para o Professor

### **Durante a Aula**
1. **Pace adequado**: Reserve tempo para dúvidas
2. **Exemplos práticos**: Use situações do cotidiano
3. **Interação**: Incentive perguntas e discussões
4. **Demonstração**: Mostre o código funcionando
5. **Indentação**: Enfatize a importância da indentação

### **Gerenciamento de Tempo**
- **1ª hora**: Foco na teoria e conceitos básicos
- **2ª hora**: Prática com exercícios simples
- **3ª hora**: Aplicações mais complexas e projeto final

### **Adaptações Possíveis**
- Se a turma for muito rápida: adicione exercícios extras
- Se houver dificuldades: reduza o número de exercícios e foque na prática
- Para turmas avançadas: inclua conceitos de operadores lógicos avançados

---

## Objetivos de Aprendizagem

Ao final da aula, os alunos devem ser capazes de:

1. **Identificar** quando usar estruturas condicionais
2. **Implementar** estruturas `if`, `elif` e `else` corretamente
3. **Utilizar** operadores de comparação e lógicos
4. **Aplicar** boas práticas na escrita de código
5. **Criar** programas que tomam decisões baseadas em condições
6. **Resolver** problemas práticos usando estruturas condicionais

---

*Este plano de aula foi desenvolvido para uma turma iniciante e pode ser adaptado conforme as necessidades específicas da turma e do tempo disponível.*
