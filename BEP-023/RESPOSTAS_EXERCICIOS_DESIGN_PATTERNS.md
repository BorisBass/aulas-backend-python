# Respostas dos Exercícios - Design Patterns

Este documento contém as respostas comentadas para os exercícios propostos no slide 16 do Módulo 4.

---

## Exercício 1: Singleton para Logger

### Solução

```python
class Logger:
    """
    Logger usando padrão Singleton.
    Garante que apenas uma instância seja criada.
    """
    _instancia = None
    _inicializado = False
    
    def __new__(cls):
        """
        Método __new__ é chamado antes de __init__.
        Controla a criação da instância.
        """
        if cls._instancia is None:
            cls._instancia = super(Logger, cls).__new__(cls)
        return cls._instancia
    
    def __init__(self):
        """
        __init__ é chamado toda vez, mas só inicializamos uma vez.
        """
        if not Logger._inicializado:
            self.logs = []
            Logger._inicializado = True
    
    def log(self, mensagem, nivel="INFO"):
        """
        Adiciona um log à lista.
        
        Args:
            mensagem (str): Mensagem do log
            nivel (str): Nível do log (INFO, WARNING, ERROR)
        """
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{nivel}] {mensagem}"
        self.logs.append(log_entry)
        print(log_entry)  # Opcional: imprimir também
    
    def obter_logs(self):
        """
        Retorna todos os logs armazenados.
        
        Returns:
            list: Lista com todos os logs
        """
        return self.logs.copy()  # Retorna cópia para não modificar original
    
    def limpar_logs(self):
        """Limpa todos os logs armazenados."""
        self.logs.clear()
        print("Logs limpos!")


# Teste
if __name__ == "__main__":
    # Criar duas "instâncias" - na verdade, ambas apontam para o mesmo objeto
    logger1 = Logger()
    logger2 = Logger()
    
    # Verificar que são a mesma instância
    print(f"logger1 é logger2? {logger1 is logger2}")  # True
    
    # Adicionar logs
    logger1.log("Sistema iniciado", "INFO")
    logger2.log("Aviso: memória alta", "WARNING")
    logger1.log("Erro ao conectar", "ERROR")
    
    # Obter logs (de qualquer instância)
    todos_logs = logger2.obter_logs()
    print(f"\nTotal de logs: {len(todos_logs)}")
    for log in todos_logs:
        print(log)
    
    # Limpar logs
    logger1.limpar_logs()
    print(f"\nLogs após limpeza: {len(logger2.obter_logs())}")
```

### Explicação

- **`__new__`**: Controla a criação do objeto. Se já existe uma instância, retorna ela; caso contrário, cria uma nova.
- **`_inicializado`**: Flag para garantir que `__init__` só inicialize os atributos uma vez (já que `__init__` é chamado toda vez).
- **`is`**: Operador que verifica se duas variáveis apontam para o mesmo objeto em memória.

---

## Exercício 2: Factory de Formas Geométricas

### Solução

```python
from abc import ABC, abstractmethod
import math


# Interface/Classe abstrata para formas
class Forma(ABC):
    """Classe abstrata que define o contrato para formas geométricas."""
    
    @abstractmethod
    def calcular_area(self):
        """Calcula e retorna a área da forma."""
        pass


# Implementações concretas
class Circulo(Forma):
    """Representa um círculo."""
    
    def __init__(self, raio):
        if raio <= 0:
            raise ValueError("Raio deve ser positivo")
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * self.raio ** 2
    
    def __str__(self):
        return f"Círculo (raio={self.raio})"


class Retangulo(Forma):
    """Representa um retângulo."""
    
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
    """Representa um triângulo."""
    
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
    """Factory para criar diferentes tipos de formas geométricas."""
    
    # Tipos suportados
    TIPOS_SUPORTADOS = {
        "circulo": Circulo,
        "retangulo": Retangulo,
        "triangulo": Triangulo
    }
    
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
        tipo_lower = tipo.lower()
        
        if tipo_lower not in FormaFactory.TIPOS_SUPORTADOS:
            tipos_disponiveis = ", ".join(FormaFactory.TIPOS_SUPORTADOS.keys())
            raise ValueError(
                f"Tipo '{tipo}' não suportado. "
                f"Tipos disponíveis: {tipos_disponiveis}"
            )
        
        classe_forma = FormaFactory.TIPOS_SUPORTADOS[tipo_lower]
        
        try:
            return classe_forma(**kwargs)
        except TypeError as e:
            raise ValueError(f"Parâmetros inválidos para {tipo}: {e}")


# Teste
if __name__ == "__main__":
    # Criar formas usando Factory
    forma1 = FormaFactory.criar("circulo", raio=5)
    forma2 = FormaFactory.criar("retangulo", largura=10, altura=5)
    forma3 = FormaFactory.criar("triangulo", base=8, altura=6)
    
    print(f"{forma1}: área = {forma1.calcular_area():.2f}")
    print(f"{forma2}: área = {forma2.calcular_area():.2f}")
    print(f"{forma3}: área = {forma3.calcular_area():.2f}")
    
    # Teste de erro
    try:
        FormaFactory.criar("pentagono", lado=5)
    except ValueError as e:
        print(f"\nErro esperado: {e}")
```

### Explicação

- **Factory Pattern**: Centraliza a criação de objetos, evitando múltiplos `if/elif`.
- **Classe Abstrata (`ABC`)**: Define o contrato que todas as formas devem seguir.
- **Validação**: Factory valida tipo e parâmetros antes de criar o objeto.
- **Extensibilidade**: Fácil adicionar novos tipos de formas sem modificar código existente.

---

## Exercício 3: Observer para Sistema de Notificações

### Solução

```python
from abc import ABC, abstractmethod


# Interface para Observers
class Observer(ABC):
    """Interface que todos os observers devem implementar."""
    
    @abstractmethod
    def atualizar(self, mensagem):
        """
        Método chamado quando o subject notifica os observers.
        
        Args:
            mensagem (str): Mensagem a ser processada
        """
        pass


# Implementações concretas de Observers
class EmailObserver(Observer):
    """Observer que envia notificações por email."""
    
    def atualizar(self, mensagem):
        print(f"📧 [EMAIL] Enviando email: {mensagem}")
        # Aqui poderia ter lógica real de envio de email


class SMSObserver(Observer):
    """Observer que envia notificações por SMS."""
    
    def atualizar(self, mensagem):
        print(f"📱 [SMS] Enviando SMS: {mensagem}")
        # Aqui poderia ter lógica real de envio de SMS


class PushObserver(Observer):
    """Observer que envia notificações push."""
    
    def atualizar(self, mensagem):
        print(f"🔔 [PUSH] Enviando notificação push: {mensagem}")
        # Aqui poderia ter lógica real de notificação push


# Subject (Observable)
class NotificacaoSubject:
    """
    Subject que gerencia observers e os notifica quando necessário.
    """
    
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
            print(f"✅ Observer {observer.__class__.__name__} adicionado")
        else:
            print(f"⚠️ Observer {observer.__class__.__name__} já está registrado")
    
    def remover_observer(self, observer):
        """
        Remove um observer da lista.
        
        Args:
            observer (Observer): Observer a ser removido
        """
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"❌ Observer {observer.__class__.__name__} removido")
        else:
            print(f"⚠️ Observer {observer.__class__.__name__} não encontrado")
    
    def notificar(self, mensagem):
        """
        Notifica todos os observers registrados.
        
        Args:
            mensagem (str): Mensagem a ser enviada
        """
        print(f"\n🔔 Notificando {len(self._observers)} observer(s)...")
        for observer in self._observers:
            observer.atualizar(mensagem)
    
    def listar_observers(self):
        """Lista todos os observers registrados."""
        if not self._observers:
            print("📭 Nenhum observer registrado")
        else:
            print(f"\n📋 Observers registrados ({len(self._observers)}):")
            for observer in self._observers:
                print(f"  - {observer.__class__.__name__}")


# Teste
if __name__ == "__main__":
    # Criar subject
    sistema = NotificacaoSubject()
    
    # Criar observers
    email_obs = EmailObserver()
    sms_obs = SMSObserver()
    push_obs = PushObserver()
    
    # Registrar observers
    sistema.adicionar_observer(email_obs)
    sistema.adicionar_observer(sms_obs)
    sistema.adicionar_observer(push_obs)
    
    # Listar observers
    sistema.listar_observers()
    
    # Notificar todos
    sistema.notificar("Nova mensagem recebida!")
    
    # Remover um observer
    sistema.remover_observer(sms_obs)
    
    # Notificar novamente (agora só email e push)
    sistema.notificar("Segunda notificação")
```

### Explicação

- **Observer Pattern**: Desacopla o subject dos observers. O subject não precisa saber quais observers existem.
- **Interface (`ABC`)**: Garante que todos os observers implementem `atualizar()`.
- **Flexibilidade**: Pode adicionar/remover observers dinamicamente sem modificar o subject.
- **Extensibilidade**: Fácil adicionar novos tipos de observers (ex: WhatsApp, Telegram).

---

## Exercício 4: Identificar Padrões

### Respostas

1. **Sistema precisa garantir apenas uma conexão com banco de dados**
   - **Padrão: Singleton**
   - **Justificativa**: Garante que apenas uma instância da conexão exista, evitando múltiplas conexões desnecessárias.

2. **Precisa criar diferentes tipos de documentos (PDF, Word, HTML) dinamicamente**
   - **Padrão: Factory Method**
   - **Justificativa**: Centraliza a criação de diferentes tipos de documentos baseado em um parâmetro.

3. **Múltiplos componentes precisam ser notificados quando um arquivo é salvo**
   - **Padrão: Observer**
   - **Justificativa**: Permite que múltiplos componentes sejam notificados automaticamente quando um evento ocorre, sem acoplamento direto.

4. **Precisa adaptar uma API antiga para trabalhar com código novo**
   - **Padrão: Adapter** (não visto ainda, mas é um padrão estrutural)
   - **Justificativa**: Adapta a interface de uma classe antiga para ser compatível com código novo.

5. **Quer adicionar funcionalidades (cache, logging) a métodos sem modificar classes**
   - **Padrão: Decorator**
   - **Justificativa**: Permite adicionar funcionalidades dinamicamente sem modificar a estrutura original da classe.

---

## Exercício 5: Refatoração com Factory Pattern

### Solução

```python
from abc import ABC, abstractmethod


# Interface para métodos de pagamento
class MetodoPagamento(ABC):
    """Classe abstrata que define o contrato para métodos de pagamento."""
    
    @abstractmethod
    def processar(self, valor):
        """
        Processa o pagamento.
        
        Args:
            valor (float): Valor a ser pago
        """
        pass


# Implementações concretas
class PagamentoCredito(MetodoPagamento):
    """Processa pagamento com cartão de crédito."""
    
    def processar(self, valor):
        print(f"💳 Processando pagamento crédito: R$ {valor:.2f}")
        # Lógica específica para crédito
        return True


class PagamentoDebito(MetodoPagamento):
    """Processa pagamento com cartão de débito."""
    
    def processar(self, valor):
        print(f"💳 Processando pagamento débito: R$ {valor:.2f}")
        # Lógica específica para débito
        return True


class PagamentoPIX(MetodoPagamento):
    """Processa pagamento via PIX."""
    
    def processar(self, valor):
        print(f"📱 Processando pagamento PIX: R$ {valor:.2f}")
        # Lógica específica para PIX
        return True


class PagamentoBoleto(MetodoPagamento):
    """Processa pagamento via boleto."""
    
    def processar(self, valor):
        print(f"📄 Processando pagamento boleto: R$ {valor:.2f}")
        # Lógica específica para boleto
        return True


# Factory Pattern
class PagamentoFactory:
    """Factory para criar diferentes métodos de pagamento."""
    
    METODOS_DISPONIVEIS = {
        "credito": PagamentoCredito,
        "debito": PagamentoDebito,
        "pix": PagamentoPIX,
        "boleto": PagamentoBoleto
    }
    
    @staticmethod
    def criar_metodo(tipo):
        """
        Cria um método de pagamento baseado no tipo.
        
        Args:
            tipo (str): Tipo do método de pagamento
        
        Returns:
            MetodoPagamento: Instância do método de pagamento
        
        Raises:
            ValueError: Se o tipo não for suportado
        """
        tipo_lower = tipo.lower()
        
        if tipo_lower not in PagamentoFactory.METODOS_DISPONIVEIS:
            metodos = ", ".join(PagamentoFactory.METODOS_DISPONIVEIS.keys())
            raise ValueError(
                f"Tipo de pagamento '{tipo}' não suportado. "
                f"Métodos disponíveis: {metodos}"
            )
        
        classe_metodo = PagamentoFactory.METODOS_DISPONIVEIS[tipo_lower]
        return classe_metodo()
    
    @staticmethod
    def processar_pagamento(tipo, valor):
        """
        Método de conveniência que cria e processa o pagamento.
        
        Args:
            tipo (str): Tipo do método de pagamento
            valor (float): Valor a ser pago
        """
        metodo = PagamentoFactory.criar_metodo(tipo)
        return metodo.processar(valor)


# Teste
if __name__ == "__main__":
    # Usando o método de conveniência
    PagamentoFactory.processar_pagamento("credito", 100.00)
    PagamentoFactory.processar_pagamento("debito", 50.00)
    PagamentoFactory.processar_pagamento("pix", 25.00)
    PagamentoFactory.processar_pagamento("boleto", 200.00)
    
    # Ou criando o método e usando depois
    print("\n--- Usando método criado ---")
    pix = PagamentoFactory.criar_metodo("pix")
    pix.processar(75.50)
    
    # Teste de erro
    try:
        PagamentoFactory.processar_pagamento("paypal", 100.00)
    except ValueError as e:
        print(f"\n❌ Erro: {e}")
```

### Comparação: Antes vs. Depois

**Antes (sem padrão):**
- ❌ Múltiplos `if/elif` difíceis de manter
- ❌ Lógica de criação misturada com lógica de processamento
- ❌ Difícil adicionar novos métodos de pagamento
- ❌ Violação do princípio Open/Closed

**Depois (com Factory Pattern):**
- ✅ Código mais limpo e organizado
- ✅ Fácil adicionar novos métodos (apenas criar classe e adicionar ao dicionário)
- ✅ Separação de responsabilidades
- ✅ Respeita o princípio Open/Closed (aberto para extensão, fechado para modificação)

---

## Dicas Finais

1. **Sempre identifique o problema antes de escolher o padrão**
   - Precisa garantir uma única instância? → Singleton
   - Precisa criar objetos de diferentes tipos? → Factory
   - Precisa notificar múltiplos componentes? → Observer

2. **Comece simples e evolua**
   - Implemente a versão mais simples primeiro
   - Adicione complexidade apenas se necessário

3. **Teste suas implementações**
   - Crie exemplos práticos
   - Verifique casos de erro
   - Teste extensibilidade

4. **Documente seu código**
   - Use docstrings
   - Comente decisões importantes
   - Explique o "porquê", não apenas o "como"

---

**Bons estudos! 🚀**


