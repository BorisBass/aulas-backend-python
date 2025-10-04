"""
# Plano de Aula: Operadores Aritméticos, Relacionais e Lógicos em Python

## Duração: 3 horas

## Público-alvo: Iniciantes em Programação

## Objetivo Geral:
Ao final desta aula, os alunos serão capazes de compreender e aplicar os diferentes tipos de operadores em Python (aritméticos, relacionais e lógicos) para realizar cálculos, comparações e construir expressões complexas.

## Conteúdo Programático:

### 1. Introdução aos Operadores (15 minutos)
- Boas-vindas e apresentação da aula.
- O que são operadores e sua importância na programação.
- Revisão rápida de variáveis e tipos de dados.

### 2. Operadores Aritméticos (60 minutos)
- Adição (`+`)
- Subtração (`-`)
- Multiplicação (`*`)
- Divisão (`/`)
- Divisão Inteira (`//`)
- Módulo (`%`)
- Exponenciação (`**`)
- Exemplos práticos e demonstrações no Google Colab.
- Exercícios práticos.

### 3. Operadores Relacionais (60 minutos)
- Igual a (`==`)
- Diferente de (`!=`)
- Maior que (`>`)
- Menor que (`<`)
- Maior ou igual a (`>=`)
- Menor ou igual a (`<=`)
- Retorno booleano dos operadores relacionais.
- Exemplos práticos e demonstrações no Google Colab.
- Exercícios práticos.

### 4. Operadores Lógicos (45 minutos)
- E (`and`)
- Ou (`or`)
- Não (`not`)
- Tabelas verdade.
- Combinação de operadores lógicos e relacionais.
- Exemplos práticos e demonstrações no Google Colab.
- Exercícios práticos.

### 5. Precedência e Associação de Operadores (30 minutos)
- Ordem de execução dos operadores.
- Uso de parênteses para alterar a precedência.
- Associação de operadores (esquerda para direita, direita para esquerda).
- Exercícios práticos.

### 6. Revisão e Perguntas (15 minutos)
- Resumo dos principais conceitos abordados.
- Espaço para dúvidas e esclarecimentos.

## Metodologia:
- Aula expositiva com apresentação de slides.
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
# Aula: Operadores Aritméticos, Relacionais e Lógicos em Python

Bem-vindos à nossa aula sobre operadores em Python! Hoje, vamos explorar os diferentes tipos de operadores que são fundamentais para realizar cálculos, comparações e construir expressões lógicas complexas.

## Objetivo da Aula
Ao final desta aula, você será capaz de:

*   Compreender e utilizar operadores aritméticos para realizar cálculos matemáticos.
*   Aplicar operadores relacionais para fazer comparações entre valores.
*   Usar operadores lógicos para construir expressões booleanas complexas.
*   Entender a precedência e associação de operadores para escrever expressões corretas.

Vamos começar!
""")

print("""
## 1. Operadores Aritméticos

Os operadores aritméticos são usados para realizar operações matemáticas básicas em Python.

### Lista dos Operadores Aritméticos:
- `+` : Adição
- `-` : Subtração
- `*` : Multiplicação
- `/` : Divisão (retorna float)
- `//` : Divisão inteira (retorna apenas a parte inteira)
- `%` : Módulo (retorna o resto da divisão)
- `**` : Exponenciação (potência)

Vamos ver alguns exemplos:
""")

# Exemplos de operadores aritméticos
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Adição: {a} + {b} = {a + b}")
print(f"Subtração: {a} - {b} = {a - b}")
print(f"Multiplicação: {a} * {b} = {a * b}")
print(f"Divisão: {a} / {b} = {a / b}")
print(f"Divisão inteira: {a} // {b} = {a // b}")
print(f"Módulo: {a} % {b} = {a % b}")
print(f"Exponenciação: {a} ** {b} = {a ** b}")

print("""
### Exercício A1: Calculadora Básica
Peça ao usuário para digitar dois números e realize todas as operações aritméticas.
""")

# Exercício A1
num1_a1 = float(input("Digite o primeiro número: "))
num2_a1 = float(input("Digite o segundo número: "))

print(f"\nResultados para {num1_a1} e {num2_a1}:")
print(f"Soma: {num1_a1 + num2_a1}")
print(f"Subtração: {num1_a1 - num2_a1}")
print(f"Multiplicação: {num1_a1 * num2_a1}")

if num2_a1 != 0:
    print(f"Divisão: {num1_a1 / num2_a1}")
    print(f"Divisão inteira: {num1_a1 // num2_a1}")
    print(f"Módulo: {num1_a1 % num2_a1}")
else:
    print("Divisão por zero não é permitida.")

print(f"Exponenciação: {num1_a1 ** num2_a1}")

print("""
### Exercício A2: Cálculo de Área e Perímetro
Peça ao usuário as dimensões de um retângulo e calcule a área e o perímetro.
""")

# Exercício A2
largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area = largura * altura
perimetro = 2 * (largura + altura)

print(f"Área do retângulo: {area}")
print(f"Perímetro do retângulo: {perimetro}")

print("""
---

## 2. Operadores Relacionais

Os operadores relacionais são usados para comparar valores. Eles sempre retornam um valor booleano (True ou False).

### Lista dos Operadores Relacionais:
- `==` : Igual a
- `!=` : Diferente de
- `>` : Maior que
- `<` : Menor que
- `>=` : Maior ou igual a
- `<=` : Menor ou igual a

Vamos ver alguns exemplos:
""")

# Exemplos de operadores relacionais
x = 5
y = 8

print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}")

print("""
### Exercício R1: Comparação de Idades
Peça a idade de duas pessoas e compare-as usando todos os operadores relacionais.
""")

# Exercício R1
idade1 = int(input("Digite a idade da primeira pessoa: "))
idade2 = int(input("Digite a idade da segunda pessoa: "))

print(f"\nComparações entre {idade1} e {idade2}:")
print(f"Idades são iguais: {idade1 == idade2}")
print(f"Idades são diferentes: {idade1 != idade2}")
print(f"Primeira pessoa é mais velha: {idade1 > idade2}")
print(f"Primeira pessoa é mais nova: {idade1 < idade2}")
print(f"Primeira pessoa tem idade maior ou igual: {idade1 >= idade2}")
print(f"Primeira pessoa tem idade menor ou igual: {idade1 <= idade2}")

print("""
### Exercício R2: Verificação de Aprovação
Peça a nota de um aluno e verifique se ele foi aprovado (nota >= 7.0).
""")

# Exercício R2
nota = float(input("Digite a nota do aluno: "))
aprovado = nota >= 7.0

print(f"Nota: {nota}")
print(f"Aluno aprovado: {aprovado}")

if aprovado:
    print("Parabéns! Você foi aprovado!")
else:
    print("Infelizmente, você não foi aprovado. Continue estudando!")

print("""
---

## 3. Operadores Lógicos

Os operadores lógicos são usados para combinar expressões booleanas.

### Lista dos Operadores Lógicos:
- `and` : E lógico (retorna True se ambas as condições forem True)
- `or` : Ou lógico (retorna True se pelo menos uma condição for True)
- `not` : Não lógico (inverte o valor booleano)

### Tabelas Verdade:

**Operador AND:**
- True and True = True
- True and False = False
- False and True = False
- False and False = False

**Operador OR:**
- True or True = True
- True or False = True
- False or True = True
- False or False = False

**Operador NOT:**
- not True = False
- not False = True

Vamos ver alguns exemplos:
""")

# Exemplos de operadores lógicos
p = True
q = False

print(f"p = {p}, q = {q}")
print(f"p and q: {p and q}")
print(f"p or q: {p or q}")
print(f"not p: {not p}")
print(f"not q: {not q}")

# Exemplos com expressões
idade_exemplo = 20
tem_carteira = True

print(f"\nExemplo prático:")
print(f"Idade: {idade_exemplo}, Tem carteira: {tem_carteira}")
print(f"Pode dirigir (idade >= 18 AND tem carteira): {idade_exemplo >= 18 and tem_carteira}")

print("""
### Exercício L1: Sistema de Acesso
Peça ao usuário se ele tem senha correta e se tem permissão de administrador. 
Verifique se ele pode acessar o sistema (precisa ter senha correta E permissão de admin).
""")

# Exercício L1
senha_correta = input("A senha está correta? (sim/não): ").lower() == 'sim'
eh_admin = input("Você tem permissão de administrador? (sim/não): ").lower() == 'sim'

pode_acessar = senha_correta and eh_admin

print(f"\nSenha correta: {senha_correta}")
print(f"É administrador: {eh_admin}")
print(f"Pode acessar o sistema: {pode_acessar}")

print("""
### Exercício L2: Desconto na Loja
Uma loja oferece desconto se o cliente for estudante OU se a compra for acima de R$ 100.
Peça essas informações e verifique se o cliente tem direito ao desconto.
""")

# Exercício L2
eh_estudante = input("Você é estudante? (sim/não): ").lower() == 'sim'
valor_compra = float(input("Digite o valor da compra: R$ "))

tem_desconto = eh_estudante or valor_compra > 100

print(f"\nÉ estudante: {eh_estudante}")
print(f"Valor da compra: R$ {valor_compra}")
print(f"Tem direito ao desconto: {tem_desconto}")

print("""
---

## 4. Precedência e Associação de Operadores

A precedência determina a ordem em que os operadores são avaliados em uma expressão.

### Ordem de Precedência (do maior para o menor):
1. `**` (Exponenciação)
2. `+x`, `-x`, `not x` (Operadores unários)
3. `*`, `/`, `//`, `%` (Multiplicação, divisão, divisão inteira, módulo)
4. `+`, `-` (Adição, subtração)
5. `==`, `!=`, `<`, `<=`, `>`, `>=` (Operadores relacionais)
6. `and` (E lógico)
7. `or` (Ou lógico)

### Exemplos de Precedência:
""")

# Exemplos de precedência
print("Exemplos de precedência:")
print(f"5 + 3 * 2 = {5 + 3 * 2}")  # Multiplicação primeiro: 5 + 6 = 11
print(f"(5 + 3) * 2 = {(5 + 3) * 2}")  # Parênteses alteram a precedência: 8 * 2 = 16
print(f"2 ** 3 ** 2 = {2 ** 3 ** 2}")  # Exponenciação é associativa à direita: 2 ** (3 ** 2) = 2 ** 9 = 512
print(f"10 > 5 and 3 < 7 = {10 > 5 and 3 < 7}")  # Relacionais primeiro, depois and

print("""
### Exercício P1: Expressões Complexas
Calcule o resultado das seguintes expressões e explique a ordem de avaliação:
""")

# Exercício P1
expr1 = 2 + 3 * 4 ** 2
expr2 = (2 + 3) * 4 ** 2
expr3 = 2 + 3 * 4 ** 2 - 1

print(f"2 + 3 * 4 ** 2 = {expr1}")
print("Ordem: 4 ** 2 = 16, depois 3 * 16 = 48, depois 2 + 48 = 50")

print(f"(2 + 3) * 4 ** 2 = {expr2}")
print("Ordem: (2 + 3) = 5, depois 4 ** 2 = 16, depois 5 * 16 = 80")

print(f"2 + 3 * 4 ** 2 - 1 = {expr3}")
print("Ordem: 4 ** 2 = 16, depois 3 * 16 = 48, depois 2 + 48 = 50, depois 50 - 1 = 49")

print("""
### Exercício P2: Condições Complexas
Peça a idade e a renda de uma pessoa. Verifique se ela pode obter um empréstimo:
- Idade entre 18 e 65 anos E renda maior que R$ 2000
""")

# Exercício P2
idade_emprestimo = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda mensal: R$ "))

pode_emprestimo = (idade_emprestimo >= 18 and idade_emprestimo <= 65) and renda > 2000

print(f"\nIdade: {idade_emprestimo}")
print(f"Renda: R$ {renda}")
print(f"Pode obter empréstimo: {pode_emprestimo}")

# Vamos quebrar a condição para entender melhor
idade_valida = idade_emprestimo >= 18 and idade_emprestimo <= 65
renda_valida = renda > 2000

print(f"\nDetalhamento:")
print(f"Idade válida (18-65): {idade_valida}")
print(f"Renda válida (> R$ 2000): {renda_valida}")
print(f"Ambas as condições: {idade_valida and renda_valida}")

print("""
---

## Exercícios Extras para Prática

### Exercício Extra 1: Calculadora de IMC
Peça o peso e altura de uma pessoa, calcule o IMC e classifique:
- IMC < 18.5: Abaixo do peso
- 18.5 <= IMC < 25: Peso normal
- 25 <= IMC < 30: Sobrepeso
- IMC >= 30: Obesidade
""")

# Exercício Extra 1
peso = float(input("Digite seu peso (kg): "))
altura_imc = float(input("Digite sua altura (m): "))

imc = peso / (altura_imc ** 2)

print(f"\nSeu IMC é: {imc:.2f}")

# Classificação usando operadores relacionais e lógicos
abaixo_peso = imc < 18.5
peso_normal = imc >= 18.5 and imc < 25
sobrepeso = imc >= 25 and imc < 30
obesidade = imc >= 30

print("Classificação:")
if abaixo_peso:
    print("Abaixo do peso")
elif peso_normal:
    print("Peso normal")
elif sobrepeso:
    print("Sobrepeso")
elif obesidade:
    print("Obesidade")

print("""
### Exercício Extra 2: Sistema de Notas
Peça 3 notas de um aluno, calcule a média e determine:
- Se foi aprovado (média >= 7.0)
- Se ficou em recuperação (5.0 <= média < 7.0)
- Se foi reprovado (média < 5.0)
""")

# Exercício Extra 2
nota1_extra = float(input("Digite a primeira nota: "))
nota2_extra = float(input("Digite a segunda nota: "))
nota3_extra = float(input("Digite a terceira nota: "))

media_extra = (nota1_extra + nota2_extra + nota3_extra) / 3

print(f"\nNotas: {nota1_extra}, {nota2_extra}, {nota3_extra}")
print(f"Média: {media_extra:.2f}")

aprovado_extra = media_extra >= 7.0
recuperacao = media_extra >= 5.0 and media_extra < 7.0
reprovado = media_extra < 5.0

print("Situação:")
if aprovado_extra:
    print("Aprovado!")
elif recuperacao:
    print("Recuperação")
elif reprovado:
    print("Reprovado")

print("""
---

## Conclusão

Parabéns! Você concluiu a aula sobre operadores em Python. Hoje, você aprendeu sobre:

*   **Operadores Aritméticos:** Para realizar cálculos matemáticos (+, -, *, /, //, %, **)
*   **Operadores Relacionais:** Para fazer comparações (==, !=, >, <, >=, <=)
*   **Operadores Lógicos:** Para construir expressões booleanas (and, or, not)
*   **Precedência e Associação:** Para entender a ordem de avaliação das expressões

Estes operadores são fundamentais para construir programas mais complexos e tomar decisões baseadas em condições. Continue praticando com diferentes combinações de operadores!

### Próximos Passos:
- Pratique criando expressões mais complexas
- Combine operadores diferentes em uma única expressão
- Use parênteses para controlar a precedência quando necessário
- Experimente com diferentes tipos de dados

Se tiver dúvidas, revise o material e os exercícios. Até a próxima aula!
""")

