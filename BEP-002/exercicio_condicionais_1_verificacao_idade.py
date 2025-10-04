# Exercício 1: Verificação de Idade
# Crie um programa que verifique se uma pessoa é maior de idade

print("=== VERIFICAÇÃO DE IDADE ===")
print()

# Entrada de dados
age = int(input("Digite sua idade: "))

# Estrutura condicional
if age >= 18:
    print("Maior de idade!")
    print("Você tem acesso a todos os serviços.")
else:
    print("Menor de idade!")
    print("Alguns serviços podem ter restrições.")

# Informações adicionais
print()
print("=== INFORMAÇÕES ADICIONAIS ===")
print(f"Idade informada: {age} anos")
if age >= 18:
    print("Status: Adulto")
else:
    print("Status: Menor de idade")

