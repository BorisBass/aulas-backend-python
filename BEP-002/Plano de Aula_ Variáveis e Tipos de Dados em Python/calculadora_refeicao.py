# Calculadora de Custo de Refeição Simples

# 1. Itens de refeição pré-definidos com seus preços unitários
preco_hamburguer = 15.50
preco_batata_frita = 8.00
preco_refrigerante = 6.50

print("Bem-vindo à Calculadora de Custo de Refeição Simples!")
print("--------------------------------------------------")

# 2. Solicitar a quantidade desejada de cada item ao usuário
quantidade_hamburguer_str = input(f"Quantos Hambúrgueres (R$ {preco_hamburguer:.2f} cada) você deseja? ")
quantidade_batata_frita_str = input(f"Quantas Batatas Fritas (R$ {preco_batata_frita:.2f} cada) você deseja? ")
quantidade_refrigerante_str = input(f"Quantos Refrigerantes (R$ {preco_refrigerante:.2f} cada) você deseja? ")

# 3. Converter as entradas do usuário para números inteiros (casting)
#    Usamos try-except para lidar com entradas não numéricas, embora o projeto inicial não exija isso explicitamente, é uma boa prática.
try:
    quantidade_hamburguer = int(quantidade_hamburguer_str)
    quantidade_batata_frita = int(quantidade_batata_frita_str)
    quantidade_refrigerante = int(quantidade_refrigerante_str)
except ValueError:
    print("Erro: Por favor, digite apenas números inteiros para as quantidades.")
    # Em um programa real, você poderia pedir para o usuário digitar novamente ou sair.
    exit()

# 4. Calcular o custo individual de cada item
custo_hamburguer = quantidade_hamburguer * preco_hamburguer
custo_batata_frita = quantidade_batata_frita * preco_batata_frita
custo_refrigerante = quantidade_refrigerante * preco_refrigerante

# 5. Calcular o custo total da refeição
custo_total_refeicao = custo_hamburguer + custo_batata_frita + custo_refrigerante

print("\n--- Detalhes do Pedido ---")
print(f"Hambúrgueres: {quantidade_hamburguer} x R$ {preco_hamburguer:.2f} = R$ {custo_hamburguer:.2f}")
print(f"Batatas Fritas: {quantidade_batata_frita} x R$ {preco_batata_frita:.2f} = R$ {custo_batata_frita:.2f}")
print(f"Refrigerantes: {quantidade_refrigerante} x R$ {preco_refrigerante:.2f} = R$ {custo_refrigerante:.2f}")
print("--------------------------------------------------")
print(f"Custo Total da Refeição: R$ {custo_total_refeicao:.2f}")
print("--------------------------------------------------")
print("Obrigado por usar a calculadora!")


