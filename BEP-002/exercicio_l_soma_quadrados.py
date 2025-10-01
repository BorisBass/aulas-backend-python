# Exercício L: Soma dos Quadrados de Três Valores
# Fórmula: A² + B² + C²

print("=== SOMA DOS QUADRADOS ===")
print()

# Entrada de dados
print("Digite três valores:")
valueA = float(input("Digite o valor de A: "))
valueB = float(input("Digite o valor de B: "))
valueC = float(input("Digite o valor de C: "))

# Cálculo dos quadrados
squareA = valueA ** 2
squareB = valueB ** 2
squareC = valueC ** 2

# Cálculo da soma dos quadrados
sumOfSquares = squareA + squareB + squareC

# Saída dos resultados
print()
print("=== RESULTADO ===")
print(f"Valor A: {valueA}")
print(f"Valor B: {valueB}")
print(f"Valor C: {valueC}")
print()
print("=== CÁLCULO DOS QUADRADOS ===")
print(f"A² = {valueA}² = {squareA}")
print(f"B² = {valueB}² = {squareB}")
print(f"C² = {valueC}² = {squareC}")
print()
print("=== SOMA DOS QUADRADOS ===")
print(f"A² + B² + C² = {squareA} + {squareB} + {squareC}")
print(f"Resultado: {sumOfSquares}")

# Verificação alternativa
print()
print("=== VERIFICAÇÃO ===")
print(f"Desenvolvendo: ({valueA})² + ({valueB})² + ({valueC})²")
print(f"= {squareA} + {squareB} + {squareC}")
print(f"= {sumOfSquares}")
