# Exercício M: Quadrado da Soma de Três Valores
# Fórmula: (A + B + C)²

print("=== QUADRADO DA SOMA ===")
print()

# Entrada de dados
print("Digite três valores:")
valueA = float(input("Digite o valor de A: "))
valueB = float(input("Digite o valor de B: "))
valueC = float(input("Digite o valor de C: "))

# Cálculo da soma
sumOfValues = valueA + valueB + valueC

# Cálculo do quadrado da soma
squaredSum = sumOfValues ** 2

# Saída dos resultados
print()
print("=== RESULTADO ===")
print(f"Valor A: {valueA}")
print(f"Valor B: {valueB}")
print(f"Valor C: {valueC}")
print()
print("=== CÁLCULO DA SOMA ===")
print(f"A + B + C = {valueA} + {valueB} + {valueC} = {sumOfValues}")
print()
print("=== QUADRADO DA SOMA ===")
print(f"(A + B + C)² = ({sumOfValues})² = {squaredSum}")

# Desenvolvimento da fórmula
print()
print("=== DESENVOLVIMENTO DA FÓRMULA ===")
print(f"(A + B + C)² = A² + B² + C² + 2AB + 2AC + 2BC")
print(f"= {valueA}² + {valueB}² + {valueC}² + 2×{valueA}×{valueB} + 2×{valueA}×{valueC} + 2×{valueB}×{valueC}")
print(f"= {valueA**2} + {valueB**2} + {valueC**2} + {2*valueA*valueB} + {2*valueA*valueC} + {2*valueB*valueC}")
print(f"= {valueA**2 + valueB**2 + valueC**2 + 2*valueA*valueB + 2*valueA*valueC + 2*valueB*valueC}")
print(f"Resultado confirma: {squaredSum}")

# Comparação com o exercício anterior
print()
print("=== COMPARAÇÃO COM SOMA DOS QUADRADOS ===")
sumOfSquares = valueA**2 + valueB**2 + valueC**2
print(f"Soma dos quadrados (A² + B² + C²): {sumOfSquares}")
print(f"Quadrado da soma (A + B + C)²: {squaredSum}")
print(f"Diferença: {squaredSum - sumOfSquares}")
print(f"Termos adicionais: 2AB + 2AC + 2BC = {2*valueA*valueB + 2*valueA*valueC + 2*valueB*valueC}")
