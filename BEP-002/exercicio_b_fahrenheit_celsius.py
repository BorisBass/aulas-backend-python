# EXERCÍCIO B: Conversor Fahrenheit para Celsius
# Fórmula: C = (F - 32) * (5/9)

print("=== CONVERSOR FAHRENHEIT PARA CELSIUS ===")

# ENTRADA: Ler temperatura em Fahrenheit
temperatureFahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# PROCESSAMENTO: Calcular temperatura em Celsius
temperatureCelsius = (temperatureFahrenheit - 32) * (5/9)

# SAÍDA: Apresentar resultado
print(f"Temperatura em Fahrenheit: {temperatureFahrenheit}°F")
print(f"Temperatura em Celsius: {temperatureCelsius}°C")
