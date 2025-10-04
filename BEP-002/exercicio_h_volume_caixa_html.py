# Exercício H: Cálculo do Volume de uma Caixa Retangular (Versão HTML)
# Fórmula: VOLUME = COMPRIMENTO × LARGURA × ALTURA

from IPython.display import display, HTML

print("=== CÁLCULO DO VOLUME DE UMA CAIXA RETANGULAR ===")
print()

# Entrada de dados
print("Digite as dimensões da caixa:")
comprimento = float(input("Comprimento (cm): "))
largura = float(input("Largura (cm): "))
altura = float(input("Altura (cm): "))

# Cálculo do volume
volume = comprimento * largura * altura

# Saída dos resultados
print()
print("=== RESULTADO ===")
print(f"Comprimento: {comprimento} cm")
print(f"Largura: {largura} cm")
print(f"Altura: {altura} cm")

# Usando HTML para exibir com sobrescrito
display(HTML(f"<p><b>Volume da caixa:</b> {volume:.2f} cm<sup>3</sup></p>"))

# Informações adicionais
display(HTML(f"<p><b>Volume em litros:</b> {volume / 1000:.3f} L</p>"))
display(HTML(f"<p><b>Volume em metros cúbicos:</b> {volume / 1000000:.6f} m<sup>3</sup></p>"))

# Fórmula matemática
display(HTML(f"<p><b>Fórmula:</b> Volume = {comprimento} × {largura} × {altura} = {volume:.2f} cm<sup>3</sup></p>"))





