# BEP-008: Exercícios de Funções em Python
# Google Colab - Exercícios Práticos

print("=" * 60)
print("BEP-008: EXERCÍCIOS DE FUNÇÕES EM PYTHON")
print("=" * 60)
print()

# =============================================================================
# EXERCÍCIO 1: FUNÇÕES BÁSICAS
# =============================================================================
print("EXERCÍCIO 1: FUNÇÕES BÁSICAS")
print("-" * 40)

# 1.1 Crie uma função chamada 'cumprimentar' que imprima "Olá, mundo!"
def cumprimentar():
    print("Olá, mundo!")

# Teste a função
print("Chamando a função cumprimentar():")
cumprimentar()
print()

# 1.2 Crie uma função chamada 'despedir' que imprima "Até logo!"
def despedir():
    print("Até logo!")

# Teste a função
print("Chamando a função despedir():")
despedir()
print()

# 1.3 Crie uma função chamada 'mostrar_data' que imprima a data atual
# (Use apenas print com texto fixo por enquanto)
def mostrar_data():
    print("Data: 15/03/2024")

# Teste a função
print("Chamando a função mostrar_data():")
mostrar_data()
print()

# =============================================================================
# EXERCÍCIO 2: FUNÇÕES COM PARÂMETROS
# =============================================================================
print("EXERCÍCIO 2: FUNÇÕES COM PARÂMETROS")
print("-" * 40)

# 2.1 Crie uma função 'cumprimentar_pessoa' que receba um nome e imprima
# "Olá, [nome]!"
def cumprimentar_pessoa(nome):
    print(f"Olá, {nome}!")

# Teste a função
print("Testando cumprimentar_pessoa:")
cumprimentar_pessoa("João")
cumprimentar_pessoa("Maria")
print()

# 2.2 Crie uma função 'calcular_dobro' que receba um número e imprima o dobro
def calcular_dobro(numero):
    dobro = numero * 2
    print(f"O dobro de {numero} é {dobro}")

# Teste a função
print("Testando calcular_dobro:")
calcular_dobro(5)
calcular_dobro(10)
print()

# 2.3 Crie uma função 'somar' que receba dois números e imprima a soma
def somar(a, b):
    resultado = a + b
    print(f"{a} + {b} = {resultado}")

# Teste a função
print("Testando somar:")
somar(3, 7)
somar(15, 25)
print()

# =============================================================================
# EXERCÍCIO 3: FUNÇÕES COM RETORNO
# =============================================================================
print("EXERCÍCIO 3: FUNÇÕES COM RETORNO")
print("-" * 40)

# 3.1 Crie uma função 'calcular_quadrado' que receba um número e retorne o quadrado
def calcular_quadrado(numero):
    return numero * numero

# Teste a função
print("Testando calcular_quadrado:")
resultado1 = calcular_quadrado(4)
print(f"O quadrado de 4 é {resultado1}")

resultado2 = calcular_quadrado(7)
print(f"O quadrado de 7 é {resultado2}")
print()

# 3.2 Crie uma função 'calcular_media' que receba três números e retorne a média
def calcular_media(a, b, c):
    soma = a + b + c
    media = soma / 3
    return media

# Teste a função
print("Testando calcular_media:")
media1 = calcular_media(8, 9, 7)
print(f"A média de 8, 9 e 7 é {media1:.2f}")

media2 = calcular_media(10, 10, 10)
print(f"A média de 10, 10 e 10 é {media2:.2f}")
print()

# 3.3 Crie uma função 'verificar_par' que receba um número e retorne True se for par
def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Teste a função
print("Testando verificar_par:")
print(f"4 é par? {verificar_par(4)}")
print(f"7 é par? {verificar_par(7)}")
print(f"10 é par? {verificar_par(10)}")
print()

# =============================================================================
# EXERCÍCIO 4: FUNÇÕES COM VALORES PADRÃO
# =============================================================================
print("EXERCÍCIO 4: FUNÇÕES COM VALORES PADRÃO")
print("-" * 40)

# 4.1 Crie uma função 'multiplicar' que receba dois números, sendo o segundo opcional
# Se o segundo número não for fornecido, use 2 como padrão
def multiplicar(a, b=2):
    return a * b

# Teste a função
print("Testando multiplicar:")
print(f"multiplicar(5, 3) = {multiplicar(5, 3)}")
print(f"multiplicar(5) = {multiplicar(5)}")  # Usa valor padrão
print(f"multiplicar(10) = {multiplicar(10)}")  # Usa valor padrão
print()

# 4.2 Crie uma função 'cumprimentar_formal' que receba um nome e um título
# O título deve ser "Sr." por padrão
def cumprimentar_formal(nome, titulo="Sr."):
    return f"Olá, {titulo} {nome}!"

# Teste a função
print("Testando cumprimentar_formal:")
print(cumprimentar_formal("João"))
print(cumprimentar_formal("Maria", "Sra."))
print(cumprimentar_formal("Pedro", "Dr."))
print()

# =============================================================================
# EXERCÍCIO 5: FUNÇÕES COM MÚLTIPLOS RETORNOS
# =============================================================================
print("EXERCÍCIO 5: FUNÇÕES COM MÚLTIPLOS RETORNOS")
print("-" * 40)

# 5.1 Crie uma função 'calcular_estatisticas' que receba uma lista de números
# e retorne a soma, média e maior valor
def calcular_estatisticas(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    maior = max(numeros)
    return soma, media, maior

# Teste a função
print("Testando calcular_estatisticas:")
lista1 = [1, 2, 3, 4, 5]
soma, media, maior = calcular_estatisticas(lista1)
print(f"Lista: {lista1}")
print(f"Soma: {soma}")
print(f"Média: {media:.2f}")
print(f"Maior: {maior}")
print()

# 5.2 Crie uma função 'verificar_triangulo' que receba três lados e retorne
# se é um triângulo válido e seu tipo
def verificar_triangulo(a, b, c):
    # Verificar se é um triângulo válido
    if a + b > c and a + c > b and b + c > a:
        # Determinar o tipo
        if a == b == c:
            tipo = "equilátero"
        elif a == b or a == c or b == c:
            tipo = "isósceles"
        else:
            tipo = "escaleno"
        return True, tipo
    else:
        return False, "inválido"

# Teste a função
print("Testando verificar_triangulo:")
valido1, tipo1 = verificar_triangulo(3, 4, 5)
print(f"Triângulo 3, 4, 5: {valido1}, tipo: {tipo1}")

valido2, tipo2 = verificar_triangulo(5, 5, 5)
print(f"Triângulo 5, 5, 5: {valido2}, tipo: {tipo2}")

valido3, tipo3 = verificar_triangulo(1, 2, 5)
print(f"Triângulo 1, 2, 5: {valido3}, tipo: {tipo3}")
print()

# =============================================================================
# EXERCÍCIO 6: FUNÇÕES COM LISTAS
# =============================================================================
print("EXERCÍCIO 6: FUNÇÕES COM LISTAS")
print("-" * 40)

# 6.1 Crie uma função 'encontrar_maior' que receba uma lista e retorne o maior elemento
def encontrar_maior(lista):
    if not lista:  # Se a lista estiver vazia
        return None
    
    maior = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior

# Teste a função
print("Testando encontrar_maior:")
lista_numeros = [15, 8, 23, 4, 42, 7]
maior_numero = encontrar_maior(lista_numeros)
print(f"Lista: {lista_numeros}")
print(f"Maior número: {maior_numero}")
print()

# 6.2 Crie uma função 'contar_pares' que receba uma lista e retorne quantos números pares existem
def contar_pares(lista):
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
            contador += 1
    return contador

# Teste a função
print("Testando contar_pares:")
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quantidade_pares = contar_pares(lista_numeros)
print(f"Lista: {lista_numeros}")
print(f"Quantidade de números pares: {quantidade_pares}")
print()

# =============================================================================
# EXERCÍCIO 7: FUNÇÕES COM DICIONÁRIOS
# =============================================================================
print("EXERCÍCIO 7: FUNÇÕES COM DICIONÁRIOS")
print("-" * 40)

# 7.1 Crie uma função 'calcular_media_aluno' que receba um dicionário com notas
# e retorne a média do aluno
def calcular_media_aluno(notas):
    soma = sum(notas.values())
    media = soma / len(notas)
    return media

# Teste a função
print("Testando calcular_media_aluno:")
notas_joao = {"matematica": 8.5, "portugues": 7.0, "ciencias": 9.2}
media_joao = calcular_media_aluno(notas_joao)
print(f"Notas do João: {notas_joao}")
print(f"Média do João: {media_joao:.2f}")
print()

# 7.2 Crie uma função 'verificar_aprovacao' que receba um dicionário com notas
# e retorne se o aluno foi aprovado (média >= 7.0)
def verificar_aprovacao(notas):
    media = calcular_media_aluno(notas)
    if media >= 7.0:
        return True, media
    else:
        return False, media

# Teste a função
print("Testando verificar_aprovacao:")
aprovado1, media1 = verificar_aprovacao(notas_joao)
print(f"João foi aprovado? {aprovado1} (média: {media1:.2f})")

notas_maria = {"matematica": 6.0, "portugues": 5.5, "ciencias": 6.8}
aprovado2, media2 = verificar_aprovacao(notas_maria)
print(f"Maria foi aprovada? {aprovado2} (média: {media2:.2f})")
print()

# =============================================================================
# EXERCÍCIO 8: FUNÇÕES COM ESTRUTURAS CONDICIONAIS
# =============================================================================
print("EXERCÍCIO 8: FUNÇÕES COM ESTRUTURAS CONDICIONAIS")
print("-" * 40)

# 8.1 Crie uma função 'classificar_idade' que receba uma idade e retorne a classificação
def classificar_idade(idade):
    if idade < 0:
        return "idade inválida"
    elif idade < 13:
        return "criança"
    elif idade < 20:
        return "adolescente"
    elif idade < 60:
        return "adulto"
    else:
        return "idoso"

# Teste a função
print("Testando classificar_idade:")
idades = [5, 15, 25, 65, -1]
for idade in idades:
    classificacao = classificar_idade(idade)
    print(f"Idade {idade}: {classificacao}")
print()

# 8.2 Crie uma função 'calcular_desconto' que receba o valor da compra e o tipo de cliente
# e retorne o valor com desconto
def calcular_desconto(valor, tipo_cliente):
    if tipo_cliente == "vip":
        desconto = 0.20  # 20% de desconto
    elif tipo_cliente == "premium":
        desconto = 0.15  # 15% de desconto
    elif tipo_cliente == "regular":
        desconto = 0.05  # 5% de desconto
    else:
        desconto = 0  # Sem desconto
    
    valor_desconto = valor * desconto
    valor_final = valor - valor_desconto
    return valor_final, valor_desconto

# Teste a função
print("Testando calcular_desconto:")
compras = [
    (100, "vip"),
    (200, "premium"),
    (150, "regular"),
    (300, "novo")
]

for valor, tipo in compras:
    valor_final, desconto = calcular_desconto(valor, tipo)
    print(f"Compra R$ {valor} ({tipo}): R$ {valor_final:.2f} (desconto: R$ {desconto:.2f})")
print()

# =============================================================================
# EXERCÍCIO 9: FUNÇÕES COM ESTRUTURAS DE REPETIÇÃO
# =============================================================================
print("EXERCÍCIO 9: FUNÇÕES COM ESTRUTURAS DE REPETIÇÃO")
print("-" * 40)

# 9.1 Crie uma função 'gerar_tabuada' que receba um número e imprima sua tabuada
def gerar_tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Teste a função
print("Testando gerar_tabuada:")
gerar_tabuada(5)
print()

# 9.2 Crie uma função 'calcular_fatorial' que receba um número e retorne o fatorial
def calcular_fatorial(numero):
    if numero < 0:
        return None
    elif numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, numero + 1):
            fatorial *= i
        return fatorial

# Teste a função
print("Testando calcular_fatorial:")
numeros = [0, 1, 5, 7, -1]
for num in numeros:
    resultado = calcular_fatorial(num)
    if resultado is not None:
        print(f"Fatorial de {num}: {resultado}")
    else:
        print(f"Fatorial de {num}: não definido")
print()

# =============================================================================
# EXERCÍCIO 10: PROJETO INTEGRADOR - CALCULADORA
# =============================================================================
print("EXERCÍCIO 10: PROJETO INTEGRADOR - CALCULADORA")
print("-" * 40)

# 10.1 Crie uma função 'somar' que receba dois números e retorne a soma
def somar(a, b):
    return a + b

# 10.2 Crie uma função 'subtrair' que receba dois números e retorne a subtração
def subtrair(a, b):
    return a - b

# 10.3 Crie uma função 'multiplicar' que receba dois números e retorne a multiplicação
def multiplicar(a, b):
    return a * b

# 10.4 Crie uma função 'dividir' que receba dois números e retorne a divisão
def dividir(a, b):
    if b == 0:
        return None  # Divisão por zero
    return a / b

# 10.5 Crie uma função 'calculadora' que receba dois números e uma operação
def calculadora(num1, num2, operacao):
    if operacao == "+":
        return somar(num1, num2)
    elif operacao == "-":
        return subtrair(num1, num2)
    elif operacao == "*":
        return multiplicar(num1, num2)
    elif operacao == "/":
        return dividir(num1, num2)
    else:
        return None  # Operação inválida

# Teste a calculadora
print("Testando a calculadora:")
operacoes = [
    (10, 5, "+"),
    (10, 5, "-"),
    (10, 5, "*"),
    (10, 5, "/"),
    (10, 0, "/"),
    (10, 5, "%")
]

for num1, num2, op in operacoes:
    resultado = calculadora(num1, num2, op)
    if resultado is not None:
        print(f"{num1} {op} {num2} = {resultado}")
    else:
        print(f"{num1} {op} {num2} = erro (operação inválida ou divisão por zero)")
print()

# =============================================================================
# EXERCÍCIO 11: FUNÇÕES COM ESCOPO DE VARIÁVEIS
# =============================================================================
print("EXERCÍCIO 11: FUNÇÕES COM ESCOPO DE VARIÁVEIS")
print("-" * 40)

# Variável global
contador_global = 0

# 11.1 Crie uma função que modifique uma variável global
def incrementar_global():
    global contador_global
    contador_global += 1
    print(f"Contador global: {contador_global}")

# 11.2 Crie uma função que use uma variável local
def incrementar_local():
    contador_local = 0
    contador_local += 1
    print(f"Contador local: {contador_local}")

# Teste as funções
print("Testando escopo de variáveis:")
print("Variável global:")
incrementar_global()
incrementar_global()
incrementar_global()

print("\nVariável local:")
incrementar_local()
incrementar_local()
incrementar_local()
print()

# =============================================================================
# EXERCÍCIO 12: FUNÇÕES RECURSIVAS (CONCEITO BÁSICO)
# =============================================================================
print("EXERCÍCIO 12: FUNÇÕES RECURSIVAS (CONCEITO BÁSICO)")
print("-" * 40)

# 12.1 Crie uma função recursiva para calcular o fatorial
def fatorial_recursivo(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)

# Teste a função recursiva
print("Testando fatorial_recursivo:")
for i in range(6):
    resultado = fatorial_recursivo(i)
    print(f"Fatorial de {i}: {resultado}")
print()

# =============================================================================
# RESUMO E PRÓXIMOS PASSOS
# =============================================================================
print("=" * 60)
print("RESUMO DOS CONCEITOS APRENDIDOS")
print("=" * 60)
print("✅ Funções básicas sem parâmetros")
print("✅ Funções com parâmetros")
print("✅ Funções com retorno de valores")
print("✅ Funções com valores padrão")
print("✅ Funções com múltiplos retornos")
print("✅ Funções com listas e dicionários")
print("✅ Funções com estruturas condicionais")
print("✅ Funções com estruturas de repetição")
print("✅ Escopo de variáveis")
print("✅ Funções recursivas básicas")
print()
print("🎯 PRÓXIMOS PASSOS:")
print("- Módulos e bibliotecas")
print("- Programação orientada a objetos")
print("- Desenvolvimento de aplicações")
print()
print("Parabéns! Você dominou os conceitos fundamentais de funções em Python! 🎉")

