# Exercício F: Troca de Valores entre Variáveis A e B

print("=== TROCA DE VALORES ENTRE VARIÁVEIS ===")
print()

# Entrada de dados
print("Digite o valor para a variável A:")
valueA = input("A = ")

print("Digite o valor para a variável B:")
valueB = input("B = ")

# Exibição dos valores originais
print()
print("=== VALORES ORIGINAIS ===")
print(f"A = {valueA}")
print(f"B = {valueB}")

# Troca dos valores
temporaryValue = valueA
valueA = valueB
valueB = temporaryValue

# Exibição dos valores trocados
print()
print("=== VALORES APÓS A TROCA ===")
print(f"A = {valueA}")
print(f"B = {valueB}")
print()
print("Os valores foram trocados com sucesso!")
