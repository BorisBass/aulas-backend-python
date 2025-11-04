"""
EXEMPLO: Demonstração de importação

Este arquivo mostra o que acontece quando você importa os outros arquivos.
"""

print("\n" + "="*60)
print("TESTE 1: Importando arquivo SEM if __name__ == '__main__'")
print("="*60)
print("Atenção: O código vai executar automaticamente!")
print()

# Descomente a linha abaixo para ver o problema:
import exemplo_sem_name_main
# → O código do exemplo_sem_name_main executa automaticamente!

print("\n" + "="*60)
print("TESTE 2: Importando arquivo COM if __name__ == '__main__'")
print("="*60)
print("Atenção: O código NÃO vai executar, só as funções ficam disponíveis!")
print()

# Descomente as linhas abaixo para ver a solução:
import exemplo_com_name_main
# → O código dentro do if NÃO executa
# → Mas você pode usar as funções:
# print(exemplo_com_name_main.saudacao("Pedro"))
# print(f"Idade: {exemplo_com_name_main.calcular_idade(1990)} anos")

print("\n" + "="*60)
print("CONCLUSÃO")
print("="*60)
print("""
✅ Use if __name__ == "__main__" quando:
   - Você quer que o arquivo possa ser importado
   - Você quer separar código de teste do código principal
   - Você segue boas práticas de programação

❌ Você pode pular se:
   - É um script muito simples e rápido
   - Você tem certeza que nunca vai importar o arquivo
   - Mas mesmo assim, é melhor usar sempre!
""")



