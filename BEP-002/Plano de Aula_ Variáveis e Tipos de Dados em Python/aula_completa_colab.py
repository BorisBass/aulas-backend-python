
"""
# Plano de Aula: Variáveis, Tipos de Dados e Entrada de Dados em Python

## Duração: 3 horas

## Público-alvo: Iniciantes em Programação

## Objetivo Geral:
Ao final desta aula, os alunos serão capazes de compreender e aplicar os conceitos fundamentais de variáveis, tipos de dados e entrada/saída de dados em Python, além de realizar a conversão de tipos (casting).

## Conteúdo Programático:

### 1. Introdução (15 minutos)
- Boas-vindas e apresentação da aula.
- Importância das variáveis e tipos de dados na programação.
- Breve introdução ao ambiente Google Colab.

### 2. Tipos de Dados Primitivos (45 minutos)
- O que são tipos de dados?
- Principais tipos de dados em Python:
  - Inteiros (`int`)
  - Números de ponto flutuante (`float`)
  - Strings (`str`)
  - Booleanos (`bool`)
- Exemplos práticos e demonstrações no Google Colab.

### 3. Variáveis: Declaração e Uso (60 minutos)
- O que são variáveis e por que usá-las?
- Regras para nomes de variáveis em Python.
- Atribuição de valores a variáveis.
- Reatribuição de valores.
- Diferença entre constantes e variáveis (convenções em Python).
- Exercícios práticos de declaração e uso de variáveis.

### 4. Entrada e Saída de Dados (45 minutos)
- Função `print()` para saída de dados:
  - Impressão de texto.
  - Impressão de variáveis.
  - Concatenação e formatação de strings (f-strings).
- Função `input()` para entrada de dados:
  - Recebendo dados do usuário.
  - `input()` sempre retorna string.
- Exercícios práticos de entrada e saída de dados.

### 5. Casting de Dados (30 minutos)
- Por que converter tipos de dados?
- Funções de conversão (`int()`, `float()`, `str()`, `bool()`).
- Exemplos e cenários de uso.
- Exercícios práticos de casting.

### 6. Revisão e Perguntas (15 minutos)
- Resumo dos principais conceitos abordados.
- Espaço para dúvidas e esclarecimentos.

## Metodologia:
- Aula expositiva com apresentação de slides (ou anotações no Colab).
- Demonstrações ao vivo no Google Colab.
- Exercícios práticos para os alunos realizarem individualmente ou em duplas no Google Colab.
- Discussão e correção dos exercícios em sala.

## Recursos:
- Google Colab (ambiente de desenvolvimento).
- Material de apoio (notebook Colab com exemplos e exercícios).

## Avaliação:
- Participação nas atividades e discussões.
- Resolução dos exercícios propostos.

"""

# ----------------------------------------------------------------------------------------------------------------------
# Conteúdo da Aula e Exercícios Práticos
# Você pode copiar e colar todo o conteúdo abaixo em uma única célula do Google Colab e executá-lo.
# ----------------------------------------------------------------------------------------------------------------------

print("""
# Aula: Variáveis, Tipos de Dados e Entrada de Dados em Python

Bem-vindos à nossa aula sobre os fundamentos da programação em Python! Hoje, vamos explorar conceitos essenciais que são a base para qualquer programa que você venha a desenvolver: **Variáveis**, **Tipos de Dados** e **Entrada de Dados**.

## Objetivo da Aula
Ao final desta aula, você será capaz de:

*   Compreender o que são variáveis e como utilizá-las para armazenar informações.
*   Identificar e trabalhar com os principais tipos de dados primitivos em Python (inteiros, decimais, textos e booleanos).
*   Receber dados do usuário através da função `input()` e exibir informações com a função `print()`.
*   Realizar a conversão de tipos de dados (casting) quando necessário.

Vamos começar!
""")

print("""
## 1. Tipos de Dados Primitivos

Em Python, todo valor tem um tipo de dado. Conhecer os tipos de dados é fundamental para entender como o Python armazena e manipula as informações.

### Inteiros (`int`)
Representam números inteiros, positivos ou negativos, sem casas decimais.
""")

idade = 25
quantidade = 100
print(f"idade = {idade}, tipo: {type(idade)}")
print(f"quantidade = {quantidade}, tipo: {type(quantidade)}")

print("""
### Números de Ponto Flutuante (`float`)
Representam números reais, com casas decimais.
""")

altura = 1.75
preco = 99.99
print(f"altura = {altura}, tipo: {type(altura)}")
print(f"preco = {preco}, tipo: {type(preco)}")

print("""
### Strings (`str`)
Representam sequências de caracteres (texto). Podem ser definidas com aspas simples (`'`) ou aspas duplas (`"`).
""")

nome = "Alice"
mensagem = 'Olá, mundo!'
print(f"nome = '{nome}', tipo: {type(nome)}")
print(f"mensagem = '{mensagem}', tipo: {type(mensagem)}")

print("""
### Booleanos (`bool`)
Representam valores lógicos: `True` (verdadeiro) ou `False` (falso). São muito usados em condições e tomadas de decisão.
""")

esta_chovendo = True
tem_desconto = False
print(f"esta_chovendo = {esta_chovendo}, tipo: {type(esta_chovendo)}")
print(f"tem_desconto = {tem_desconto}, tipo: {type(tem_desconto)}")

print("""
---

### Exercício 1: Identificação de Tipos de Dados

**Objetivo:** Praticar a identificação dos tipos de dados primitivos em Python.

**Instruções:** Para cada variável abaixo, adicione um comentário indicando qual é o seu tipo de dado (int, float, str, bool). Use a função `type()` para verificar se precisar.
""")

# Variável 1
idade_ex1 = 30
# Tipo: int
print(f"idade_ex1 = {idade_ex1}, tipo: {type(idade_ex1)}")

# Variável 2
preco_ex1 = 19.99
# Tipo: float
print(f"preco_ex1 = {preco_ex1}, tipo: {type(preco_ex1)}")

# Variável 3
nome_ex1 = "Maria"
# Tipo: str
print(f"nome_ex1 = '{nome_ex1}', tipo: {type(nome_ex1)}")

# Variável 4
is_estudante_ex1 = True
# Tipo: bool
print(f"is_estudante_ex1 = {is_estudante_ex1}, tipo: {type(is_estudante_ex1)}")

# Variável 5
numero_grande_ex1 = 1000000
# Tipo: int
print(f"numero_grande_ex1 = {numero_grande_ex1}, tipo: {type(numero_grande_ex1)}")

# Variável 6
temperatura_ex1 = -5.5
# Tipo: float
print(f"temperatura_ex1 = {temperatura_ex1}, tipo: {type(temperatura_ex1)}")

# Variável 7
mensagem_ex1 = "Olá, mundo!"
# Tipo: str
print(f"mensagem_ex1 = '{mensagem_ex1}', tipo: {type(mensagem_ex1)}")

# Variável 8
tem_desconto_ex1 = False
# Tipo: bool
print(f"tem_desconto_ex1 = {tem_desconto_ex1}, tipo: {type(tem_desconto_ex1)}")

print("""
---

## 2. Variáveis: Declaração e Uso

Variáveis são como "caixas" ou "contêineres" que usamos para armazenar dados na memória do computador. Elas nos permitem dar nomes significativos aos valores, facilitando a leitura e manutenção do código.

### Regras para Nomes de Variáveis em Python
*   Devem começar com uma letra (a-z, A-Z) ou um underscore (`_`).
*   Não podem começar com números.
*   Podem conter letras, números e underscores.
*   São *case-sensitive* (maiúsculas e minúsculas fazem diferença): `nome` é diferente de `Nome`.
*   Não podem ser palavras reservadas do Python (ex: `if`, `else`, `for`, `while`, `print`, `input`).

### Atribuição de Valores
Usamos o operador de atribuição (`=`) para dar um valor a uma variável.
""")

nome_aluno = "Carlos"
nota1 = 8.5
nota2 = 7.0
media = (nota1 + nota2) / 2
print(f"O aluno {nome_aluno} teve média {media}")

print("""
### Reatribuição de Valores
Você pode mudar o valor de uma variável a qualquer momento.
""")

contador = 0
print(f"Contador inicial: {contador}")
contador = contador + 1
print(f"Contador após incremento: {contador}")
contador = "fim" # Variáveis podem mudar de tipo em Python (tipagem dinâmica)
print(f"Contador agora é: {contador}")

print("""
### Diferença entre Constantes e Variáveis (Convenções em Python)
Python não tem um conceito de "constante" como em outras linguagens (onde o valor não pode ser alterado depois de definido). No entanto, por **convenção**, usamos nomes de variáveis em **MAIÚSCULAS** para indicar que elas devem ser tratadas como constantes, ou seja, seus valores não devem ser alterados durante a execução do programa.
""")

PI = 3.14159
TAXA_JUROS = 0.05

print(f"Valor de PI: {PI}")
print(f"Taxa de Juros: {TAXA_JUROS}")

# Embora seja possível, evite reatribuir constantes por convenção
# PI = 3.0 # Não faça isso em um código real se PI for uma constante

print("""
---

### Exercício 2: Declaração e Manipulação de Variáveis

**Objetivo:** Praticar a declaração, atribuição e reatribuição de valores a variáveis.

**Instruções:**
1. Declare uma variável `cidade` e atribua a ela o nome da sua cidade.
2. Declare uma variável `populacao` e atribua a ela um valor numérico (aproximado) da população da sua cidade.
3. Imprima o valor de ambas as variáveis.
4. Reatribua a variável `cidade` para o nome de outra cidade.
5. Reatribua a variável `populacao` para um novo valor.
6. Imprima os novos valores das variáveis.
""")

# Seu código aqui
cidade = "São Paulo"
populacao = 12000000
print(f"Cidade: {cidade}, População: {populacao}")

cidade = "Rio de Janeiro"
populacao = 6700000
print(f"Nova Cidade: {cidade}, Nova População: {populacao}")

print("""
---

## 3. Entrada e Saída de Dados

Para que nossos programas sejam interativos, precisamos de formas de exibir informações para o usuário (saída) e de receber informações dele (entrada).

### Função `print()` para Saída de Dados
A função `print()` é usada para exibir mensagens e valores na tela.
""")

print("Olá, Python!")

nome_print = "Ana"
idade_print = 28

# Imprimindo variáveis
print(nome_print)
print(idade_print)

# Concatenação de strings (não recomendado para muitas variáveis)
print("Meu nome é " + nome_print + " e tenho " + str(idade_print) + " anos.")

# F-strings (formatar strings) - RECOMENDADO!
print(f"Meu nome é {nome_print} e tenho {idade_print} anos.")

# Múltiplos argumentos para print (separados por espaço por padrão)
print("Nome:", nome_print, "Idade:", idade_print)

print("""
### Função `input()` para Entrada de Dados
A função `input()` é usada para receber dados digitados pelo usuário. **Importante:** `input()` sempre retorna o valor como uma **string**.
""")

# Exemplo básico
nome_usuario = input("Digite seu nome: ")
print(f"Bem-vindo(a), {nome_usuario}!")

# Recebendo um número (ainda como string!)
numero_str_input = input("Digite um número: ")
print(f"Você digitou: {numero_str_input}, que é do tipo: {type(numero_str_input)}")

print("""
---

### Exercício 3: Entrada e Saída de Dados

**Objetivo:** Utilizar as funções `input()` e `print()` para interagir com o usuário.

**Instruções:**
1. Peça ao usuário para digitar seu nome e armazene-o em uma variável `seu_nome`.
2. Peça ao usuário para digitar sua idade e armazene-a em uma variável `sua_idade`.
3. Usando f-strings, imprima uma mensagem personalizada que inclua o nome e a idade digitados pelo usuário.
   Exemplo: "Olá, [seu_nome]! Você tem [sua_idade] anos."
""")

# Seu código aqui
seu_nome = input("Digite seu nome: ")
sua_idade = input("Digite sua idade: ")
print(f"Olá, {seu_nome}! Você tem {sua_idade} anos.")

print("""
---

## 4. Casting de Dados

Como vimos, a função `input()` sempre retorna uma string. Mas e se precisarmos fazer cálculos com os números que o usuário digitou? Precisamos converter (ou fazer o "casting") essa string para um tipo numérico (inteiro ou float).

### Funções de Conversão
*   `int()`: Converte para inteiro.
*   `float()`: Converte para número de ponto flutuante.
*   `str()`: Converte para string.
*   `bool()`: Converte para booleano.
""")

# Exemplo de conversão de string para int
numero_str_cast = "123"
numero_int_cast = int(numero_str_cast)
print(f"'{numero_str_cast}' (tipo: {type(numero_str_cast)}) convertido para {numero_int_cast} (tipo: {type(numero_int_cast)}))")

# Exemplo de conversão de string para float
valor_str_cast = "45.67"
valor_float_cast = float(valor_str_cast)
print(f"'{valor_str_cast}' (tipo: {type(valor_str_cast)}) convertido para {valor_float_cast} (tipo: {type(valor_float_cast)}))")

# Exemplo de uso com input()
num1_str_cast_input = input("Digite o primeiro número: ")
num2_str_cast_input = input("Digite o segundo número: ")

num1_cast = int(num1_str_cast_input)
num2_cast = int(num2_str_cast_input)

soma_cast = num1_cast + num2_cast
print(f"A soma é: {soma_cast}")

print("""
# Cuidado com erros de conversão!
# int("abc") # Isso geraria um erro!
""")

print("""
---

### Exercício 4: Casting de Dados

**Objetivo:** Praticar a conversão de tipos de dados (casting).

**Instruções:**
1. Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis (lembre-se que `input()` retorna string).
2. Converta essas strings para números inteiros.
3. Calcule a soma, subtração, multiplicação e divisão desses dois números.
4. Imprima os resultados de cada operação, indicando qual operação foi realizada.
""")

# Seu código aqui
num1_ex4_str = input("Digite o primeiro número inteiro: ")
num2_ex4_str = input("Digite o segundo número inteiro: ")

num1_ex4 = int(num1_ex4_str)
num2_ex4 = int(num2_ex4_str)

soma_ex4 = num1_ex4 + num2_ex4
subtracao_ex4 = num1_ex4 - num2_ex4
multiplicacao_ex4 = num1_ex4 * num2_ex4
divisao_ex4 = num1_ex4 / num2_ex4 # A divisão sempre retorna um float

print(f"Soma: {soma_ex4}")
print(f"Subtração: {subtracao_ex4}")
print(f"Multiplicação: {multiplicacao_ex4}")
print(f"Divisão: {divisao_ex4}")

print("""
---

### Exercício 5: Desafio Combinado

**Objetivo:** Combinar os conceitos de variáveis, entrada/saída e casting.

**Instruções:**
1. Peça ao usuário para digitar o preço de um produto e a quantidade comprada.
2. Calcule o valor total da compra.
3. Peça ao usuário para digitar o valor pago.
4. Calcule o troco.
5. Imprima o valor total da compra e o troco de forma formatada.
""")

# Seu código aqui
preco_ex5_str = input("Digite o preço do produto: ")
quantidade_ex5_str = input("Digite a quantidade comprada: ")

preco_ex5 = float(preco_ex5_str)
quantidade_ex5 = int(quantidade_ex5_str)

valor_total_ex5 = preco_ex5 * quantidade_ex5
print(f"Valor total da compra: R$ {valor_total_ex5:.2f}")

valor_pago_ex5_str = input("Digite o valor pago: ")
valor_pago_ex5 = float(valor_pago_ex5_str)

troco_ex5 = valor_pago_ex5 - valor_total_ex5
print(f"Troco: R$ {troco_ex5:.2f}")

print("""
---

### Exercício Extra: Calculadora Simples

**Objetivo:** Criar uma calculadora simples que receba dois números e uma operação, e exiba o resultado.

**Instruções:**
1. Peça ao usuário para digitar o primeiro número.
2. Peça ao usuário para digitar o segundo número.
3. Peça ao usuário para digitar a operação desejada (ex: '+', '-', '*', '/').
4. Realize a operação e imprima o resultado. Lembre-se de converter os números para o tipo correto antes de realizar a operação.
""")

# Seu código aqui
num1_calc_str = input("Digite o primeiro número: ")
num2_calc_str = input("Digite o segundo número: ")
operacao_calc = input("Digite a operação (+, -, *, /): ")

num1_calc = float(num1_calc_str)
num2_calc = float(num2_calc_str)

if operacao_calc == '+':
    resultado_calc = num1_calc + num2_calc
elif operacao_calc == '-':
    resultado_calc = num1_calc - num2_calc
elif operacao_calc == '*':
    resultado_calc = num1_calc * num2_calc
elif operacao_calc == '/':
    if num2_calc != 0:
        resultado_calc = num1_calc / num2_calc
    else:
        resultado_calc = "Erro: Divisão por zero!"
else:
    resultado_calc = "Operação inválida!"

print(f"Resultado: {resultado_calc}")

print("""
---

### Exercício 6: Conversão de Temperatura

**Objetivo:** Converter uma temperatura de Celsius para Fahrenheit usando casting.

**Instruções:**
1. Peça ao usuário para digitar uma temperatura em Celsius (número decimal).
2. Converta a entrada para o tipo `float`.
3. Calcule a temperatura em Fahrenheit usando a fórmula: `Fahrenheit = (Celsius * 9/5) + 32`.
4. Imprima o resultado formatado com duas casas decimais.
""")

# Seu código aqui
celsius_str_temp = input("Digite a temperatura em Celsius: ")
celsius_temp = float(celsius_str_temp)
fahrenheit_temp = (celsius_temp * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit_temp:.2f}F")

print("""
---

### Exercício 7: Análise de Dados de Usuário

**Objetivo:** Coletar diferentes tipos de dados do usuário e garantir que estejam nos formatos corretos.

**Instruções:**
1. Peça ao usuário para digitar seu nome completo.
2. Peça ao usuário para digitar o ano de seu nascimento.
3. Peça ao usuário para digitar sua altura em metros (ex: 1.75).
4. Converta o ano de nascimento para `int` e a altura para `float`.
5. Calcule a idade aproximada do usuário (ano atual - ano de nascimento).
6. Imprima todas as informações coletadas e calculadas, incluindo os tipos de dados de cada variável após o casting.
""")

# Seu código aqui
import datetime

nome_completo_user = input("Digite seu nome completo: ")
ano_nascimento_user_str = input("Digite o ano de seu nascimento: ")
altura_user_str = input("Digite sua altura em metros (ex: 1.75): ")

ano_nascimento_user = int(ano_nascimento_user_str)
altura_user = float(altura_user_str)

ano_atual_user = datetime.datetime.now().year
idade_user = ano_atual_user - ano_nascimento_user

print(f"Nome: {nome_completo_user} (Tipo: {type(nome_completo_user)})")
print(f"Ano de Nascimento: {ano_nascimento_user} (Tipo: {type(ano_nascimento_user)})")
print(f"Altura: {altura_user} (Tipo: {type(altura_user)})")
print(f"Idade aproximada: {idade_user} anos")

print("""
---

### Exercício 8: Soma Segura de Números

**Objetivo:** Receber dois números do usuário e somá-los, tratando possíveis erros de conversão.

**Instruções:**
1. Peça ao usuário para digitar o primeiro número.
2. Peça ao usuário para digitar o segundo número.
3. Tente converter ambos para `float` e some-os.
4. Se a conversão falhar (por exemplo, se o usuário digitar texto), imprima uma mensagem de erro amigável. (Dica: use um bloco `try-except` se já tiver aprendido, caso contrário, apenas comente sobre o erro).
5. Imprima o resultado da soma ou a mensagem de erro.
""")

# Seu código aqui
num1_soma_str = input("Digite o primeiro número: ")
num2_soma_str = input("Digite o segundo número: ")

try:
    num1_soma = float(num1_soma_str)
    num2_soma = float(num2_soma_str)
    soma_segura = num1_soma + num2_soma
    print(f"A soma é: {soma_segura}")
except ValueError:
    print("Erro: Por favor, digite apenas números válidos.")

print("""
---

## Conclusão

Parabéns! Você concluiu a primeira parte da nossa jornada em Python. Hoje, você aprendeu sobre:

*   **Tipos de Dados Primitivos:** `int`, `float`, `str`, `bool`
*   **Variáveis:** Como declarar, usar e a diferença entre variáveis e "constantes" (por convenção).
*   **Entrada e Saída de Dados:** Usando `print()` para exibir e `input()` para receber informações.
*   **Casting de Dados:** Convertendo tipos com `int()`, `float()`, `str()`, etc.

Estes são conceitos fundamentais que você usará em praticamente todos os programas que escrever. Continue praticando e explorando!

Se tiver dúvidas, revise o material e os exercícios. Até a próxima!
""")


