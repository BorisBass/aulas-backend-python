# Exercício J: Conversão de Dólar para Real
# Solicita cotação do dólar e quantidade de dólares

print("=== CONVERSOR DÓLAR PARA REAL ===")
print()

# Entrada de dados
dollarRate = float(input("Digite a cotação do dólar (R$ por US$): "))
dollarAmount = float(input("Digite a quantidade de dólares: "))

# Cálculo da conversão
valueInReais = dollarAmount * dollarRate

# Saída dos resultados
print()
print("=== RESULTADO DA CONVERSÃO ===")
print(f"Cotação do dólar: R$ {dollarRate:.2f}")
print(f"Quantidade de dólares: US$ {dollarAmount:.2f}")
print(f"Valor em reais: R$ {valueInReais:.2f}")

# Informações adicionais
print()
print("=== INFORMAÇÕES ADICIONAIS ===")
print(f"Taxa de câmbio: 1 USD = R$ {dollarRate:.2f}")
print(f"Valor por dólar: R$ {dollarRate:.2f}")

# Formatação para moeda brasileira
print()
print("=== FORMATO BRASILEIRO ===")
print(f"Você tem US$ {dollarAmount:.2f} que equivalem a R$ {valueInReais:.2f}")
