"""
EXEMPLO: Programa COM if __name__ == "__main__"
SOLUÇÃO: O código só executa quando rodado diretamente!
"""

def saudacao(nome):
    """Função de saudação"""
    return f"Olá, {nome}!"

def calcular_idade(ano_nascimento):
    """Calcula a idade"""
    from datetime import datetime
    ano_atual = datetime.now().year
    return ano_atual - ano_nascimento

# ✅ SOLUÇÃO: Este código só executa quando você roda o arquivo diretamente
if __name__ == "__main__":
    print("=" * 50)
    print("PROGRAMA COM if __name__ == '__main__'")
    print("=" * 50)
    print(saudacao("Maria"))
    print(f"Idade: {calcular_idade(1995)} anos")
    print("=" * 50)

# Se você fizer: import exemplo_com_name_main
# → As funções ficam disponíveis (saudacao, calcular_idade)
# → Mas o código dentro do if NÃO executa automaticamente!
# → Você pode usar as funções sem executar o código de teste



