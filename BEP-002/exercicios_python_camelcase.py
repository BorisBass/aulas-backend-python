# Exercícios Python - Notação CamelCase e Nomes em Inglês
# Prontos para Google Colab

# ========================================
# EXERCÍCIO A: Conversor Celsius para Fahrenheit
# ========================================

print("=== CONVERSOR CELSIUS PARA FAHRENHEIT ===")

# Ler temperatura em Celsius
temperatureCelsius = float(input("Digite a temperatura em graus Celsius: "))

# Calcular temperatura em Fahrenheit usando a fórmula: F = (9 * C + 160) / 5
temperatureFahrenheit = (9 * temperatureCelsius + 160) / 5

# Apresentar resultado
print(f"Temperatura em Celsius: {temperatureCelsius}°C")
print(f"Temperatura em Fahrenheit: {temperatureFahrenheit}°F")

print("\n" + "="*50 + "\n")

# ========================================
# EXERCÍCIO B: Conversor Fahrenheit para Celsius
# ========================================

print("=== CONVERSOR FAHRENHEIT PARA CELSIUS ===")

# Ler temperatura em Fahrenheit
temperatureFahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# Calcular temperatura em Celsius usando a fórmula: C = (F - 32) * (5/9)
temperatureCelsius = (temperatureFahrenheit - 32) * (5/9)

# Apresentar resultado
print(f"Temperatura em Fahrenheit: {temperatureFahrenheit}°F")
print(f"Temperatura em Celsius: {temperatureCelsius}°C")

print("\n" + "="*50 + "\n")

# ========================================
# EXERCÍCIO C: Calculadora de Volume de Lata de Óleo
# ========================================

print("=== CALCULADORA DE VOLUME DE LATA DE ÓLEO ===")

# Ler raio e altura da lata
radius = float(input("Digite o raio da lata em metros: "))
height = float(input("Digite a altura da lata em metros: "))

# Definir valor de π (pi)
pi = 3.14159

# Calcular volume usando a fórmula: Volume = π * Raio² * Altura
volume = pi * (radius ** 2) * height

# Apresentar resultado
print(f"Raio da lata: {radius} metros")
print(f"Altura da lata: {height} metros")
print(f"Volume da lata: {volume:.4f} metros cúbicos")

print("\n" + "="*50 + "\n")

# ========================================
# EXERCÍCIO D: Calculadora de Combustível de Viagem
# ========================================

print("=== CALCULADORA DE COMBUSTÍVEL DE VIAGEM ===")

# Ler tempo gasto e velocidade média
timeSpent = float(input("Digite o tempo gasto na viagem em horas: "))
averageSpeed = float(input("Digite a velocidade média em km/h: "))

# Calcular distância percorrida: DISTANCIA = TEMPO * VELOCIDADE
distance = timeSpent * averageSpeed

# Calcular litros de combustível utilizados: LITROS_USADOS = DISTANCIA / 12
# (considerando que o carro faz 12 km por litro)
litersUsed = distance / 12

# Apresentar todos os valores
print("\n=== RESUMO DA VIAGEM ===")
print(f"Velocidade média: {averageSpeed} km/h")
print(f"Tempo gasto: {timeSpent} horas")
print(f"Distância percorrida: {distance} km")
print(f"Litros de combustível utilizados: {litersUsed:.2f} litros")

print("\n" + "="*50 + "\n")

# ========================================
# EXERCÍCIOS INDIVIDUAIS PARA COPIAR NO COLAB
# ========================================

print("=== CÓDIGOS INDIVIDUAIS PARA COPIAR ===")
print("Copie cada bloco abaixo separadamente no Google Colab:\n")

print("EXERCÍCIO A - Conversor Celsius para Fahrenheit:")
print("""
print("=== CONVERSOR CELSIUS PARA FAHRENHEIT ===")

# ENTRADA: Ler temperatura em Celsius
temperatureCelsius = float(input("Digite a temperatura em graus Celsius: "))

# PROCESSAMENTO: Calcular temperatura em Fahrenheit
temperatureFahrenheit = (9 * temperatureCelsius + 160) / 5

# SAÍDA: Apresentar resultado
print(f"Temperatura em Celsius: {temperatureCelsius}°C")
print(f"Temperatura em Fahrenheit: {temperatureFahrenheit}°F")
""")

print("EXERCÍCIO B - Conversor Fahrenheit para Celsius:")
print("""
print("=== CONVERSOR FAHRENHEIT PARA CELSIUS ===")

# ENTRADA: Ler temperatura em Fahrenheit
temperatureFahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# PROCESSAMENTO: Calcular temperatura em Celsius
temperatureCelsius = (temperatureFahrenheit - 32) * (5/9)

# SAÍDA: Apresentar resultado
print(f"Temperatura em Fahrenheit: {temperatureFahrenheit}°F")
print(f"Temperatura em Celsius: {temperatureCelsius}°C")
""")

print("EXERCÍCIO C - Calculadora de Volume de Lata:")
print("""
print("=== CALCULADORA DE VOLUME DE LATA DE ÓLEO ===")

# ENTRADA: Ler raio e altura da lata
radius = float(input("Digite o raio da lata em metros: "))
height = float(input("Digite a altura da lata em metros: "))

# PROCESSAMENTO: Definir valor de π (pi) e calcular volume
pi = 3.14159
volume = pi * (radius ** 2) * height

# SAÍDA: Apresentar resultado
print(f"Raio da lata: {radius} metros")
print(f"Altura da lata: {height} metros")
print(f"Volume da lata: {volume:.4f} metros cúbicos")
""")

print("EXERCÍCIO D - Calculadora de Combustível:")
print("""
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
""")
