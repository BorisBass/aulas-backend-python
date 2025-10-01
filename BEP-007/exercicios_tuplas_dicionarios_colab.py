# Exercícios Práticos: Tuplas e Dicionários em Python

# =============================================================================
# PARTE 1: EXERCÍCIOS COM TUPLAS
# =============================================================================

print("=" * 60)
print("PARTE 1: EXERCÍCIOS COM TUPLAS")
print("=" * 60)

# Exercício 1: Criação de Tuplas
# Crie uma tupla com seus dados pessoais (nome, idade, cidade, profissão).

print("\nExercício 1: Criação de Tuplas")
print("-" * 40)

# Solução:
dados_pessoais = ("João Silva", 25, "Salvador", "Programador")
print("Dados pessoais:", dados_pessoais)
print("Tipo:", type(dados_pessoais))

# Acessando elementos
print(f"Nome: {dados_pessoais[0]}")
print(f"Idade: {dados_pessoais[1]}")
print(f"Cidade: {dados_pessoais[2]}")
print(f"Profissão: {dados_pessoais[3]}")

print("\n" + "=" * 50 + "\n")

# Exercício 2: Tupla de Coordenadas
# Crie uma tupla representando coordenadas geográficas (latitude, longitude).

print("Exercício 2: Tupla de Coordenadas")
print("-" * 40)

# Solução:
coordenadas = (-12.9714, -38.5014)  # Salvador, BA
print("Coordenadas:", coordenadas)
print(f"Latitude: {coordenadas[0]}")
print(f"Longitude: {coordenadas[1]}")

# Desempacotamento
lat, lon = coordenadas
print(f"Desempacotamento - Lat: {lat}, Lon: {lon}")

print("\n" + "=" * 50 + "\n")

# Exercício 3: Fatiamento de Tuplas
# Dada a tupla (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), extraia os elementos do índice 2 ao 7.

print("Exercício 3: Fatiamento de Tuplas")
print("-" * 40)

# Solução:
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Tupla original:", numeros)

fatiamento = numeros[2:7]  # Do índice 2 ao 6 (7 exclusivo)
print("Fatiamento [2:7]:", fatiamento)

# Outros exemplos de fatiamento
print("Primeiros 3 elementos:", numeros[:3])
print("Últimos 3 elementos:", numeros[-3:])
print("Elementos pares (índices pares):", numeros[::2])

print("\n" + "=" * 50 + "\n")

# Exercício 4: Métodos de Tuplas
# Crie uma tupla com elementos repetidos e use count() e index().

print("Exercício 4: Métodos de Tuplas")
print("-" * 40)

# Solução:
cores = ("vermelho", "azul", "verde", "azul", "amarelo", "azul", "roxo")
print("Tupla de cores:", cores)

# Contando ocorrências
print(f"Quantidade de 'azul': {cores.count('azul')}")
print(f"Quantidade de 'verde': {cores.count('verde')}")
print(f"Quantidade de 'preto': {cores.count('preto')}")

# Encontrando índices
print(f"Primeira posição de 'azul': {cores.index('azul')}")
print(f"Primeira posição de 'verde': {cores.index('verde')}")

print("\n" + "=" * 50 + "\n")

# Exercício 5: Operações com Tuplas
# Crie duas tuplas e realize operações de concatenação e repetição.

print("Exercício 5: Operações com Tuplas")
print("-" * 40)

# Solução:
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
print("Tupla 1:", tupla1)
print("Tupla 2:", tupla2)

# Concatenação
concatenada = tupla1 + tupla2
print("Concatenação:", concatenada)

# Repetição
repetida = tupla1 * 3
print("Repetição (tupla1 * 3):", repetida)

print("\n" + "=" * 50 + "\n")

# Exercício 6: Funções Built-in com Tuplas
# Crie uma tupla com números e use len(), max(), min(), sum().

print("Exercício 6: Funções Built-in com Tuplas")
print("-" * 40)

# Solução:
notas = (8.5, 7.0, 9.2, 6.8, 8.0, 7.5, 9.0)
print("Tupla de notas:", notas)

print(f"Quantidade de notas: {len(notas)}")
print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}")
print(f"Soma das notas: {sum(notas)}")
print(f"Média das notas: {sum(notas) / len(notas):.2f}")

print("\n" + "=" * 50 + "\n")

# Exercício 7: Tupla Aninhada
# Crie uma tupla contendo outras tuplas (coordenadas de múltiplos pontos).

print("Exercício 7: Tupla Aninhada")
print("-" * 40)

# Solução:
pontos = (
    (0, 0),      # Origem
    (3, 4),      # Ponto A
    (6, 8),      # Ponto B
    (9, 12)      # Ponto C
)

print("Pontos:", pontos)
print(f"Primeiro ponto: {pontos[0]}")
print(f"Coordenada X do segundo ponto: {pontos[1][0]}")
print(f"Coordenada Y do segundo ponto: {pontos[1][1]}")

# Calculando distâncias da origem
for i, ponto in enumerate(pontos):
    x, y = ponto
    distancia = (x**2 + y**2)**0.5
    print(f"Ponto {i}: {ponto} - Distância da origem: {distancia:.2f}")

print("\n" + "=" * 50 + "\n")

# =============================================================================
# PARTE 2: EXERCÍCIOS COM DICIONÁRIOS
# =============================================================================

print("=" * 60)
print("PARTE 2: EXERCÍCIOS COM DICIONÁRIOS")
print("=" * 60)

# Exercício 8: Criação de Dicionários
# Crie um dicionário representando um contato telefônico.

print("\nExercício 8: Criação de Dicionários")
print("-" * 40)

# Solução:
contato = {
    "nome": "Maria Santos",
    "telefone": "(71) 99999-8888",
    "email": "maria@email.com",
    "cidade": "Salvador"
}

print("Contato:", contato)
print("Tipo:", type(contato))

# Acessando valores
print(f"Nome: {contato['nome']}")
print(f"Telefone: {contato['telefone']}")
print(f"Email: {contato['email']}")

print("\n" + "=" * 50 + "\n")

# Exercício 9: Acesso Seguro a Dicionários
# Use o método get() para acessar valores de forma segura.

print("Exercício 9: Acesso Seguro a Dicionários")
print("-" * 40)

# Solução:
pessoa = {
    "nome": "João",
    "idade": 30,
    "profissao": "Engenheiro"
}

print("Dados da pessoa:", pessoa)

# Acesso seguro com get()
print(f"Nome: {pessoa.get('nome', 'Não informado')}")
print(f"Idade: {pessoa.get('idade', 'Não informado')}")
print(f"Salário: {pessoa.get('salario', 'Não informado')}")

# Verificando existência de chaves
print(f"'nome' existe: {'nome' in pessoa}")
print(f"'salario' existe: {'salario' in pessoa}")

print("\n" + "=" * 50 + "\n")

# Exercício 10: Adição e Modificação
# Crie um dicionário vazio e adicione/modifique elementos.

print("Exercício 10: Adição e Modificação")
print("-" * 40)

# Solução:
produto = {}
print("Dicionário vazio:", produto)

# Adicionando elementos
produto["nome"] = "Notebook"
produto["preco"] = 2500.00
produto["marca"] = "TechCorp"
print("Após adicionar elementos:", produto)

# Modificando elementos
produto["preco"] = 2200.00  # Desconto
produto["estoque"] = 15     # Novo campo
print("Após modificações:", produto)

# Usando update() para múltiplas alterações
produto.update({
    "categoria": "Eletrônicos",
    "garantia": "12 meses"
})
print("Após update():", produto)

print("\n" + "=" * 50 + "\n")

# Exercício 11: Remoção de Elementos
# Crie um dicionário e remova elementos usando diferentes métodos.

print("Exercício 11: Remoção de Elementos")
print("-" * 40)

# Solução:
aluno = {
    "nome": "Ana Costa",
    "matricula": "2024001",
    "curso": "Ciência da Computação",
    "semestre": 3,
    "nota1": 8.5,
    "nota2": 7.0,
    "nota3": 9.2
}

print("Dados do aluno:", aluno)

# Removendo com del
del aluno["semestre"]
print("Após remover 'semestre' com del:", aluno)

# Removendo com pop() e retornando o valor
nota_removida = aluno.pop("nota3")
print(f"Nota removida: {nota_removida}")
print("Após remover 'nota3' com pop():", aluno)

# Removendo com popitem() (remove item arbitrário)
item_removido = aluno.popitem()
print(f"Item removido: {item_removido}")
print("Após popitem():", aluno)

print("\n" + "=" * 50 + "\n")

# Exercício 12: Agenda Telefônica
# Crie uma agenda telefônica com múltiplos contatos.

print("Exercício 12: Agenda Telefônica")
print("-" * 40)

# Solução:
agenda = {
    "João Silva": {
        "telefone": "(71) 99999-1111",
        "email": "joao@email.com",
        "cidade": "Salvador"
    },
    "Maria Santos": {
        "telefone": "(71) 99999-2222",
        "email": "maria@email.com",
        "cidade": "Feira de Santana"
    },
    "Pedro Costa": {
        "telefone": "(71) 99999-3333",
        "email": "pedro@email.com",
        "cidade": "Salvador"
    }
}

print("Agenda telefônica:")
for nome, dados in agenda.items():
    print(f"\n{nome}:")
    print(f"  Telefone: {dados['telefone']}")
    print(f"  Email: {dados['email']}")
    print(f"  Cidade: {dados['cidade']}")

# Buscando um contato específico
nome_busca = "Maria Santos"
if nome_busca in agenda:
    print(f"\nContato encontrado: {nome_busca}")
    print(f"Telefone: {agenda[nome_busca]['telefone']}")
else:
    print(f"\nContato '{nome_busca}' não encontrado")

print("\n" + "=" * 50 + "\n")

# Exercício 13: Sistema de Notas
# Crie um sistema de notas usando dicionários.

print("Exercício 13: Sistema de Notas")
print("-" * 40)

# Solução:
notas_alunos = {
    "Ana": [8.5, 7.0, 9.2],
    "Bruno": [6.8, 8.0, 7.5],
    "Carla": [9.0, 8.5, 9.5],
    "Diego": [7.2, 6.5, 8.0]
}

print("Sistema de Notas:")
print("-" * 20)

for aluno, notas in notas_alunos.items():
    media = sum(notas) / len(notas)
    status = "Aprovado" if media >= 7.0 else "Reprovado"
    
    print(f"{aluno}:")
    print(f"  Notas: {notas}")
    print(f"  Média: {media:.2f}")
    print(f"  Status: {status}")
    print()

print("\n" + "=" * 50 + "\n")

# Exercício 14: Inventário de Produtos
# Crie um inventário de produtos com controle de estoque.

print("Exercício 14: Inventário de Produtos")
print("-" * 40)

# Solução:
inventario = {
    "notebook": {
        "preco": 2500.00,
        "estoque": 10,
        "categoria": "Eletrônicos"
    },
    "mouse": {
        "preco": 50.00,
        "estoque": 25,
        "categoria": "Acessórios"
    },
    "teclado": {
        "preco": 120.00,
        "estoque": 15,
        "categoria": "Acessórios"
    },
    "monitor": {
        "preco": 800.00,
        "estoque": 8,
        "categoria": "Eletrônicos"
    }
}

print("Inventário de Produtos:")
print("-" * 25)

total_valor = 0
for produto, dados in inventario.items():
    valor_produto = dados["preco"] * dados["estoque"]
    total_valor += valor_produto
    
    print(f"{produto.title()}:")
    print(f"  Preço: R$ {dados['preco']:.2f}")
    print(f"  Estoque: {dados['estoque']} unidades")
    print(f"  Categoria: {dados['categoria']}")
    print(f"  Valor total: R$ {valor_produto:.2f}")
    print()

print(f"Valor total do inventário: R$ {total_valor:.2f}")

print("\n" + "=" * 50 + "\n")

# Exercício 15: Métodos de Dicionários
# Explore os métodos keys(), values(), items() e outros.

print("Exercício 15: Métodos de Dicionários")
print("-" * 40)

# Solução:
pessoa = {
    "nome": "Carlos",
    "idade": 35,
    "profissao": "Médico",
    "cidade": "Salvador",
    "salario": 15000.00
}

print("Dados da pessoa:", pessoa)

# Métodos principais
print(f"\nChaves: {list(pessoa.keys())}")
print(f"Valores: {list(pessoa.values())}")
print(f"Items: {list(pessoa.items())}")

# Iterando sobre chaves
print("\nIterando sobre chaves:")
for chave in pessoa.keys():
    print(f"  {chave}: {pessoa[chave]}")

# Iterando sobre valores
print("\nIterando sobre valores:")
for valor in pessoa.values():
    print(f"  {valor}")

# Iterando sobre items
print("\nIterando sobre items:")
for chave, valor in pessoa.items():
    print(f"  {chave}: {valor}")

print("\n" + "=" * 50 + "\n")

# Exercício 16: Funções Built-in com Dicionários
# Use len(), max(), min() e outras funções com dicionários.

print("Exercício 16: Funções Built-in com Dicionários")
print("-" * 40)

# Solução:
vendas = {
    "janeiro": 15000,
    "fevereiro": 18000,
    "marco": 12000,
    "abril": 22000,
    "maio": 19000
}

print("Vendas por mês:", vendas)

print(f"\nQuantidade de meses: {len(vendas)}")
print(f"Maior venda: {max(vendas.values())}")
print(f"Menor venda: {min(vendas.values())}")
print(f"Total de vendas: {sum(vendas.values())}")
print(f"Média de vendas: {sum(vendas.values()) / len(vendas):.2f}")

# Encontrando o mês com maior venda
mes_maior_venda = max(vendas, key=vendas.get)
print(f"Mês com maior venda: {mes_maior_venda} ({vendas[mes_maior_venda]})")

print("\n" + "=" * 50 + "\n")

# Exercício 17: Exercício Combinado
# Crie um sistema que combine tuplas e dicionários.

print("Exercício 17: Exercício Combinado")
print("-" * 40)

# Solução:
# Sistema de coordenadas de cidades com informações adicionais
cidades = {
    "Salvador": {
        "coordenadas": (-12.9714, -38.5014),
        "populacao": 2886698,
        "estado": "BA"
    },
    "São Paulo": {
        "coordenadas": (-23.5505, -46.6333),
        "populacao": 12396372,
        "estado": "SP"
    },
    "Rio de Janeiro": {
        "coordenadas": (-22.9068, -43.1729),
        "populacao": 6775561,
        "estado": "RJ"
    }
}

print("Sistema de Cidades:")
print("-" * 20)

for cidade, dados in cidades.items():
    lat, lon = dados["coordenadas"]  # Desempacotamento da tupla
    print(f"{cidade} ({dados['estado']}):")
    print(f"  Coordenadas: {lat}, {lon}")
    print(f"  População: {dados['populacao']:,}")
    print()

# Calculando distância entre Salvador e São Paulo (aproximada)
salvador = cidades["Salvador"]["coordenadas"]
sp = cidades["São Paulo"]["coordenadas"]

# Fórmula simplificada para distância
import math
distancia = math.sqrt((salvador[0] - sp[0])**2 + (salvador[1] - sp[1])**2)
print(f"Distância aproximada Salvador-SP: {distancia:.2f} graus")

print("\n" + "=" * 50 + "\n")

# Exercício 18: Sistema de Login
# Crie um sistema simples de login usando dicionários.

print("Exercício 18: Sistema de Login")
print("-" * 40)

# Solução:
usuarios = {
    "admin": {
        "senha": "123456",
        "nivel": "administrador",
        "ativo": True
    },
    "usuario1": {
        "senha": "senha123",
        "nivel": "usuario",
        "ativo": True
    },
    "usuario2": {
        "senha": "minhasenha",
        "nivel": "usuario",
        "ativo": False
    }
}

def verificar_login(usuario, senha):
    if usuario in usuarios:
        dados = usuarios[usuario]
        if dados["senha"] == senha and dados["ativo"]:
            return True, dados["nivel"]
        elif not dados["ativo"]:
            return False, "Usuário inativo"
        else:
            return False, "Senha incorreta"
    else:
        return False, "Usuário não encontrado"

# Testando o sistema
print("Testando sistema de login:")
print("-" * 25)

# Teste 1: Login válido
resultado, info = verificar_login("admin", "123456")
print(f"Login 'admin': {'Sucesso' if resultado else 'Falha'} - {info}")

# Teste 2: Senha incorreta
resultado, info = verificar_login("usuario1", "senha_errada")
print(f"Login 'usuario1' (senha errada): {'Sucesso' if resultado else 'Falha'} - {info}")

# Teste 3: Usuário inativo
resultado, info = verificar_login("usuario2", "minhasenha")
print(f"Login 'usuario2' (inativo): {'Sucesso' if resultado else 'Falha'} - {info}")

# Teste 4: Usuário inexistente
resultado, info = verificar_login("inexistente", "qualquer")
print(f"Login 'inexistente': {'Sucesso' if resultado else 'Falha'} - {info}")

print("\n" + "=" * 50 + "\n")

print("=" * 60)
print("FIM DOS EXERCÍCIOS!")
print("Continue praticando para dominar tuplas e dicionários em Python!")
print("=" * 60)
