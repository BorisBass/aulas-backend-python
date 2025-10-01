# Exercícios Práticos: Estruturas Condicionais (if, elif, else)

# Exercício 1: Verificador de Idade para Votação
# Peça ao usuário para digitar sua idade. Se a idade for 18 ou mais, imprima "Você pode votar."
# Caso contrário, imprima "Você ainda não pode votar."

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode votar.")
else:
    print("Você ainda não pode votar.")

print("\n" + "-"*30 + "\n")

# Exercício 2: Classificador de Números
# Peça ao usuário para digitar um número. Verifique se o número é positivo, negativo ou zero.
# Imprima a classificação correspondente.

numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

print("\n" + "-"*30 + "\n")

# Exercício 3: Sistema de Notas
# Peça ao usuário para digitar uma nota (de 0 a 100). Classifique a nota em:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Abaixo de 60

nota = int(input("Digite a nota (0-100): "))

if nota >= 90:
    print("Conceito: A")
elif nota >= 80:
    print("Conceito: B")
elif nota >= 70:
    print("Conceito: C")
elif nota >= 60:
    print("Conceito: D")
else:
    print("Conceito: F")

print("\n" + "-"*30 + "\n")

# Exercício 4: Verificador de Par ou Ímpar
# Peça ao usuário para digitar um número inteiro. Verifique se o número é par ou ímpar.

numero_inteiro = int(input("Digite um número inteiro: "))

if numero_inteiro % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

print("\n" + "-"*30 + "\n")

# Exercício 5: Dia da Semana
# Peça ao usuário para digitar um número de 1 a 7. Imprima o dia da semana correspondente.
# Ex: 1 = Domingo, 2 = Segunda, etc.
# Se o número não estiver no intervalo, imprima "Número inválido."

dia = int(input("Digite um número de 1 a 7 para o dia da semana: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sábado")
else:
    print("Número inválido.")

print("\n" + "-"*30 + "\n")

# Exercício 6: Calculadora de Desconto
# Peça ao usuário o valor de uma compra e se ele possui um cupom de desconto (sim/não).
# Se o valor da compra for maior que R$100 e ele tiver um cupom, aplique 15% de desconto.
# Se o valor da compra for maior que R$50 e ele tiver um cupom, aplique 10% de desconto.
# Se ele não tiver cupom, não aplique desconto.
# Imprima o valor final da compra.

valor_compra = float(input("Digite o valor da compra: "))
possui_cupom = input("Você possui um cupom de desconto? (sim/não): ").lower()

valor_final = valor_compra

if possui_cupom == "sim":
    if valor_compra > 100:
        valor_final = valor_compra * 0.85  # 15% de desconto
        print("Desconto de 15% aplicado!")
    elif valor_compra > 50:
        valor_final = valor_compra * 0.90  # 10% de desconto
        print("Desconto de 10% aplicado!")
    else:
        print("Nenhum desconto aplicado com cupom para este valor de compra.")
else:
    print("Nenhum cupom de desconto aplicado.")

print(f"Valor final da compra: R${valor_final:.2f}")

print("\n" + "-"*30 + "\n")

# Exercício 7: Verificador de Ano Bissexto
# Peça ao usuário para digitar um ano. Verifique se o ano é bissexto.
# Um ano é bissexto se for divisível por 4, exceto se for divisível por 100 mas não por 400.

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

print("\n" + "-"*30 + "\n")

# Exercício 8: Jogo de Adivinhação Simples
# Gere um número secreto (fixo, por exemplo, 7). Peça ao usuário para adivinhar o número.
# Dê dicas se o número é maior ou menor, ou se ele acertou.

numero_secreto = 7

palpite = int(input("Adivinhe o número secreto (entre 1 e 10): "))

if palpite == numero_secreto:
    print("Parabéns! Você acertou o número secreto!")
elif palpite < numero_secreto:
    print("Seu palpite é muito baixo. Tente um número maior.")
else:
    print("Seu palpite é muito alto. Tente um número menor.")

print("\n" + "-"*30 + "\n")

# Exercício 9: Classificador de Triângulos
# Peça ao usuário para digitar o comprimento dos três lados de um triângulo.
# Classifique o triângulo como equilátero (todos os lados iguais),
# isósceles (dois lados iguais) ou escaleno (todos os lados diferentes).
# Considere também se os lados formam um triângulo válido (a soma de dois lados deve ser maior que o terceiro).

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print("É um triângulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Os lados fornecidos não formam um triângulo válido.")

print("\n" + "-"*30 + "\n")

# Exercício 10: Verificador de Faixa Etária
# Peça ao usuário para digitar sua idade. Com base na idade, imprima a faixa etária:
# Bebê (0-1 ano)
# Criança (2-12 anos)
# Adolescente (13-17 anos)
# Adulto (18-64 anos)
# Idoso (65+ anos)

idade_faixa = int(input("Digite sua idade para verificar a faixa etária: "))

if idade_faixa >= 0 and idade_faixa <= 1:
    print("Faixa etária: Bebê")
elif idade_faixa >= 2 and idade_faixa <= 12:
    print("Faixa etária: Criança")
elif idade_faixa >= 13 and idade_faixa <= 17:
    print("Faixa etária: Adolescente")
elif idade_faixa >= 18 and idade_faixa <= 64:
    print("Faixa etária: Adulto")
elif idade_faixa >= 65:
    print("Faixa etária: Idoso")
else:
    print("Idade inválida.")

print("\n" + "-"*30 + "\n")


