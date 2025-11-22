# Respostas dos Exercícios - BEP-022: Tratamento de Exceções em POO

Este documento contém as respostas completas para todos os exercícios propostos na BEP-022.

---

## Exercício 1: Calculadora Segura

**Objetivo:** Criar uma classe `Calculadora` com tratamento de exceções para operações matemáticas.

### Solução:

```python
class Calculadora:
    """Calculadora com tratamento de exceções"""
    
    def somar(self, a, b):
        """Soma dois números"""
        try:
            return float(a) + float(b)
        except (ValueError, TypeError) as e:
            raise ValueError(f"❌ Erro: Valores devem ser numéricos! ({e})")
    
    def subtrair(self, a, b):
        """Subtrai dois números"""
        try:
            return float(a) - float(b)
        except (ValueError, TypeError) as e:
            raise ValueError(f"❌ Erro: Valores devem ser numéricos! ({e})")
    
    def multiplicar(self, a, b):
        """Multiplica dois números"""
        try:
            return float(a) * float(b)
        except (ValueError, TypeError) as e:
            raise ValueError(f"❌ Erro: Valores devem ser numéricos! ({e})")
    
    def dividir(self, a, b):
        """Divide dois números"""
        try:
            a = float(a)
            b = float(b)
            if b == 0:
                raise ZeroDivisionError("❌ Erro: Divisão por zero não permitida!")
            return a / b
        except (ValueError, TypeError) as e:
            raise ValueError(f"❌ Erro: Valores devem ser numéricos! ({e})")
        except ZeroDivisionError:
            raise

# Teste
calc = Calculadora()
try:
    print(calc.somar(10, 5))        # 15.0
    print(calc.subtrair(10, 3))      # 7.0
    print(calc.multiplicar(4, 5))    # 20.0
    print(calc.dividir(10, 2))       # 5.0
    print(calc.dividir(10, 0))       # Erro: Divisão por zero
except (ValueError, ZeroDivisionError) as e:
    print(e)
```

### Explicação:
- Todos os métodos convertem valores para `float()` e tratam `ValueError` e `TypeError`
- O método `dividir()` verifica explicitamente divisão por zero
- Mensagens de erro claras e específicas
- Exceções são relançadas para permitir tratamento externo

---

## Exercício 2: Validador de Dados

**Objetivo:** Criar uma classe `Validador` com métodos de validação que tratam exceções.

### Solução:

```python
class Validador:
    """Validador de dados com tratamento de exceções"""
    
    def validar_idade(self, idade):
        """Valida idade entre 0 e 150"""
        try:
            idade = int(idade)
            if idade < 0 or idade > 150:
                raise ValueError(f"❌ Idade inválida: {idade}. Deve estar entre 0 e 150.")
            return True
        except ValueError as e:
            if "invalid literal" in str(e):
                raise ValueError(f"❌ Idade deve ser um número inteiro!")
            raise
    
    def validar_email(self, email):
        """Valida formato de email"""
        try:
            if not isinstance(email, str):
                raise TypeError("❌ Email deve ser uma string!")
            
            if '@' not in email:
                raise ValueError("❌ Email inválido: deve conter '@'")
            
            partes = email.split('@')
            if len(partes) != 2:
                raise ValueError("❌ Email inválido: formato incorreto")
            
            if '.' not in partes[1]:
                raise ValueError("❌ Email inválido: domínio deve conter '.'")
            
            return True
        except (TypeError, ValueError) as e:
            raise
    
    def validar_telefone(self, telefone):
        """Valida telefone com pelo menos 10 dígitos"""
        try:
            if not isinstance(telefone, str):
                raise TypeError("❌ Telefone deve ser uma string!")
            
            # Remove caracteres não numéricos
            digitos = ''.join(filter(str.isdigit, telefone))
            
            if len(digitos) < 10:
                raise ValueError(f"❌ Telefone inválido: deve ter pelo menos 10 dígitos (encontrados {len(digitos)})")
            
            return True
        except (TypeError, ValueError) as e:
            raise

# Teste
validador = Validador()

try:
    print(validador.validar_idade(25))           # True
    print(validador.validar_idade(200))          # Erro
    print(validador.validar_email("user@mail.com"))  # True
    print(validador.validar_email("email_invalido"))  # Erro
    print(validador.validar_telefone("(71) 99999-9999"))  # True
    print(validador.validar_telefone("123"))     # Erro
except (ValueError, TypeError) as e:
    print(e)
```

### Explicação:
- Cada método valida um tipo específico de dado
- Tratamento de exceções para valores inválidos
- Mensagens de erro descritivas
- Retorna `True` quando válido, lança exceção quando inválido

---

## Exercício 3: Gerenciador de Arquivos

**Objetivo:** Criar uma classe para gerenciar arquivos com tratamento de exceções e uso de `finally`.

### Solução:

```python
class GerenciadorArquivo:
    """Gerenciador de arquivos com tratamento de exceções"""
    
    def ler_arquivo(self, caminho):
        """Lê conteúdo de um arquivo"""
        arquivo = None
        try:
            arquivo = open(caminho, 'r', encoding='utf-8')
            conteudo = arquivo.read()
            return conteudo
        except FileNotFoundError:
            raise FileNotFoundError(f"❌ Arquivo não encontrado: {caminho}")
        except PermissionError:
            raise PermissionError(f"❌ Sem permissão para ler o arquivo: {caminho}")
        except IOError as e:
            raise IOError(f"❌ Erro de I/O ao ler arquivo: {e}")
        finally:
            if arquivo:
                arquivo.close()
                print(f"✅ Arquivo {caminho} fechado com sucesso")
    
    def escrever_arquivo(self, caminho, conteudo):
        """Escreve conteúdo em um arquivo"""
        arquivo = None
        try:
            arquivo = open(caminho, 'w', encoding='utf-8')
            arquivo.write(conteudo)
            print(f"✅ Conteúdo escrito em {caminho}")
        except PermissionError:
            raise PermissionError(f"❌ Sem permissão para escrever no arquivo: {caminho}")
        except IOError as e:
            raise IOError(f"❌ Erro de I/O ao escrever arquivo: {e}")
        finally:
            if arquivo:
                arquivo.close()
                print(f"✅ Arquivo {caminho} fechado com sucesso")
    
    def copiar_arquivo(self, origem, destino):
        """Copia um arquivo"""
        arquivo_origem = None
        arquivo_destino = None
        try:
            # Ler arquivo origem
            arquivo_origem = open(origem, 'r', encoding='utf-8')
            conteudo = arquivo_origem.read()
            
            # Escrever arquivo destino
            arquivo_destino = open(destino, 'w', encoding='utf-8')
            arquivo_destino.write(conteudo)
            
            print(f"✅ Arquivo copiado de {origem} para {destino}")
        except FileNotFoundError:
            raise FileNotFoundError(f"❌ Arquivo não encontrado: {origem}")
        except PermissionError:
            raise PermissionError(f"❌ Sem permissão para acessar arquivo")
        except IOError as e:
            raise IOError(f"❌ Erro de I/O ao copiar arquivo: {e}")
        finally:
            if arquivo_origem:
                arquivo_origem.close()
            if arquivo_destino:
                arquivo_destino.close()
            print("✅ Arquivos fechados")

# Teste
gerenciador = GerenciadorArquivo()

try:
    # Escrever arquivo
    gerenciador.escrever_arquivo("teste.txt", "Conteúdo de teste")
    
    # Ler arquivo
    conteudo = gerenciador.ler_arquivo("teste.txt")
    print(f"Conteúdo lido: {conteudo}")
    
    # Copiar arquivo
    gerenciador.copiar_arquivo("teste.txt", "copia.txt")
    
    # Tentar ler arquivo inexistente
    gerenciador.ler_arquivo("inexistente.txt")
except (FileNotFoundError, PermissionError, IOError) as e:
    print(e)
```

### Explicação:
- Uso de `finally` para garantir que arquivos sejam sempre fechados
- Tratamento específico para `FileNotFoundError`, `PermissionError` e `IOError`
- Mensagens de erro claras indicando qual operação falhou
- Garantia de limpeza de recursos mesmo em caso de erro

---

## Exercício 4: Sistema Bancário com Exceções Customizadas

**Objetivo:** Criar exceções customizadas e uma classe `ContaBancaria` que as utiliza.

### Solução:

```python
# Hierarquia de Exceções Customizadas
class ErroBancario(Exception):
    """Exceção base para erros bancários"""
    pass

class SaldoInsuficienteError(ErroBancario):
    """Exceção para saldo insuficiente"""
    def __init__(self, saldo_atual, valor_solicitado):
        self.saldo_atual = saldo_atual
        self.valor_solicitado = valor_solicitado
        self.mensagem = f"❌ Saldo insuficiente! Saldo atual: R$ {saldo_atual:.2f}, Valor solicitado: R$ {valor_solicitado:.2f}"
        super().__init__(self.mensagem)

class ValorInvalidoError(ErroBancario):
    """Exceção para valor inválido"""
    def __init__(self, valor):
        self.valor = valor
        self.mensagem = f"❌ Valor inválido: R$ {valor:.2f}. Valor deve ser positivo!"
        super().__init__(self.mensagem)

class ContaNaoEncontradaError(ErroBancario):
    """Exceção para conta não encontrada"""
    def __init__(self, numero_conta):
        self.numero_conta = numero_conta
        self.mensagem = f"❌ Conta não encontrada: {numero_conta}"
        super().__init__(self.mensagem)


class ContaBancaria:
    """Conta bancária com tratamento de exceções customizadas"""
    
    def __init__(self, numero_conta, titular, saldo_inicial=0.0):
        self.numero_conta = numero_conta
        self.titular = titular
        if saldo_inicial < 0:
            raise ValorInvalidoError(saldo_inicial)
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        """Deposita valor na conta"""
        try:
            valor = float(valor)
            if valor <= 0:
                raise ValorInvalidoError(valor)
            self.saldo += valor
            print(f"✅ Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")
        except (ValueError, TypeError):
            raise ValorInvalidoError(valor)
    
    def sacar(self, valor):
        """Saca valor da conta"""
        try:
            valor = float(valor)
            if valor <= 0:
                raise ValorInvalidoError(valor)
            if valor > self.saldo:
                raise SaldoInsuficienteError(self.saldo, valor)
            self.saldo -= valor
            print(f"✅ Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")
        except (ValueError, TypeError):
            raise ValorInvalidoError(valor)
    
    def transferir(self, conta_destino, valor):
        """Transfere valor para outra conta"""
        try:
            if not isinstance(conta_destino, ContaBancaria):
                raise ContaNaoEncontradaError("Conta destino inválida")
            
            valor = float(valor)
            if valor <= 0:
                raise ValorInvalidoError(valor)
            
            # Tenta sacar da conta origem
            self.sacar(valor)
            
            # Deposita na conta destino
            conta_destino.depositar(valor)
            print(f"✅ Transferência de R$ {valor:.2f} realizada para conta {conta_destino.numero_conta}")
        except (ValueError, TypeError):
            raise ValorInvalidoError(valor)
    
    def consultar_saldo(self):
        """Consulta saldo da conta"""
        return self.saldo

# Teste
try:
    # Criar contas
    conta1 = ContaBancaria("001", "João", 1000.0)
    conta2 = ContaBancaria("002", "Maria", 500.0)
    
    # Operações válidas
    conta1.depositar(200.0)
    conta1.sacar(100.0)
    conta1.transferir(conta2, 50.0)
    
    # Operações que geram exceções
    conta1.sacar(2000.0)  # SaldoInsuficienteError
    conta1.depositar(-100)  # ValorInvalidoError
    
except ErroBancario as e:
    print(e)
```

### Explicação:
- Hierarquia de exceções: `ErroBancario` (base) → exceções específicas
- Cada exceção customizada armazena informações relevantes
- Métodos da classe lançam exceções apropriadas
- Tratamento pode ser feito pela exceção base ou específica

---

## Exercício 5: Sistema de E-commerce

**Objetivo:** Criar exceções customizadas e classes para um sistema de e-commerce.

### Solução:

```python
# Exceções Customizadas para E-commerce
class ErroEcommerce(Exception):
    """Exceção base para erros de e-commerce"""
    pass

class ProdutoIndisponivelError(ErroEcommerce):
    """Exceção para produto indisponível"""
    def __init__(self, produto_nome):
        self.produto_nome = produto_nome
        self.mensagem = f"❌ Produto '{produto_nome}' está indisponível"
        super().__init__(self.mensagem)

class EstoqueInsuficienteError(ErroEcommerce):
    """Exceção para estoque insuficiente"""
    def __init__(self, produto_nome, estoque_atual, quantidade_solicitada):
        self.produto_nome = produto_nome
        self.estoque_atual = estoque_atual
        self.quantidade_solicitada = quantidade_solicitada
        self.mensagem = f"❌ Estoque insuficiente de '{produto_nome}'. Disponível: {estoque_atual}, Solicitado: {quantidade_solicitada}"
        super().__init__(self.mensagem)

class DescontoInvalidoError(ErroEcommerce):
    """Exceção para desconto inválido"""
    def __init__(self, desconto):
        self.desconto = desconto
        self.mensagem = f"❌ Desconto inválido: {desconto}%. Deve estar entre 0 e 100"
        super().__init__(self.mensagem)


class Produto:
    """Classe representando um produto"""
    
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.disponivel = estoque > 0
    
    def verificar_disponibilidade(self):
        """Verifica se produto está disponível"""
        if not self.disponivel:
            raise ProdutoIndisponivelError(self.nome)
        return True
    
    def verificar_estoque(self, quantidade):
        """Verifica se há estoque suficiente"""
        self.verificar_disponibilidade()
        if quantidade <= 0:
            raise ValueError(f"❌ Quantidade deve ser positiva: {quantidade}")
        if quantidade > self.estoque:
            raise EstoqueInsuficienteError(self.nome, self.estoque, quantidade)
        return True
    
    def reduzir_estoque(self, quantidade):
        """Reduz estoque do produto"""
        self.verificar_estoque(quantidade)
        self.estoque -= quantidade
        if self.estoque == 0:
            self.disponivel = False


class Carrinho:
    """Carrinho de compras"""
    
    def __init__(self):
        self.itens = {}  # {produto: quantidade}
    
    def adicionar_produto(self, produto, quantidade=1):
        """Adiciona produto ao carrinho"""
        try:
            produto.verificar_estoque(quantidade)
            
            if produto in self.itens:
                nova_quantidade = self.itens[produto] + quantidade
                produto.verificar_estoque(nova_quantidade)
                self.itens[produto] = nova_quantidade
            else:
                self.itens[produto] = quantidade
            
            print(f"✅ {quantidade}x '{produto.nome}' adicionado ao carrinho")
        except (ProdutoIndisponivelError, EstoqueInsuficienteError) as e:
            raise
    
    def remover_produto(self, produto):
        """Remove produto do carrinho"""
        if produto in self.itens:
            del self.itens[produto]
            print(f"✅ '{produto.nome}' removido do carrinho")
        else:
            print(f"⚠️ Produto '{produto.nome}' não está no carrinho")
    
    def calcular_total(self, desconto=0):
        """Calcula total do carrinho com desconto"""
        try:
            if desconto < 0 or desconto > 100:
                raise DescontoInvalidoError(desconto)
            
            total = sum(produto.preco * quantidade for produto, quantidade in self.itens.items())
            
            if desconto > 0:
                valor_desconto = total * (desconto / 100)
                total -= valor_desconto
                print(f"💰 Desconto de {desconto}% aplicado: R$ {valor_desconto:.2f}")
            
            return total
        except DescontoInvalidoError:
            raise
    
    def finalizar_compra(self, desconto=0):
        """Finaliza compra e reduz estoque"""
        try:
            total = self.calcular_total(desconto)
            
            # Reduz estoque de todos os produtos
            for produto, quantidade in self.itens.items():
                produto.reduzir_estoque(quantidade)
            
            print(f"✅ Compra finalizada! Total: R$ {total:.2f}")
            self.itens.clear()
            return total
        except (EstoqueInsuficienteError, DescontoInvalidoError) as e:
            raise

# Teste
try:
    # Criar produtos
    produto1 = Produto("Notebook", 2500.0, 5)
    produto2 = Produto("Mouse", 50.0, 10)
    produto3 = Produto("Teclado", 150.0, 0)  # Indisponível
    
    # Criar carrinho
    carrinho = Carrinho()
    
    # Adicionar produtos
    carrinho.adicionar_produto(produto1, 2)
    carrinho.adicionar_produto(produto2, 3)
    
    # Calcular total com desconto
    total = carrinho.calcular_total(desconto=10)
    print(f"Total com desconto: R$ {total:.2f}")
    
    # Tentar adicionar produto indisponível
    carrinho.adicionar_produto(produto3)  # ProdutoIndisponivelError
    
    # Tentar adicionar mais do que há em estoque
    carrinho.adicionar_produto(produto1, 10)  # EstoqueInsuficienteError
    
    # Tentar desconto inválido
    carrinho.calcular_total(desconto=150)  # DescontoInvalidoError
    
    # Finalizar compra
    carrinho.finalizar_compra(desconto=5)
    
except ErroEcommerce as e:
    print(e)
```

### Explicação:
- Exceções customizadas específicas para e-commerce
- Classe `Produto` valida disponibilidade e estoque
- Classe `Carrinho` gerencia itens e calcula totais
- Tratamento de exceções em todas as operações críticas

---

## Exercício 6: Sistema de Usuários

**Objetivo:** Criar exceções customizadas e classes para um sistema de gerenciamento de usuários.

### Solução:

```python
# Exceções Customizadas para Sistema de Usuários
class ErroUsuario(Exception):
    """Exceção base para erros de usuário"""
    pass

class EmailInvalidoError(ErroUsuario):
    """Exceção para email inválido"""
    def __init__(self, email):
        self.email = email
        self.mensagem = f"❌ Email inválido: {email}"
        super().__init__(self.mensagem)

class SenhaFracaError(ErroUsuario):
    """Exceção para senha fraca"""
    def __init__(self, motivo):
        self.motivo = motivo
        self.mensagem = f"❌ Senha fraca: {motivo}"
        super().__init__(self.mensagem)

class UsuarioNaoEncontradoError(ErroUsuario):
    """Exceção para usuário não encontrado"""
    def __init__(self, identificador):
        self.identificador = identificador
        self.mensagem = f"❌ Usuário não encontrado: {identificador}"
        super().__init__(self.mensagem)

class EmailJaCadastradoError(ErroUsuario):
    """Exceção para email já cadastrado"""
    def __init__(self, email):
        self.email = email
        self.mensagem = f"❌ Email já cadastrado: {email}"
        super().__init__(self.mensagem)


class Usuario:
    """Classe representando um usuário"""
    
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = self.validar_email(email)
        self.senha = self.validar_senha(senha)
        self.ativo = True
    
    def validar_email(self, email):
        """Valida formato de email"""
        if not isinstance(email, str):
            raise EmailInvalidoError(f"{email} (deve ser string)")
        
        if '@' not in email:
            raise EmailInvalidoError(email)
        
        partes = email.split('@')
        if len(partes) != 2:
            raise EmailInvalidoError(email)
        
        if '.' not in partes[1]:
            raise EmailInvalidoError(email)
        
        return email.lower()
    
    def validar_senha(self, senha):
        """Valida força da senha"""
        if not isinstance(senha, str):
            raise SenhaFracaError("Senha deve ser uma string")
        
        if len(senha) < 8:
            raise SenhaFracaError("Senha deve ter pelo menos 8 caracteres")
        
        if not any(c.isupper() for c in senha):
            raise SenhaFracaError("Senha deve conter pelo menos uma letra maiúscula")
        
        if not any(c.islower() for c in senha):
            raise SenhaFracaError("Senha deve conter pelo menos uma letra minúscula")
        
        if not any(c.isdigit() for c in senha):
            raise SenhaFracaError("Senha deve conter pelo menos um número")
        
        return senha
    
    def autenticar(self, senha):
        """Autentica usuário com senha"""
        if not self.ativo:
            raise ValueError("❌ Usuário está inativo")
        return self.senha == senha


class SistemaUsuarios:
    """Sistema de gerenciamento de usuários"""
    
    def __init__(self):
        self.usuarios = {}  # {email: Usuario}
    
    def cadastrar(self, nome, email, senha):
        """Cadastra novo usuário"""
        try:
            # Verifica se email já existe
            if email.lower() in self.usuarios:
                raise EmailJaCadastradoError(email)
            
            # Cria usuário (validações internas)
            usuario = Usuario(nome, email, senha)
            self.usuarios[usuario.email] = usuario
            print(f"✅ Usuário '{nome}' cadastrado com sucesso!")
            return usuario
        except (EmailInvalidoError, SenhaFracaError, EmailJaCadastradoError):
            raise
    
    def buscar(self, email):
        """Busca usuário por email"""
        try:
            email = email.lower()
            if email not in self.usuarios:
                raise UsuarioNaoEncontradoError(email)
            return self.usuarios[email]
        except UsuarioNaoEncontradoError:
            raise
    
    def autenticar(self, email, senha):
        """Autentica usuário"""
        try:
            usuario = self.buscar(email)
            if usuario.autenticar(senha):
                print(f"✅ Autenticação bem-sucedida para {usuario.nome}")
                return True
            else:
                print("❌ Senha incorreta")
                return False
        except UsuarioNaoEncontradoError:
            raise
    
    def desativar_usuario(self, email):
        """Desativa um usuário"""
        try:
            usuario = self.buscar(email)
            usuario.ativo = False
            print(f"✅ Usuário {email} desativado")
        except UsuarioNaoEncontradoError:
            raise
    
    def listar_usuarios(self):
        """Lista todos os usuários"""
        if not self.usuarios:
            print("📭 Nenhum usuário cadastrado")
            return
        
        print("\n📋 Usuários Cadastrados:")
        for email, usuario in self.usuarios.items():
            status = "✅ Ativo" if usuario.ativo else "❌ Inativo"
            print(f"  - {usuario.nome} ({email}) - {status}")

# Teste
try:
    sistema = SistemaUsuarios()
    
    # Cadastrar usuários válidos
    sistema.cadastrar("João Silva", "joao@email.com", "Senha123")
    sistema.cadastrar("Maria Santos", "maria@email.com", "MinhaSenha456")
    
    # Tentar cadastrar com email inválido
    sistema.cadastrar("Pedro", "email_invalido", "Senha123")  # EmailInvalidoError
    
    # Tentar cadastrar com senha fraca
    sistema.cadastrar("Ana", "ana@email.com", "123")  # SenhaFracaError
    
    # Tentar cadastrar email duplicado
    sistema.cadastrar("João 2", "joao@email.com", "OutraSenha789")  # EmailJaCadastradoError
    
    # Buscar usuário
    usuario = sistema.buscar("joao@email.com")
    print(f"Usuário encontrado: {usuario.nome}")
    
    # Tentar buscar usuário inexistente
    sistema.buscar("inexistente@email.com")  # UsuarioNaoEncontradoError
    
    # Autenticar usuário
    sistema.autenticar("joao@email.com", "Senha123")  # Sucesso
    sistema.autenticar("joao@email.com", "SenhaErrada")  # Senha incorreta
    
    # Listar usuários
    sistema.listar_usuarios()
    
except ErroUsuario as e:
    print(e)
```

### Explicação:
- Exceções customizadas para cada tipo de erro de usuário
- Classe `Usuario` valida email e senha no construtor
- Classe `SistemaUsuarios` gerencia cadastro, busca e autenticação
- Validações rigorosas de email e senha
- Tratamento de exceções em todas as operações

---

## Resumo das Boas Práticas Aplicadas

### ✅ Tratamento de Exceções
- Uso de exceções específicas antes das genéricas
- Mensagens de erro claras e descritivas
- Informações úteis armazenadas nas exceções customizadas

### ✅ Exceções Customizadas
- Hierarquia de exceções (base → específicas)
- Nomes descritivos e informativos
- Armazenamento de dados relevantes

### ✅ Uso de Finally
- Garantia de limpeza de recursos (arquivos, conexões)
- Execução sempre, mesmo em caso de erro

### ✅ Validações
- Validação de entrada em todos os métodos críticos
- Lançamento de exceções apropriadas
- Tratamento adequado de erros

### ✅ Organização
- Código limpo e bem estruturado
- Separação de responsabilidades
- Documentação clara

---

**Bons estudos! 🚀**

