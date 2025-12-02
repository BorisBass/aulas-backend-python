"""
EXEMPLO PRÁTICO: Entendendo __new__ vs __init__

Este arquivo demonstra a diferença entre __new__ e __init__
e por que __new__ é necessário no padrão Singleton.
"""

print("="*70)
print("PARTE 1: Entendendo a ordem de execução")
print("="*70)

class ExemploOrdem:
    """Classe que mostra a ordem de execução de __new__ e __init__"""
    
    def __new__(cls):
        print("  1️⃣  __new__ está sendo chamado...")
        print("     → Criando o objeto em memória")
        # Cria o objeto chamando o __new__ da classe pai (object)
        instancia = super().__new__(cls)
        print(f"     → Objeto criado! ID: {id(instancia)}")
        return instancia  # IMPORTANTE: deve retornar a instância!
    
    def __init__(self):
        print("  2️⃣  __init__ está sendo chamado...")
        print("     → Inicializando o objeto já criado")
        self.nome = "Exemplo"
        self.valor = 42

print("\n📝 Criando objeto:")
obj = ExemploOrdem()
print(f"\n✅ Objeto criado: {obj}")
print(f"   Nome: {obj.nome}, Valor: {obj.valor}")


print("\n" + "="*70)
print("PARTE 2: Por que __new__ é necessário no Singleton?")
print("="*70)

print("\n❌ TENTATIVA SEM __new__ (não funciona):")
print("-" * 70)

class LoggerSemNew:
    """Tentativa de Singleton sem __new__ - NÃO FUNCIONA"""
    _instancia = None
    
    def __init__(self):
        print("  🔧 __init__ chamado")
        if LoggerSemNew._instancia is None:
            LoggerSemNew._instancia = self
            print("  ✅ Definindo como instância única")
        else:
            print("  ⚠️  Já existe instância, mas objeto já foi criado!")

print("\nCriando l1:")
l1 = LoggerSemNew()

print("\nCriando l2:")
l2 = LoggerSemNew()

print(f"\n🔍 l1 é l2? {l1 is l2}")  # False - são objetos diferentes!
print(f"   ID de l1: {id(l1)}")
print(f"   ID de l2: {id(l2)}")
print("\n❌ PROBLEMA: Mesmo tentando controlar, criamos 2 objetos!")


print("\n" + "="*70)
print("✅ SOLUÇÃO COM __new__ (funciona!):")
print("-" * 70)

class LoggerComNew:
    """Singleton usando __new__ - FUNCIONA"""
    _instancia = None
    
    def __new__(cls):
        print("  🔨 __new__ chamado")
        if cls._instancia is None:
            print("  ✅ Primeira vez: criando instância")
            cls._instancia = super().__new__(cls)
        else:
            print("  ♻️  Já existe: retornando instância existente")
        return cls._instancia
    
    def __init__(self):
        # Só inicializa se ainda não foi inicializado
        if not hasattr(self, 'inicializado'):
            print("  🔧 Inicializando Logger...")
            self.inicializado = True
            self.logs = []
        else:
            print("  ⚠️  __init__ chamado novamente (mas já estava inicializado)")

print("\nCriando l1:")
l1 = LoggerComNew()

print("\nCriando l2:")
l2 = LoggerComNew()

print(f"\n🔍 l1 é l2? {l1 is l2}")  # True - mesma instância!
print(f"   ID de l1: {id(l1)}")
print(f"   ID de l2: {id(l2)}")
print("\n✅ SUCESSO: Apenas uma instância foi criada!")

# Testando que ambos compartilham os mesmos logs
print("\n📝 Adicionando logs:")
l1.logs.append("Log 1")
l2.logs.append("Log 2")

print(f"   Logs de l1: {l1.logs}")
print(f"   Logs de l2: {l2.logs}")
print("   ✅ Ambos compartilham os mesmos logs!")


print("\n" + "="*70)
print("PARTE 3: Comparação lado a lado")
print("="*70)

print("\n📊 RESUMO:")
print("-" * 70)
print("""
┌─────────────┬──────────────────────────┬─────────────────────────┐
│ Método      │ Quando é chamado         │ O que faz               │
├─────────────┼──────────────────────────┼─────────────────────────┤
│ __new__     │ ANTES de criar objeto    │ CRIA o objeto           │
│ __init__    │ DEPOIS de criar objeto   │ INICIALIZA o objeto     │
└─────────────┴──────────────────────────┴─────────────────────────┘

Ordem de execução:
  1. Python chama __new__() → cria objeto
  2. Python chama __init__() → inicializa objeto

Por que __new__ no Singleton?
  → __new__ controla SE o objeto é criado
  → __init__ só inicializa um objeto JÁ CRIADO
  → Para garantir uma única instância, precisamos controlar a CRIAÇÃO
""")

print("\n" + "="*70)
print("✅ Entendido! Agora você sabe por que __new__ é necessário no Singleton!")
print("="*70)

