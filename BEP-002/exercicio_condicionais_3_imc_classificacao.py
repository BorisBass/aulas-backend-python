# Exercício 3: Calculadora de IMC com Classificação
# Crie um programa que calcule o IMC e classifique:
# IMC < 18.5: Abaixo do peso
# 18.5 <= IMC < 25: Peso normal
# 25 <= IMC < 30: Sobrepeso
# IMC >= 30: Obesidade

print("=== CALCULADORA DE IMC COM CLASSIFICAÇÃO ===")
print()

# Entrada de dados
weight = float(input("Digite seu peso (kg): "))
height = float(input("Digite sua altura (m): "))

# Cálculo do IMC
bmi = weight / (height ** 2)

# Estrutura condicional para classificação
if bmi < 18.5:
    category = "Abaixo do peso"
    recommendation = "Consulte um nutricionista para ganhar peso de forma saudável"
elif bmi < 25:
    category = "Peso normal"
    recommendation = "Parabéns! Mantenha seus hábitos saudáveis"
elif bmi < 30:
    category = "Sobrepeso"
    recommendation = "Considere uma dieta balanceada e exercícios regulares"
else:
    category = "Obesidade"
    recommendation = "Recomendamos consultar um médico e nutricionista"

# Exibição dos resultados
print()
print("=== RESULTADO ===")
print(f"Peso: {weight} kg")
print(f"Altura: {height} m")
print(f"IMC: {bmi:.2f}")
print(f"Classificação: {category}")
print(f"Recomendação: {recommendation}")

# Informações adicionais
print()
print("=== INFORMAÇÕES ADICIONAIS ===")
print("Fórmula do IMC: peso / (altura)²")
print(f"Cálculo: {weight} / ({height})² = {bmi:.2f}")
print()
print("Classificação IMC:")
print("- Abaixo do peso: IMC < 18.5")
print("- Peso normal: 18.5 ≤ IMC < 25")
print("- Sobrepeso: 25 ≤ IMC < 30")
print("- Obesidade: IMC ≥ 30")

