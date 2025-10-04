# Exercício 2: Sistema de Notas
# Crie um sistema de notas com os seguintes critérios:
# 9.0 - 10.0: A
# 7.0 - 8.9: B
# 5.0 - 6.9: C
# 0.0 - 4.9: D

print("=== SISTEMA DE NOTAS ===")
print()

# Entrada de dados
grade = float(input("Digite sua nota (0.0 a 10.0): "))

# Validação da nota
if grade < 0 or grade > 10:
    print("ERRO: Nota deve estar entre 0.0 e 10.0!")
else:
    # Estrutura condicional para classificação
    if grade >= 9.0:
        concept = "A"
        status = "Excelente"
    elif grade >= 7.0:
        concept = "B"
        status = "Bom"
    elif grade >= 5.0:
        concept = "C"
        status = "Regular"
    else:
        concept = "D"
        status = "Insuficiente"
    
    # Exibição dos resultados
    print()
    print("=== RESULTADO ===")
    print(f"Nota: {grade:.1f}")
    print(f"Conceito: {concept}")
    print(f"Status: {status}")
    
    # Informações adicionais
    print()
    print("=== INFORMAÇÕES ADICIONAIS ===")
    if concept in ["A", "B"]:
        print("Parabéns! Você foi aprovado com bom desempenho!")
    elif concept == "C":
        print("Você foi aprovado, mas pode melhorar!")
    else:
        print("Você foi reprovado. Estude mais para a próxima!")

