# Exercício I: Quadrado da Diferença de Dois Números
# Fórmula: (A - B)²

print("=== QUADRADO DA DIFERENÇA ===")
print()

# Entrada de dados
print("Digite dois números inteiros:")
valueA = int(input("Digite o valor de A: "))
valueB = int(input("Digite o valor de B: "))

# Cálculo da diferença
difference = valueA - valueB

# Cálculo do quadrado da diferença
squaredDifference = difference ** 2

# Saída dos resultados
print()
print("=== RESULTADO ===")
print(f"Valor A: {valueA}")
print(f"Valor B: {valueB}")
print(f"Diferença (A - B): {valueA} - {valueB} = {difference}")
print(f"Quadrado da diferença: ({difference})² = {squaredDifference}")

# Verificação alternativa
print()
print("=== VERIFICAÇÃO ===")
print(f"Desenvolvendo (A - B)² = A² - 2AB + B²:")
print(f"= {valueA}² - 2×{valueA}×{valueB} + {valueB}²")
print(f"= {valueA**2} - {2*valueA*valueB} + {valueB**2}")
print(f"= {valueA**2 - 2*valueA*valueB + valueB**2}")
print(f"Resultado confirma: {squaredDifference}")
