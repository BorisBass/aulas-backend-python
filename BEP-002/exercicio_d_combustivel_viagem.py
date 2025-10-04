# EXERCÍCIO D: Calculadora de Combustível de Viagem
# Carro faz 12 km por litro
# Fórmulas: DISTANCIA = TEMPO * VELOCIDADE
#          LITROS_USADOS = DISTANCIA / 12

print("=== CALCULADORA DE COMBUSTÍVEL DE VIAGEM ===")

# ENTRADA: Ler tempo gasto e velocidade média
timeSpent = float(input("Digite o tempo gasto na viagem em horas: "))
averageSpeed = float(input("Digite a velocidade média em km/h: "))

# PROCESSAMENTO: Calcular distância percorrida e litros utilizados
distance = timeSpent * averageSpeed
litersUsed = distance / 12

# SAÍDA: Apresentar todos os valores
print("\n=== RESUMO DA VIAGEM ===")
print(f"Velocidade média: {averageSpeed} km/h")
print(f"Tempo gasto: {timeSpent} horas")
print(f"Distância percorrida: {distance} km")
print(f"Litros de combustível utilizados: {litersUsed:.2f} litros")
