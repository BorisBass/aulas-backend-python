# Exercício 4: Verificação de Acesso
# Crie um sistema de verificação de acesso:
# Solicite idade e se tem carteira de identidade
# Regras:
# - Menor de 18 anos: "Acesso negado - menor de idade"
# - Maior de 18 anos sem carteira: "Acesso negado - sem documento"
# - Maior de 18 anos com carteira: "Acesso liberado"

print("=== SISTEMA DE VERIFICAÇÃO DE ACESSO ===")
print()

# Entrada de dados
age = int(input("Digite sua idade: "))
hasId = input("Você tem carteira de identidade? (s/n): ").lower().strip()

# Validação da entrada
if hasId in ['s', 'sim', 'y', 'yes']:
    hasId = True
elif hasId in ['n', 'não', 'nao', 'no']:
    hasId = False
else:
    print("ERRO: Digite 's' para sim ou 'n' para não!")
    exit()

# Estrutura condicional para verificação de acesso
print()
print("=== VERIFICAÇÃO DE ACESSO ===")
print(f"Idade: {age} anos")
print(f"Possui carteira: {'Sim' if hasId else 'Não'}")
print()

if age < 18:
    print("❌ ACESSO NEGADO - Menor de idade")
    print("Você precisa ter pelo menos 18 anos para acessar este serviço.")
elif not hasId:
    print("❌ ACESSO NEGADO - Sem documento")
    print("Você precisa apresentar uma carteira de identidade válida.")
else:
    print("✅ ACESSO LIBERADO")
    print("Bem-vindo! Você pode acessar todos os serviços disponíveis.")

# Informações adicionais
print()
print("=== INFORMAÇÕES ADICIONAIS ===")
print("Requisitos para acesso:")
print("1. Ter pelo menos 18 anos de idade")
print("2. Apresentar carteira de identidade válida")
print()
print("Status atual:")
print(f"- Idade adequada: {'Sim' if age >= 18 else 'Não'}")
print(f"- Documento apresentado: {'Sim' if hasId else 'Não'}")
print(f"- Acesso permitido: {'Sim' if age >= 18 and hasId else 'Não'}")

