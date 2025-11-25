# Respostas dos Exercícios - BEP-023: Introdução aos Padrões de Projeto

Este documento contém as soluções completas para os exercícios propostos na BEP-023 sobre Design Patterns.

---

## Exercício 1: Singleton para Logger

**Desafio:** Crie uma classe Logger usando o padrão Singleton que permite apenas uma instância, armazena logs em uma lista, possui métodos para logar, obter logs e limpar logs.

### Solução:

```python
class Logger:
    """
    Logger Singleton - garante apenas uma instância
    """
    _instancia = None
    _logs = []
    
    def __new__(cls):
        """
        Método especial que controla a criação de instâncias.
        Garante que apenas uma instância seja criada.
        """
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self):
        """
        Inicializa a lista de logs apenas uma vez.
        Usa flag para evitar reinicialização.
        """
        if not hasattr(self, 'inicializado'):
            self._logs = []
            self.inicializado = True
    
    def log(self, mensagem, nivel="INFO"):
        """
        Adiciona uma mensagem de log com nível especificado.
        
        Args:
            mensagem (str): Mensagem a ser logada
            nivel (str): Nível do log (INFO, WARNING, ERROR)
        """
        log_entry = f"[{nivel}] {mensagem}"
        self._logs.append(log_entry)
        print(log_entry)
    
    def obter_logs(self):
        """
        Retorna uma cópia da lista de logs.
        
        Returns:
            list: Lista de logs
        """
        return self._logs.copy()
    
    def limpar_logs(self):
        """
        Limpa todos os logs armazenados.
        """
        self._logs.clear()
        print("✅ Logs limpos!")


# Teste do Singleton
if __name__ == "__main__":
    # Criar duas "instâncias"
    logger1 = Logger()
    logger2 = Logger()
    
    # Verificar que são a mesma instância
    print(f"logger1 é logger2? {logger1 is logger2}")  # True
    
    # Usar qualquer uma das referências
    logger1.log("Primeira mensagem", "INFO")
    logger2.log("Segunda mensagem", "WARNING")
    logger1.log("Terceira mensagem", "ERROR")
    
    # Obter logs (ambos retornam os mesmos logs)
    print("\n📋 Logs do logger1:")
    for log in logger1.obter_logs():
        print(f"  {log}")
    
    print("\n📋 Logs do logger2:")
    for log in logger2.obter_logs():
        print(f"  {log}")
    
    # Limpar logs
    logger1.limpar_logs()
    print(f"\nLogs após limpeza: {len(logger2.obter_logs())}")  # 0
```

### Explicação:

1. **`__new__`**: Método especial que controla a criação de objetos. Garante que apenas uma instância seja criada.
2. **Flag `inicializado`**: Evita que `__init__` reinicialize a lista quando a mesma instância é "criada" novamente.
3. **`obter_logs()` retorna cópia**: Evita que código externo modifique a lista interna diretamente.
4. **Mesma instância**: Todas as referências apontam para o mesmo objeto, então os logs são compartilhados.

---

## Exercício 2: Factory de Formas Geométricas

**Desafio:** Crie um sistema usando Factory Pattern que cria diferentes formas geométricas (Círculo, Retângulo, Triângulo) com método `calcular_area()`.

### Solução:

```python
import math
from abc import ABC, abstractmethod


# Classe abstrata base
class Forma(ABC):
    """Classe abstrata para formas geométricas"""
    
    @abstractmethod
    def calcular_area(self):
        """Calcula a área da forma"""
        pass
    
    @abstractmethod
    def __str__(self):
        """Representação em string da forma"""
        pass


# Implementações concretas
class Circulo(Forma):
    def __init__(self, raio):
        if raio <= 0:
            raise ValueError("Raio deve ser positivo")
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * self.raio ** 2
    
    def __str__(self):
        return f"Círculo (raio={self.raio})"


class Retangulo(Forma):
    def __init__(self, largura, altura):
        if largura <= 0 or altura <= 0:
            raise ValueError("Largura e altura devem ser positivas")
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    
    def __str__(self):
        return f"Retângulo ({self.largura}x{self.altura})"


class Triangulo(Forma):
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("Base e altura devem ser positivas")
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2
    
    def __str__(self):
        return f"Triângulo (base={self.base}, altura={self.altura})"


# Factory Pattern
class FormaFactory:
    """Factory para criar formas geométricas"""
    
    @staticmethod
    def criar(tipo, **kwargs):
        """
        Cria uma forma geométrica baseada no tipo especificado.
        
        Args:
            tipo (str): Tipo da forma ("circulo", "retangulo", "triangulo")
            **kwargs: Parâmetros específicos de cada forma
        
        Returns:
            Forma: Instância da forma criada
        
        Raises:
            ValueError: Se o tipo não for suportado ou parâmetros inválidos
        """
        tipo = tipo.lower()
        
        if tipo == "circulo":
            if "raio" not in kwargs:
                raise ValueError("Círculo requer parâmetro 'raio'")
            return Circulo(kwargs["raio"])
        
        elif tipo == "retangulo":
            if "largura" not in kwargs or "altura" not in kwargs:
                raise ValueError("Retângulo requer parâmetros 'largura' e 'altura'")
            return Retangulo(kwargs["largura"], kwargs["altura"])
        
        elif tipo == "triangulo":
            if "base" not in kwargs or "altura" not in kwargs:
                raise ValueError("Triângulo requer parâmetros 'base' e 'altura'")
            return Triangulo(kwargs["base"], kwargs["altura"])
        
        else:
            raise ValueError(f"Tipo de forma '{tipo}' não suportado. "
                           f"Tipos disponíveis: circulo, retangulo, triangulo")


# Teste do Factory
if __name__ == "__main__":
    # Criar diferentes formas usando Factory
    forma1 = FormaFactory.criar("circulo", raio=5)
    forma2 = FormaFactory.criar("retangulo", largura=10, altura=5)
    forma3 = FormaFactory.criar("triangulo", base=8, altura=6)
    
    # Calcular áreas
    print(f"{forma1}: Área = {forma1.calcular_area():.2f}")
    print(f"{forma2}: Área = {forma2.calcular_area():.2f}")
    print(f"{forma3}: Área = {forma3.calcular_area():.2f}")
    
    # Teste de erro
    try:
        forma4 = FormaFactory.criar("quadrado", lado=5)
    except ValueError as e:
        print(f"\n❌ Erro esperado: {e}")
```

### Explicação:

1. **Classe abstrata `Forma`**: Define a interface comum para todas as formas.
2. **Classes concretas**: Implementam a interface com lógica específica.
3. **Factory estático**: Método `criar()` centraliza a lógica de criação.
4. **Validação**: Verifica tipo e parâmetros antes de criar.
5. **Extensibilidade**: Fácil adicionar novos tipos de formas sem modificar código existente.

---

## Exercício 3: Observer para Sistema de Notificações

**Desafio:** Implemente um sistema de notificações usando Observer Pattern com diferentes tipos de observers.

### Solução:

```python
from abc import ABC, abstractmethod


# Interface Observer
class Observer(ABC):
    """Interface para observers"""
    
    @abstractmethod
    def atualizar(self, mensagem):
        """Método chamado quando há uma notificação"""
        pass


# Implementações concretas de Observer
class EmailObserver(Observer):
    def __init__(self, email):
        self.email = email
    
    def atualizar(self, mensagem):
        print(f"📧 Email enviado para {self.email}: {mensagem}")


class SMSObserver(Observer):
    def __init__(self, numero):
        self.numero = numero
    
    def atualizar(self, mensagem):
        print(f"📱 SMS enviado para {self.numero}: {mensagem}")


class PushObserver(Observer):
    def __init__(self, token):
        self.token = token
    
    def atualizar(self, mensagem):
        print(f"🔔 Push enviado para dispositivo {self.token[:8]}...: {mensagem}")


# Subject (Observado)
class NotificacaoSubject:
    """Gerencia observers e notifica mudanças"""
    
    def __init__(self):
        self._observers = []
    
    def adicionar_observer(self, observer):
        """
        Adiciona um observer à lista.
        
        Args:
            observer (Observer): Observer a ser adicionado
        """
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"✅ Observer adicionado: {type(observer).__name__}")
        else:
            print(f"⚠️ Observer já está registrado")
    
    def remover_observer(self, observer):
        """
        Remove um observer da lista.
        
        Args:
            observer (Observer): Observer a ser removido
        """
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"❌ Observer removido: {type(observer).__name__}")
        else:
            print(f"⚠️ Observer não encontrado")
    
    def notificar(self, mensagem):
        """
        Notifica todos os observers registrados.
        
        Args:
            mensagem (str): Mensagem a ser enviada
        """
        if not self._observers:
            print("⚠️ Nenhum observer registrado")
            return
        
        print(f"\n🔔 Notificando {len(self._observers)} observer(s)...")
        for observer in self._observers:
            observer.atualizar(mensagem)


# Teste do Observer Pattern
if __name__ == "__main__":
    # Criar subject
    sistema = NotificacaoSubject()
    
    # Criar observers
    email_obs = EmailObserver("usuario@email.com")
    sms_obs = SMSObserver("(71) 99999-9999")
    push_obs = PushObserver("abc123xyz456")
    
    # Registrar observers
    sistema.adicionar_observer(email_obs)
    sistema.adicionar_observer(sms_obs)
    sistema.adicionar_observer(push_obs)
    
    # Notificar todos
    sistema.notificar("Nova mensagem recebida!")
    
    print("\n" + "="*50)
    
    # Remover um observer
    sistema.remover_observer(sms_obs)
    
    # Notificar novamente (apenas email e push)
    sistema.notificar("Segunda notificação")
```

### Explicação:

1. **Interface `Observer`**: Define o contrato que todos os observers devem seguir.
2. **Observers concretos**: Implementam `atualizar()` com comportamento específico.
3. **Subject**: Gerencia lista de observers e notifica todos quando necessário.
4. **Desacoplamento**: Subject não conhece detalhes dos observers, apenas a interface.
5. **Flexibilidade**: Fácil adicionar/remover observers dinamicamente.

---

## Exercício 4: Identificar Padrões

**Desafio:** Analise cenários e identifique qual padrão seria mais adequado.

### Respostas:

1. **Sistema precisa garantir apenas uma conexão com banco de dados**
   - **Padrão:** Singleton
   - **Justificativa:** Garante que apenas uma instância de conexão seja criada, evitando múltiplas conexões desnecessárias.

2. **Precisa criar diferentes tipos de documentos (PDF, Word, HTML) dinamicamente**
   - **Padrão:** Factory Method
   - **Justificativa:** Centraliza a criação de diferentes tipos de documentos sem expor a lógica de criação ao cliente.

3. **Múltiplos componentes precisam ser notificados quando um arquivo é salvo**
   - **Padrão:** Observer
   - **Justificativa:** Permite que múltiplos componentes sejam notificados automaticamente quando um evento ocorre (salvamento de arquivo).

4. **Precisa adaptar uma API antiga para trabalhar com código novo**
   - **Padrão:** Adapter
   - **Justificativa:** Adapta a interface antiga para ser compatível com o código novo, sem modificar o código legado.

5. **Quer adicionar funcionalidades (cache, logging) a métodos sem modificar classes**
   - **Padrão:** Decorator
   - **Justificativa:** Permite adicionar funcionalidades dinamicamente a objetos sem modificar suas classes base.

---

## Exercício 5: Refatoração com Factory Pattern

**Desafio:** Refatore o código de processamento de pagamento usando Factory Pattern.

### Solução:

```python
from abc import ABC, abstractmethod


# Classe abstrata para métodos de pagamento
class MetodoPagamento(ABC):
    """Interface para métodos de pagamento"""
    
    @abstractmethod
    def processar(self, valor):
        """
        Processa o pagamento.
        
        Args:
            valor (float): Valor a ser pago
        
        Returns:
            bool: True se processado com sucesso
        """
        pass
    
    @abstractmethod
    def __str__(self):
        """Representação do método de pagamento"""
        pass


# Implementações concretas
class PagamentoCredito(MetodoPagamento):
    def processar(self, valor):
        print(f"💳 Processando pagamento com cartão de crédito: R$ {valor:.2f}")
        # Lógica específica para crédito
        return True
    
    def __str__(self):
        return "Cartão de Crédito"


class PagamentoDebito(MetodoPagamento):
    def processar(self, valor):
        print(f"💳 Processando pagamento com cartão de débito: R$ {valor:.2f}")
        # Lógica específica para débito
        return True
    
    def __str__(self):
        return "Cartão de Débito"


class PagamentoPIX(MetodoPagamento):
    def processar(self, valor):
        print(f"📱 Processando pagamento via PIX: R$ {valor:.2f}")
        # Lógica específica para PIX
        return True
    
    def __str__(self):
        return "PIX"


class PagamentoBoleto(MetodoPagamento):
    def processar(self, valor):
        print(f"📄 Processando pagamento via boleto: R$ {valor:.2f}")
        # Lógica específica para boleto
        return True
    
    def __str__(self):
        return "Boleto"


# Factory Pattern
class PagamentoFactory:
    """Factory para criar métodos de pagamento"""
    
    @staticmethod
    def criar(tipo):
        """
        Cria um método de pagamento baseado no tipo.
        
        Args:
            tipo (str): Tipo de pagamento ("credito", "debito", "pix", "boleto")
        
        Returns:
            MetodoPagamento: Instância do método de pagamento
        
        Raises:
            ValueError: Se o tipo não for suportado
        """
        tipos = {
            "credito": PagamentoCredito,
            "debito": PagamentoDebito,
            "pix": PagamentoPIX,
            "boleto": PagamentoBoleto
        }
        
        tipo_lower = tipo.lower()
        classe = tipos.get(tipo_lower)
        
        if classe:
            return classe()
        else:
            tipos_disponiveis = ", ".join(tipos.keys())
            raise ValueError(f"Tipo de pagamento '{tipo}' não suportado. "
                           f"Tipos disponíveis: {tipos_disponiveis}")


# Função refatorada usando Factory
def processar_pagamento(tipo, valor):
    """
    Processa pagamento usando Factory Pattern.
    
    Args:
        tipo (str): Tipo de pagamento
        valor (float): Valor a ser pago
    
    Returns:
        bool: True se processado com sucesso
    """
    try:
        metodo = PagamentoFactory.criar(tipo)
        return metodo.processar(valor)
    except ValueError as e:
        print(f"❌ Erro: {e}")
        return False


# Teste da refatoração
if __name__ == "__main__":
    # Testar diferentes tipos de pagamento
    processar_pagamento("credito", 100.00)
    processar_pagamento("debito", 50.00)
    processar_pagamento("pix", 25.00)
    processar_pagamento("boleto", 200.00)
    
    # Teste de erro
    processar_pagamento("paypal", 75.00)  # Tipo não suportado
    
    print("\n" + "="*50)
    
    # Uso direto do Factory (mais flexível)
    metodo = PagamentoFactory.criar("pix")
    print(f"\nMétodo criado: {metodo}")
    metodo.processar(150.00)
```

### Comparação: Antes vs Depois

**❌ Antes (sem padrão):**
- Muitos `if/elif` aninhados
- Difícil adicionar novos tipos
- Lógica de criação misturada com lógica de processamento
- Violação do princípio Open/Closed

**✅ Depois (com Factory):**
- Código organizado e extensível
- Fácil adicionar novos tipos (apenas criar nova classe)
- Separação de responsabilidades
- Segue princípios SOLID

### Explicação:

1. **Interface `MetodoPagamento`**: Define contrato comum para todos os métodos.
2. **Classes concretas**: Cada tipo de pagamento implementa sua própria lógica.
3. **Factory centraliza criação**: Um único ponto para criar métodos de pagamento.
4. **Extensibilidade**: Adicionar novo tipo requer apenas criar nova classe e adicionar ao dicionário.
5. **Manutenibilidade**: Mudanças em um tipo não afetam outros.

---

## Exercícios Extras (Desafio)

### Exercício Extra 1: Singleton Thread-Safe

**Desafio:** Implemente um Singleton thread-safe para uso em ambientes multi-thread.

```python
import threading


class ThreadSafeLogger:
    """Logger Singleton thread-safe"""
    
    _instancia = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instancia is None:
            with cls._lock:
                # Verificar novamente dentro do lock (double-check)
                if cls._instancia is None:
                    cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self):
        if not hasattr(self, 'inicializado'):
            self._logs = []
            self._log_lock = threading.Lock()
            self.inicializado = True
    
    def log(self, mensagem):
        with self._log_lock:
            self._logs.append(mensagem)
            print(f"[LOG] {mensagem}")
```

### Exercício Extra 2: Factory com Registro Dinâmico

**Desafio:** Crie um Factory que permite registrar novos tipos dinamicamente.

```python
class FormaFactory:
    """Factory com registro dinâmico de tipos"""
    
    _tipos = {}
    
    @classmethod
    def registrar(cls, nome, classe):
        """Registra um novo tipo de forma"""
        cls._tipos[nome.lower()] = classe
    
    @classmethod
    def criar(cls, tipo, **kwargs):
        """Cria uma forma do tipo especificado"""
        tipo_lower = tipo.lower()
        classe = cls._tipos.get(tipo_lower)
        
        if classe:
            return classe(**kwargs)
        else:
            raise ValueError(f"Tipo '{tipo}' não registrado")
    
    @classmethod
    def listar_tipos(cls):
        """Lista todos os tipos registrados"""
        return list(cls._tipos.keys())


# Uso
FormaFactory.registrar("circulo", Circulo)
FormaFactory.registrar("retangulo", Retangulo)

# Adicionar novo tipo dinamicamente
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2

FormaFactory.registrar("quadrado", Quadrado)
```

---

## Conclusão

Estes exercícios demonstram a aplicação prática dos principais Design Patterns:

- **Singleton**: Para recursos únicos e compartilhados
- **Factory**: Para criação flexível de objetos
- **Observer**: Para sistemas de notificação e eventos

Lembre-se: use padrões quando eles realmente resolvem problemas, não apenas porque são "bonitos". O objetivo é código mais limpo, organizado e manutenível!

---

**Bons estudos! 🚀**


