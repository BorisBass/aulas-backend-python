# Exercício E: Cálculo de Prestação em Atraso
# Fórmula: PRESTACAO = VALOR + (VALOR * TAXA/100) * TEMPO

print("=== CÁLCULO DE PRESTAÇÃO EM ATRASO ===")
print()

# Entrada de dados
originalValue = float(input("Digite o valor original da prestação: R$ "))
interestRate = float(input("Digite a taxa de juros (%): "))
delayTime = int(input("Digite o tempo de atraso (em meses): "))

# Cálculo da prestação em atraso
latePayment = originalValue + (originalValue * interestRate / 100) * delayTime

# Saída dos resultados
print()
print("=== RESULTADO ===")
print(f"Valor original: R$ {originalValue:.2f}")
print(f"Taxa de juros: {interestRate}%")
print(f"Tempo de atraso: {delayTime} meses")
print(f"Valor da prestação em atraso: R$ {latePayment:.2f}")
print(f"Juros cobrados: R$ {latePayment - originalValue:.2f}")
