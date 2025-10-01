# Exercícios Práticos: Estruturas de Repetição (while, for)

# Exercício 1: Contagem Regressiva
# Crie um programa que faça uma contagem regressiva de 10 até 1, e então imprima "Lançamento!".

print("Exercício 1: Contagem Regressiva")
print("-" * 30)

# Solução:
for i in range(10, 0, -1):
    print(i)
print("Lançamento!")

print("\n" + "=" * 50 + "\n")

# Exercício 2: Soma de Números
# Escreva um programa que calcule a soma de todos os números de 1 a 100 usando um laço while.

print("Exercício 2: Soma de Números")
print("-" * 30)

# Solução:
soma = 0
contador = 1

while contador <= 100:
    soma += contador
    contador += 1

print(f"A soma dos números de 1 a 100 é: {soma}")

print("\n" + "=" * 50 + "\n")

# Exercício 3: Tabuada
# Crie um programa que imprima a tabuada de um número fornecido pelo usuário, de 1 a 10.

print("Exercício 3: Tabuada")
print("-" * 30)

# Solução:
numero = int(input("Digite um número para ver sua tabuada: "))

print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

print("\n" + "=" * 50 + "\n")

# Exercício 4: Encontrar Números Primos
# Escreva um programa que encontre todos os números primos entre 1 e 50 usando laços aninhados.

print("Exercício 4: Encontrar Números Primos")
print("-" * 30)

# Solução:
print("Números primos entre 1 e 50:")
for num in range(2, 51):
    eh_primo = True
    for i in range(2, num):
        if num % i == 0:
            eh_primo = False
            break
    
    if eh_primo:
        print(num, end=" ")

print("\n\n" + "=" * 50 + "\n")

# Exercício 5: Padrão de Asteriscos
# Crie um programa que imprima um padrão de asteriscos como mostrado abaixo:
# *
# **
# ***
# ****
# *****

print("Exercício 5: Padrão de Asteriscos")
print("-" * 30)

# Solução:
for i in range(1, 6):
    print("*" * i)

print("\n" + "=" * 50 + "\n")

# Exercício 6: Adivinhe o Número
# Crie um jogo onde o computador escolhe um número entre 1 e 100, e o usuário tenta adivinhar.
# O programa deve informar se o palpite é maior ou menor que o número escolhido.

print("Exercício 6: Adivinhe o Número")
print("-" * 30)

# Solução:
import random

numero_secreto = random.randint(1, 100)
tentativas = 0
max_tentativas = 10

print("Bem-vindo ao jogo de adivinhação!")
print(f"Tente adivinhar o número entre 1 e 100. Você tem {max_tentativas} tentativas.")

while tentativas < max_tentativas:
    palpite = int(input("\nDigite seu palpite: "))
    tentativas += 1
    
    if palpite < numero_secreto:
        print("Tente um número MAIOR!")
    elif palpite > numero_secreto:
        print("Tente um número MENOR!")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas!")
        break
        
    print(f"Tentativas restantes: {max_tentativas - tentativas}")
    
if tentativas == max_tentativas and palpite != numero_secreto:
    print(f"\nSuas tentativas acabaram! O número secreto era {numero_secreto}.")

print("\n" + "=" * 50 + "\n")

# Exercício 7: Calculadora de Fatorial
# Crie um programa que calcule o fatorial de um número fornecido pelo usuário.
# Lembre-se: O fatorial de um número n é o produto de todos os inteiros positivos menores ou iguais a n.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

print("Exercício 7: Calculadora de Fatorial")
print("-" * 30)

# Solução:
numero = int(input("Digite um número para calcular seu fatorial: "))

if numero < 0:
    print("Não existe fatorial de número negativo!")
elif numero == 0:
    print("O fatorial de 0 é 1")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    
    print(f"O fatorial de {numero} é {fatorial}")

print("\n" + "=" * 50 + "\n")

# Exercício 8: Fibonacci
# Crie um programa que gere os primeiros n termos da sequência de Fibonacci.
# A sequência começa com 0 e 1, e cada termo subsequente é a soma dos dois anteriores.
# Exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

print("Exercício 8: Sequência de Fibonacci")
print("-" * 30)

# Solução:
n = int(input("Quantos termos da sequência de Fibonacci você deseja gerar? "))

a, b = 0, 1
contador = 0

if n <= 0:
    print("Por favor, insira um número positivo!")
elif n == 1:
    print("Sequência de Fibonacci até o termo", n, ":")
    print(a)
else:
    print("Sequência de Fibonacci:")
    while contador < n:
        print(a, end=" ")
        c = a + b
        # Atualizando valores
        a = b
        b = c
        contador += 1

print("\n\n" + "=" * 50 + "\n")

# Exercício 9: Validação de Entrada
# Crie um programa que solicite ao usuário uma senha. O programa deve continuar
# pedindo a senha até que o usuário digite "python123".

print("Exercício 9: Validação de Entrada")
print("-" * 30)

# Solução:
senha_correta = "python123"

while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Senha correta! Acesso concedido.")
        break
    else:
        print("Senha incorreta. Tente novamente.")

print("\n" + "=" * 50 + "\n")

# Exercício 10: Média de Notas
# Crie um programa que solicite ao usuário quantas notas ele deseja inserir,
# depois peça cada nota e calcule a média.

print("Exercício 10: Média de Notas")
print("-" * 30)

# Solução:
quantidade = int(input("Quantas notas você deseja inserir? "))

if quantidade <= 0:
    print("Quantidade inválida!")
else:
    soma = 0
    for i in range(1, quantidade + 1):
        nota = float(input(f"Digite a {i}ª nota: "))
        soma += nota
    
    media = soma / quantidade
    print(f"\nA média das {quantidade} notas é: {media:.2f}")

print("\n" + "=" * 50 + "\n")

print("Fim dos exercícios! Continue praticando para aprimorar suas habilidades em Python!")

