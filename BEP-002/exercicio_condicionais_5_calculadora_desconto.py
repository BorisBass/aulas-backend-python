# Exercício 5: Calculadora de Desconto
# Crie uma calculadora de desconto baseada no valor da compra:
# - Compras até R$ 100: sem desconto
# - Compras de R$ 100 a R$ 500: 5% de desconto
# - Compras de R$ 500 a R$ 1000: 10% de desconto
# - Compras acima de R$ 1000: 15% de desconto

print("=== CALCULADORA DE DESCONTO ===")
print()

# Entrada de dados
purchaseValue = float(input("Digite o valor da compra: R$ "))

# Validação do valor
if purchaseValue < 0:
    print("ERRO: O valor da compra não pode ser negativo!")
    exit()

# Estrutura condicional para cálculo do desconto
if purchaseValue <= 100:
    discountRate = 0
    discountCategory = "Sem desconto"
elif purchaseValue <= 500:
    discountRate = 0.05
    discountCategory = "Desconto de 5%"
elif purchaseValue <= 1000:
    discountRate = 0.10
    discountCategory = "Desconto de 10%"
else:
    discountRate = 0.15
    discountCategory = "Desconto de 15%"

# Cálculos
discountAmount = purchaseValue * discountRate
finalValue = purchaseValue - discountAmount

# Exibição dos resultados
print()
print("=== RESULTADO ===")
print(f"Valor original: R$ {purchaseValue:.2f}")
print(f"Categoria: {discountCategory}")
print(f"Taxa de desconto: {discountRate * 100:.0f}%")
print(f"Valor do desconto: R$ {discountAmount:.2f}")
print(f"Valor final: R$ {finalValue:.2f}")

# Informações adicionais
print()
print("=== INFORMAÇÕES ADICIONAIS ===")
print("Tabela de descontos:")
print("- Até R$ 100,00: Sem desconto")
print("- R$ 100,01 a R$ 500,00: 5% de desconto")
print("- R$ 500,01 a R$ 1.000,00: 10% de desconto")
print("- Acima de R$ 1.000,00: 15% de desconto")
print()
print(f"Economia: R$ {discountAmount:.2f}")
print(f"Percentual de economia: {(discountAmount / purchaseValue) * 100:.1f}%")

