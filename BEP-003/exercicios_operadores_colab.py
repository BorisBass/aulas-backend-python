
# Exercícios de Operadores Aritméticos, Relacionais e Lógicos em Python

# --- Operadores Aritméticos ---

# Exercício A1: Cálculos Básicos
# Peça ao usuário para digitar dois números. Realize e imprima a soma, subtração, multiplicação e divisão.
print("\n--- Exercício A1: Cálculos Básicos ---")
num1_a1 = float(input("Digite o primeiro número: "))
num2_a1 = float(input("Digite o segundo número: "))

soma_a1 = num1_a1 + num2_a1
subtracao_a1 = num1_a1 - num2_a1
multiplicacao_a1 = num1_a1 * num2_a1

print(f"Soma: {soma_a1}")
print(f"Subtração: {subtracao_a1}")
print(f"Multiplicação: {multiplicacao_a1}")

if num2_a1 != 0:
    divisao_a1 = num1_a1 / num2_a1
    print(f"Divisão: {divisao_a1}")
else:
    print("Divisão por zero não é permitida.")

# Exercício A2: Média Ponderada
# Peça ao usuário para digitar 3 notas e seus respectivos pesos. Calcule e imprima a média ponderada.
print("\n--- Exercício A2: Média Ponderada ---")
nota1 = float(input("Digite a primeira nota: "))
peso1 = float(input("Digite o peso da primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))
peso2 = float(input("Digite o peso da segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))
peso3 = float(input("Digite o peso da terceira nota: "))

media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
print(f"A média ponderada é: {media_ponderada:.2f}")

# Exercício A3: Conversor de Moeda Simples
# Peça ao usuário um valor em Reais (R$) e uma taxa de câmbio para Dólar (US$). Converta e imprima o valor em Dólar.
print("\n--- Exercício A3: Conversor de Moeda Simples ---")
valor_reais = float(input("Digite o valor em Reais (R$): "))
taxa_cambio = float(input("Digite a taxa de câmbio (ex: 5.20 para 1 US$): "))

valor_dolar = valor_reais / taxa_cambio
print(f"O valor em Dólar é: US$ {valor_dolar:.2f}")

# --- Operadores Relacionais ---

# Exercício R1: Comparação de Idades
# Peça a idade de duas pessoas. Imprima se a primeira pessoa é mais velha, mais nova ou tem a mesma idade que a segunda.
print("\n--- Exercício R1: Comparação de Idades ---")
idade1 = int(input("Digite a idade da primeira pessoa: "))
idade2 = int(input("Digite a idade da segunda pessoa: "))

print(f"Pessoa 1 é mais velha que Pessoa 2: {idade1 > idade2}")
print(f"Pessoa 1 é mais nova que Pessoa 2: {idade1 < idade2}")
print(f"Pessoa 1 tem a mesma idade que Pessoa 2: {idade1 == idade2}")

# Exercício R2: Verificação de Aprovação
# Peça a nota de um aluno. Imprima True se a nota for maior ou igual a 70 (aprovado), False caso contrário.
print("\n--- Exercício R2: Verificação de Aprovação ---")
nota_aluno = float(input("Digite a nota do aluno: "))

esta_aprovado = nota_aluno >= 70
print(f"O aluno está aprovado? {esta_aprovado}")

# Exercício R3: Intervalo Numérico
# Peça um número. Imprima True se o número estiver entre 10 e 20 (inclusive), False caso contrário.
print("\n--- Exercício R3: Intervalo Numérico ---")
numero_intervalo = float(input("Digite um número: "))

esta_no_intervalo = (numero_intervalo >= 10) and (numero_intervalo <= 20)
print(f"O número está entre 10 e 20? {esta_no_intervalo}")

# --- Operadores Lógicos ---

# Exercício L1: Condição para Desconto
# Peça ao usuário se ele é estudante (True/False) e se tem cupom de desconto (True/False). Imprima True se ele tiver direito a desconto (é estudante OU tem cupom).
print("\n--- Exercício L1: Condição para Desconto ---")
# Para simplificar, vamos assumir que o usuário digitará 'True' ou 'False' (como string)
# Em um cenário real, usaríamos input() e converteríamos para bool, ou usaríamos checkboxes em uma interface.

eh_estudante_str = input("Você é estudante? (True/False): ")
tem_cupom_str = input("Você tem cupom de desconto? (True/False): ")

eh_estudante = eh_estudante_str.lower() == 'true'
tem_cupom = tem_cupom_str.lower() == 'true'

tem_direito_desconto = eh_estudante or tem_cupom
print(f"Tem direito a desconto? {tem_direito_desconto}")

# Exercício L2: Acesso Permitido
# Peça ao usuário se ele tem permissão de administrador (True/False) e se a senha está correta (True/False). Imprima True se o acesso for permitido (tem permissão E senha correta).
print("\n--- Exercício L2: Acesso Permitido ---")
tem_admin_str = input("Você tem permissão de administrador? (True/False): ")
senha_correta_str = input("A senha está correta? (True/False): ")

tem_admin = tem_admin_str.lower() == 'true'
senha_correta = senha_correta_str.lower() == 'true'

acesso_permitido = tem_admin and senha_correta
print(f"Acesso permitido? {acesso_permitido}")

# Exercício L3: Negação
# Peça ao usuário se ele está logado (True/False). Imprima True se ele NÃO estiver logado.
print("\n--- Exercício L3: Negação ---")
esta_logado_str = input("Você está logado? (True/False): ")

esta_logado = esta_logado_str.lower() == 'true'

nao_esta_logado = not esta_logado
print(f"Não está logado? {nao_esta_logado}")

# --- Precedência e Associação de Operadores ---

# Exercício P1: Expressão Complexa
# Calcule o resultado da expressão: 5 + 3 * 2 ** 2 - 10 / 5
print("\n--- Exercício P1: Expressão Complexa ---")
resultado_p1 = 5 + 3 * 2 ** 2 - 10 / 5
print(f"Resultado de 5 + 3 * 2 ** 2 - 10 / 5: {resultado_p1}")

# Exercício P2: Uso de Parênteses
# Calcule o resultado da expressão: (5 + 3) * 2 ** (2 - 10) / 5
print("\n--- Exercício P2: Uso de Parênteses ---")
resultado_p2 = (5 + 3) * 2 ** (2 - 10) / 5
print(f"Resultado de (5 + 3) * 2 ** (2 - 10) / 5: {resultado_p2}")

# Exercício P3: Condição Lógica com Precedência
# Peça dois números (num_p3_a, num_p3_b) e um booleano (condicao_p3). 
# Verifique se (num_p3_a > 10 e num_p3_b < 5) ou condicao_p3 é True.
print("\n--- Exercício P3: Condição Lógica com Precedência ---")
num_p3_a = float(input("Digite o primeiro número para P3: "))
num_p3_b = float(input("Digite o segundo número para P3: "))
condicao_p3_str = input("Digite True ou False para a condição P3: ")
condicao_p3 = condicao_p3_str.lower() == 'true'

resultado_p3 = (num_p3_a > 10 and num_p3_b < 5) or condicao_p3
print(f"Resultado da condição: {resultado_p3}")


