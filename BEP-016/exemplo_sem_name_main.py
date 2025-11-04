"""
EXEMPLO: Programa SEM if __name__ == "__main__"
PROBLEMA: Se você importar este arquivo, o código executa automaticamente!
"""

def saudacao(nome):
    """Função de saudação"""
    return f"Olá, {nome}!"

def calcular_idade(ano_nascimento):
    """Calcula a idade"""
    from datetime import datetime
    ano_atual = datetime.now().year
    return ano_atual - ano_nascimento

# ⚠️ PROBLEMA: Este código executa SEMPRE, mesmo quando importado!
print("=" * 50)
print("PROGRAMA SEM if __name__ == '__main__'")
print("=" * 50)
print(saudacao("João"))
print(f"Idade: {calcular_idade(2000)} anos")
print("=" * 50)

# Se você fizer: import exemplo_sem_name_main
# → Este código vai executar automaticamente!
# → Isso pode não ser o que você quer!



