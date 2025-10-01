# EXERCÍCIO C: Calculadora de Volume de Lata de Óleo
# Fórmula: Volume = π * Raio² * Altura

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
