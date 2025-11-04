"""
EXPLICAÇÃO: O que são os comandos com __ (dunder) e quando usar if __name__ == "__main__"

Este arquivo demonstra diferentes formas de estruturar programas Python.
"""

# ============================================================================
# PARTE 1: O QUE SÃO OS COMANDOS COM __ (DUNDER METHODS)?
# ============================================================================

"""
Os comandos que começam e terminam com __ (dois underscores) são chamados de 
"dunder methods" (double underscore methods) ou "métodos especiais" em Python.

Exemplos comuns:
- __name__: Variável especial que contém o nome do módulo
- __main__: String especial que indica o módulo principal
- __init__: Método construtor de classes
- __str__: Método que define como o objeto é representado como string
- __len__: Método que define o comportamento da função len()

NÃO são comandos normais - são partes especiais da linguagem Python!
"""

# ============================================================================
# PARTE 2: PROGRAMA SIMPLES - SEM if __name__ == "__main__"
# ============================================================================

print("\n" + "="*60)
print("EXEMPLO 1: Programa simples SEM if __name__ == '__main__'")
print("="*60)

# Este código executa DIRETAMENTE quando o arquivo é rodado
# Funciona perfeitamente para programas simples!

def somar(a, b):
    """Função simples de soma"""
    return a + b

def subtrair(a, b):
    """Função simples de subtração"""
    return a - b

# Código executando diretamente
print("Calculadora Simples")
print(f"5 + 3 = {somar(5, 3)}")
print(f"10 - 4 = {subtrair(10, 4)}")

# Este código SEMPRE executa quando você roda o arquivo
# Mas pode causar problemas se você quiser IMPORTAR este arquivo em outro lugar!


# ============================================================================
# PARTE 3: PROGRAMA COM if __name__ == "__main__"
# ============================================================================

print("\n" + "="*60)
print("EXEMPLO 2: Programa COM if __name__ == '__main__' (RECOMENDADO)")
print("="*60)

def multiplicar(a, b):
    """Função de multiplicação"""
    return a * b

def dividir(a, b):
    """Função de divisão"""
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

# Esta parte SÓ executa se o arquivo for rodado diretamente
# NÃO executa se o arquivo for importado em outro lugar
if __name__ == "__main__":
    print("Calculadora Avançada")
    print(f"6 * 4 = {multiplicar(6, 4)}")
    print(f"15 / 3 = {dividir(15, 3)}")
    print(f"10 / 0 = {dividir(10, 0)}")


# ============================================================================
# PARTE 4: POR QUE USAR if __name__ == "__main__"?
# ============================================================================

print("\n" + "="*60)
print("EXPLICAÇÃO: Por que usar if __name__ == '__main__'?")
print("="*60)

print("""
Quando você roda um arquivo Python diretamente:
    python meu_arquivo.py
    
    → __name__ será igual a "__main__"
    → O código dentro do if executa

Quando você IMPORTA um arquivo Python em outro lugar:
    import meu_arquivo
    
    → __name__ será igual a "meu_arquivo" (nome do módulo)
    → O código dentro do if NÃO executa
    → Mas as funções ficam disponíveis para uso!

VANTAGENS:
1. ✅ Permite que o arquivo seja usado como módulo (importado)
2. ✅ Evita executar código desnecessário ao importar
3. ✅ É uma boa prática de programação
4. ✅ Facilita testes e reutilização de código
""")


# ============================================================================
# PARTE 5: EXEMPLO PRÁTICO - COM E SEM
# ============================================================================

print("\n" + "="*60)
print("EXEMPLO PRÁTICO: Comparação")
print("="*60)

# Função que pode ser reutilizada
def calcular_area_retangulo(largura, altura):
    """Calcula a área de um retângulo"""
    return largura * altura

# Função que pode ser reutilizada
def calcular_perimetro_retangulo(largura, altura):
    """Calcula o perímetro de um retângulo"""
    return 2 * (largura + altura)

# Versão SEM if __name__ == "__main__"
# PROBLEMA: Se alguém importar este arquivo, este código executa também!
# print("Área:", calcular_area_retangulo(5, 3))
# print("Perímetro:", calcular_perimetro_retangulo(5, 3))

# Versão COM if __name__ == "__main__" (CORRETA)
# VANTAGEM: Só executa quando rodar diretamente, não quando importar
if __name__ == "__main__":
    print("\n📐 Cálculos de Retângulo:")
    print(f"Largura: 5, Altura: 3")
    print(f"Área: {calcular_area_retangulo(5, 3)}")
    print(f"Perímetro: {calcular_perimetro_retangulo(5, 3)}")


# ============================================================================
# PARTE 6: ESTRUTURA RECOMENDADA PARA PROGRAMAS
# ============================================================================

print("\n" + "="*60)
print("ESTRUTURA RECOMENDADA PARA PROGRAMAS PYTHON")
print("="*60)

print("""
ESTRUTURA IDEAL:

1. IMPORTS (no topo)
   import sqlite3
   import os

2. DEFINIÇÃO DE FUNÇÕES
   def funcao1():
       pass
   
   def funcao2():
       pass

3. FUNÇÃO MAIN (opcional, mas recomendado)
   def main():
       # Código principal aqui
       print("Iniciando programa...")
       funcao1()
       funcao2()

4. VERIFICAÇÃO __name__ == "__main__"
   if __name__ == "__main__":
       main()

RESUMO:
- ✅ SEMPRE use if __name__ == "__main__" para programas que podem ser importados
- ✅ Para scripts simples e rápidos, pode pular (mas não é recomendado)
- ✅ É uma BOA PRÁTICA de programação Python
- ✅ Facilita testes e organização do código
""")


# ============================================================================
# PARTE 7: TESTE - O QUE ACONTECE COM __name__?
# ============================================================================

print("\n" + "="*60)
print("TESTE: Veja o valor de __name__")
print("="*60)

print(f"Quando você roda este arquivo diretamente:")
print(f"  __name__ = '{__name__}'")
print(f"  Resultado: __name__ == '__main__' é {__name__ == '__main__'}")
print()
print("Se você importar este arquivo em outro lugar:")
print("  import explicacao_name_main")
print("  → __name__ será 'explicacao_name_main'")
print("  → O código dentro do if NÃO executa")

