# Exercício H: Cálculo do Volume de uma Caixa Retangular
# Fórmula: VOLUME = COMPRIMENTO × LARGURA × ALTURA

print("=== CÁLCULO DO VOLUME DE UMA CAIXA RETANGULAR ===")
print()

# Entrada de dados
print("Digite as dimensões da caixa:")
length = float(input("Comprimento (cm): "))
width = float(input("Largura (cm): "))
height = float(input("Altura (cm): "))

# Cálculo do volume
volume = length * width * height

# Saída dos resultados
print()
print("=== RESULTADO ===")
print(f"Comprimento: {length} cm")
print(f"Largura: {width} cm")
print(f"Altura: {height} cm")
print(f"Volume da caixa: {volume:.2f} cm³")

# Informações adicionais
print()
print("=== INFORMAÇÕES ADICIONAIS === cm")
print(f"Volume em litros: {volume / 1000:.3f} L")
print(f"Volume em metros cúbicos: {volume / 1000000:.6f} m³")
