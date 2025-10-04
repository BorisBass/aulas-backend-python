# EXERCÍCIO A: Conversor Celsius para Fahrenheit
# Fórmula: F = (9 * C + 160) / 5

print("=== CONVERSOR CELSIUS PARA FAHRENHEIT ===")

# ENTRADA: Ler temperatura em Celsius
temperatureCelsius = float(input("Digite a temperatura em graus Celsius: "))

# PROCESSAMENTO: Calcular temperatura em Fahrenheit
temperatureFahrenheit = (9 * temperatureCelsius + 160) / 5

# SAÍDA: Apresentar resultado
print(f"Temperatura em Celsius: {temperatureCelsius}°C")
print(f"Temperatura em Fahrenheit: {temperatureFahrenheit}°F")
