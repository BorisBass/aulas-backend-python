# Exercício G: Propriedade Distributiva com Quatro Números
# Operações: A+B, A+C, A+D, B+C, B+D, C+D (adições)
# Operações: A*B, A*C, A*D, B*C, B*D, C*D (multiplicações)

print("=== PROPRIEDADE DISTRIBUTIVA ===")
print("Digite quatro números inteiros:")
print()

# Entrada de dados
valueA = int(input("Digite o valor de A: "))
valueB = int(input("Digite o valor de B: "))
valueC = int(input("Digite o valor de C: "))
valueD = int(input("Digite o valor de D: "))

print()
print("=== RESULTADOS DAS ADIÇÕES ===")
# Adições
sumAB = valueA + valueB
sumAC = valueA + valueC
sumAD = valueA + valueD
sumBC = valueB + valueC
sumBD = valueB + valueD
sumCD = valueC + valueD

print(f"A + B = {valueA} + {valueB} = {sumAB}")
print(f"A + C = {valueA} + {valueC} = {sumAC}")
print(f"A + D = {valueA} + {valueD} = {sumAD}")
print(f"B + C = {valueB} + {valueC} = {sumBC}")
print(f"B + D = {valueB} + {valueD} = {sumBD}")
print(f"C + D = {valueC} + {valueD} = {sumCD}")

print()
print("=== RESULTADOS DAS MULTIPLICAÇÕES ===")
# Multiplicações
multAB = valueA * valueB
multAC = valueA * valueC
multAD = valueA * valueD
multBC = valueB * valueC
multBD = valueB * valueD
multCD = valueC * valueD

print(f"A × B = {valueA} × {valueB} = {multAB}")
print(f"A × C = {valueA} × {valueC} = {multAC}")
print(f"A × D = {valueA} × {valueD} = {multAD}")
print(f"B × C = {valueB} × {valueC} = {multBC}")
print(f"B × D = {valueB} × {valueD} = {multBD}")
print(f"C × D = {valueC} × {valueD} = {multCD}")

print()
print("=== RESUMO ===")
print(f"Total de operações realizadas: 12 (6 adições + 6 multiplicações)")
print(f"Valores utilizados: A={valueA}, B={valueB}, C={valueC}, D={valueD}")
