"""
EXEMPLO: Como funciona o __init__.py

Este exemplo demonstra a diferença entre ter e não ter __init__.py
"""

print("=" * 60)
print("EXEMPLO 1: Importando com __init__.py (FÁCIL)")
print("=" * 60)

# Como nosso crud_sistema tem __init__.py configurado,
# podemos importar diretamente:

from crud_sistema import conectar_banco, cadastrar_aluno, listar_alunos

print("✅ Importação simples e limpa!")
print("   from crud_sistema import conectar_banco")
print()

# Podemos ver as funções disponíveis:
print("📦 Funções disponíveis via __init__.py:")
print("   - conectar_banco")
print("   - cadastrar_aluno")
print("   - listar_alunos")
print("   - buscar_aluno")
print("   - atualizar_aluno")
print("   - remover_aluno")
print("   - mostrar_estatisticas")
print("   - exibir_menu")
print()

print("=" * 60)
print("EXEMPLO 2: Como seria SEM __init__.py (DIFÍCIL)")
print("=" * 60)

# Sem __init__.py, precisaríamos fazer:
# from crud_sistema.database import conectar_banco
# from crud_sistema.crud_operations import cadastrar_aluno
# from crud_sistema.crud_operations import listar_alunos
# etc...

print("❌ Seria necessário importar com caminho completo:")
print("   from crud_sistema.database import conectar_banco")
print("   from crud_sistema.crud_operations import cadastrar_aluno")
print("   from crud_sistema.crud_operations import listar_alunos")
print("   # ... e assim por diante para cada função")
print()

print("=" * 60)
print("EXEMPLO 3: Verificando o __init__.py")
print("=" * 60)

# Podemos ver o que está definido no __init__.py
import crud_sistema

print(f"📦 Versão do pacote: {crud_sistema.__version__}")
print(f"👤 Autor: {crud_sistema.__author__}")
print()

print("📋 O que está exportado (__all__):")
if hasattr(crud_sistema, '__all__'):
    for item in crud_sistema.__all__:
        print(f"   - {item}")
print()

print("=" * 60)
print("CONCLUSÃO")
print("=" * 60)
print("""
✅ O __init__.py:
   1. Torna o diretório um PACOTE Python
   2. Facilita importações (não precisa do caminho completo)
   3. Define o que é exportado (__all__)
   4. Permite adicionar código de inicialização
    
✅ O __pycache__/:
   1. É criado AUTOMATICAMENTE pelo Python
   2. Contém bytecode compilado (.pyc)
   3. Acelera importações futuras
   4. Pode ser apagado sem problemas
   5. Deve estar no .gitignore
""")

