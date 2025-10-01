# Exercícios Práticos para Google Colab

## Variáveis, Tipos de Dados e Entrada de Dados em Python

Estes exercícios foram desenvolvidos para serem executados no Google Colab. Copie e cole cada bloco de código em uma célula do Colab e execute-o para ver o resultado.

---

### Exercício 1: Identificação de Tipos de Dados

**Objetivo:** Praticar a identificação dos tipos de dados primitivos em Python.

**Instruções:** Para cada variável abaixo, adicione um comentário indicando qual é o seu tipo de dado (int, float, str, bool).

```python
# Variável 1
idade = 30
# Tipo: 

# Variável 2
preco = 19.99
# Tipo: 

# Variável 3
nome = "Maria"
# Tipo: 

# Variável 4
is_estudante = True
# Tipo: 

# Variável 5
numero_grande = 1000000
# Tipo: 

# Variável 6
temperatura = -5.5
# Tipo: 

# Variável 7
mensagem = "Olá, mundo!"
# Tipo: 

# Variável 8
tem_desconto = False
# Tipo: 
```

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

```python
# Seu código aqui

```

---

### Exercício 3: Entrada e Saída de Dados

**Objetivo:** Utilizar as funções `input()` e `print()` para interagir com o usuário.

**Instruções:**
1. Peça ao usuário para digitar seu nome e armazene-o em uma variável `seu_nome`.
2. Peça ao usuário para digitar sua idade e armazene-a em uma variável `sua_idade`.
3. Usando f-strings, imprima uma mensagem personalizada que inclua o nome e a idade digitados pelo usuário.
   Exemplo: "Olá, [seu_nome]! Você tem [sua_idade] anos."

```python
# Seu código aqui

```

---

### Exercício 4: Casting de Dados

**Objetivo:** Praticar a conversão de tipos de dados (casting).

**Instruções:**
1. Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis (lembre-se que `input()` retorna string).
2. Converta essas strings para números inteiros.
3. Calcule a soma, subtração, multiplicação e divisão desses dois números.
4. Imprima os resultados de cada operação, indicando qual operação foi realizada.

```python
# Seu código aqui

```

---

### Exercício 5: Desafio Combinado

**Objetivo:** Combinar os conceitos de variáveis, entrada/saída e casting.

**Instruções:**
1. Peça ao usuário para digitar o preço de um produto e a quantidade comprada.
2. Calcule o valor total da compra.
3. Peça ao usuário para digitar o valor pago.
4. Calcule o troco.
5. Imprima o valor total da compra e o troco de forma formatada.

```python
# Seu código aqui

```




---

### Exercício Extra: Calculadora Simples

**Objetivo:** Criar uma calculadora simples que receba dois números e uma operação, e exiba o resultado.

**Instruções:**
1. Peça ao usuário para digitar o primeiro número.
2. Peça ao usuário para digitar o segundo número.
3. Peça ao usuário para digitar a operação desejada (ex: '+', '-', '*', '/').
4. Realize a operação e imprima o resultado. Lembre-se de converter os números para o tipo correto antes de realizar a operação.

```python
# Seu código aqui

```
```




---

### Exercício 6: Conversão de Temperatura

**Objetivo:** Converter uma temperatura de Celsius para Fahrenheit usando casting.

**Instruções:**
1. Peça ao usuário para digitar uma temperatura em Celsius (número decimal).
2. Converta a entrada para o tipo `float`.
3. Calcule a temperatura em Fahrenheit usando a fórmula: `Fahrenheit = (Celsius * 9/5) + 32`.
4. Imprima o resultado formatado com duas casas decimais.

```python
# Seu código aqui

```

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

```python
# Seu código aqui

```

---

### Exercício 8: Soma Segura de Números

**Objetivo:** Receber dois números do usuário e somá-los, tratando possíveis erros de conversão.

**Instruções:**
1. Peça ao usuário para digitar o primeiro número.
2. Peça ao usuário para digitar o segundo número.
3. Tente converter ambos para `float` e some-os.
4. Se a conversão falhar (por exemplo, se o usuário digitar texto), imprima uma mensagem de erro amigável. (Dica: use um bloco `try-except` se já tiver aprendido, caso contrário, apenas comente sobre o erro).
5. Imprima o resultado da soma ou a mensagem de erro.

```python
# Seu código aqui

```


