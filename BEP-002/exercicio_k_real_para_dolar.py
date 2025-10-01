# Exercício K: Conversão de Real para Dólar
# Solicita cotação do dólar e quantidade de reais

print("=== CONVERSOR REAL PARA DÓLAR ===")
print()

# Entrada de dados
dollarRate = float(input("Digite a cotação do dólar (R$ por US$): "))
realAmount = float(input("Digite a quantidade de reais: "))

# Cálculo da conversão
valueInDollars = realAmount / dollarRate

# Saída dos resultados
print()
print("=== RESULTADO DA CONVERSÃO ===")
print(f"Cotação do dólar: R$ {dollarRate:.2f}")
print(f"Quantidade de reais: R$ {realAmount:.2f}")
print(f"Valor em dólares: US$ {valueInDollars:.2f}")

# Informações adicionais
print()
print("=== INFORMAÇÕES ADICIONAIS ===")
print(f"Taxa de câmbio: 1 USD = R$ {dollarRate:.2f}")
print(f"Valor por real: US$ {1/dollarRate:.4f}")

# Formatação para moeda americana
print()
print("=== FORMATO AMERICANO ===")
print(f"Você tem R$ {realAmount:.2f} que equivalem a US$ {valueInDollars:.2f}")

# Comparação com o exercício anterior
print()
print("=== COMPARAÇÃO ===")
print(f"Se você converter US$ {valueInDollars:.2f} de volta para reais:")
print(f"US$ {valueInDollars:.2f} × R$ {dollarRate:.2f} = R$ {valueInDollars * dollarRate:.2f}")
print(f"Valor original: R$ {realAmount:.2f}")
print(f"Diferença: R$ {abs(realAmount - valueInDollars * dollarRate):.2f}")
