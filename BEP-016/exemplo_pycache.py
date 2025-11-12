"""
EXEMPLO: Demonstração do __pycache__

Este script mostra como o Python cria e usa o __pycache__
"""

import os
import sys

print("=" * 60)
print("ENTENDENDO O __pycache__")
print("=" * 60)

# Verificar se __pycache__ existe
caminho_cache = "crud_sistema/__pycache__"
existe = os.path.exists(caminho_cache)

print(f"\n1. Verificando se __pycache__ existe:")
print(f"   {caminho_cache}")
print(f"   Existe? {existe}")
print()

if existe:
    print("2. Listando arquivos em __pycache__:")
    arquivos = os.listdir(caminho_cache)
    for arquivo in arquivos:
        caminho_completo = os.path.join(caminho_cache, arquivo)
        tamanho = os.path.getsize(caminho_completo)
        print(f"   📄 {arquivo} ({tamanho} bytes)")
    print()
else:
    print("2. __pycache__ ainda não foi criado.")
    print("   Ele será criado quando você importar módulos do crud_sistema.")
    print()

print("=" * 60)
print("COMO O PYTHON USA O __pycache__")
print("=" * 60)

print("""
Quando você faz: import crud_sistema

1. Python procura por crud_sistema/
2. Lê os arquivos .py
3. Compila para bytecode (.pyc)
4. Salva em __pycache__/
5. Na próxima importação, usa o .pyc (mais rápido!)

Ciclo:
   Primeira vez:  .py → compila → .pyc → salva → executa
   Próximas vezes: .pyc existe? → SIM → usa .pyc (rápido!)
                  .pyc existe? → NÃO → compila novamente
""")

print("=" * 60)
print("POSSO APAGAR O __pycache__?")
print("=" * 60)

print("""
✅ SIM! Pode apagar sem problemas.

O que acontece:
   - Python vai recriar quando necessário
   - Não afeta o funcionamento do código
   - Útil para garantir que está usando código atualizado

Quando apagar:
   ✅ Antes de fazer commit no Git
   ✅ Quando você alterou código e quer garantir versão nova
   ✅ Para limpar arquivos temporários

Como apagar:
   rm -rf crud_sistema/__pycache__
   ou
   find . -type d -name __pycache__ -exec rm -r {} +
""")

print("=" * 60)
print("RECOMENDAÇÃO: .gitignore")
print("=" * 60)

print("""
Sempre adicione ao .gitignore:

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

Por quê?
   - Não precisa versionar bytecode
   - Cada desenvolvedor pode ter versão diferente do Python
   - Evita conflitos desnecessários
""")

print("=" * 60)
print("TESTE PRÁTICO")
print("=" * 60)

print("\nVamos importar o crud_sistema para criar o __pycache__:")
print("   import crud_sistema")
print()

try:
    import crud_sistema
    print("✅ Importação bem-sucedida!")
    print()
    
    # Verificar se foi criado agora
    if os.path.exists(caminho_cache):
        print("✅ __pycache__ foi criado!")
        print("   Verifique a pasta crud_sistema/__pycache__/")
    else:
        print("ℹ️  __pycache__ pode não ter sido criado ainda")
        print("   (pode acontecer em algumas versões do Python)")
        
except Exception as e:
    print(f"❌ Erro: {e}")

print()
print("=" * 60)
print("RESUMO")
print("=" * 60)
print("""
__pycache__/:
   ✅ Criado automaticamente
   ✅ Pode ser apagado
   ✅ Não precisa versionar (Git)
   ✅ Acelera importações
   ✅ Representa "memória local" de execução
""")

