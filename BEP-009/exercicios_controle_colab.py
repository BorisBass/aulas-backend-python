"""
BEP-009: Estruturas de Controle Avançadas em Python
Exercícios Práticos para Google Colab

Instruções:
- Leia atentamente cada exercício
- Implemente a solução no espaço indicado
- Teste seu código com diferentes valores
- Compare com as soluções fornecidas
"""

# ========================================
# EXERCÍCIO 1: Contador Inteligente
# ========================================
"""
Crie um programa que conte de 1 a 100, mas:
- Pule números divisíveis por 3
- Pare quando encontrar um número divisível por 7
- Mostre quantos números foram processados
"""

print("=" * 50)
print("EXERCÍCIO 1: Contador Inteligente")
print("=" * 50)

# Sua solução aqui:


# ========================================
# EXERCÍCIO 2: Busca em Lista
# ========================================
"""
Procure por um número específico em uma lista e informe:
- Se encontrou ou não
- Em qual posição encontrou
- Quantas tentativas foram necessárias
"""

print("\n" + "=" * 50)
print("EXERCÍCIO 2: Busca em Lista")
print("=" * 50)

numeros = [5, 2, 8, 1, 9, 3, 7, 4, 6]
numero_procurado = 7

# Sua solução aqui:


# ========================================
# EXERCÍCIO 3: Tabuada Personalizada
# ========================================
"""
Crie uma tabuada que:
- Pergunte qual número multiplicar
- Pare quando o resultado for maior que 50
- Mostre apenas resultados pares
"""

print("\n" + "=" * 50)
print("EXERCÍCIO 3: Tabuada Personalizada")
print("=" * 50)

# Sua solução aqui:


# ========================================
# EXERCÍCIO 4: Sistema de Login com Tentativas
# ========================================
"""
Crie um sistema de login que:
- Permita 3 tentativas de senha
- Pare quando a senha estiver correta
- Informe quantas tentativas restam
- Bloqueie a conta após 3 tentativas
"""

print("\n" + "=" * 50)
print("EXERCÍCIO 4: Sistema de Login")
print("=" * 50)

senha_correta = "python123"

# Sua solução aqui:


# ========================================
# EXERCÍCIO 5: Processamento de Dados
# ========================================
"""
Processe uma lista de números e:
- Some apenas números positivos
- Pare quando encontrar um número negativo
- Mostre a soma e quantos números foram processados
"""

print("\n" + "=" * 50)
print("EXERCÍCIO 5: Processamento de Dados")
print("=" * 50)

numeros = [5, 3, 8, -2, 7, 1, 9]

# Sua solução aqui:


# ========================================
# EXERCÍCIO 6: Gerador de Padrões
# ========================================
"""
Crie um padrão de asteriscos que:
- Tenha 5 linhas
- Cada linha tenha o número de asteriscos igual ao número da linha
- Use loops aninhados
"""

print("\n" + "=" * 50)
print("EXERCÍCIO 6: Gerador de Padrões")
print("=" * 50)

# Sua solução aqui:


# ========================================
# EXERCÍCIO 7: Validador de Senha
# ========================================
"""
Crie um validador que verifique se uma senha:
- Tem pelo menos 8 caracteres
- Contém pelo menos um número
- Contém pelo menos uma letra maiúscula
- Contém pelo menos uma letra minúscula
"""

print("\n" + "=" * 50)
print("EXERCÍCIO 7: Validador de Senha")
print("=" * 50)

senhas_teste = ["12345678", "abcdefgh", "ABCDEFGH", "Abc123", "Abc12345"]

# Sua solução aqui:


# ========================================
# EXERCÍCIO 8: Calculadora de Estatísticas
# ========================================
"""
Calcule estatísticas de uma lista de números:
- Média dos números positivos
- Maior e menor número
- Quantos números são pares
- Pare se encontrar um número negativo
"""

print("\n" + "=" * 50)
print("EXERCÍCIO 8: Calculadora de Estatísticas")
print("=" * 50)

numeros = [5, 3, 8, 2, 7, 1, 9, -1, 4, 6]

# Sua solução aqui:


# ========================================
# EXERCÍCIO 9: Jogo da Forca Simplificado
# ========================================
"""
Crie um jogo da forca que:
- Tenha uma palavra secreta
- Permita 5 tentativas de letras
- Mostre as letras acertadas
- Pare quando acertar a palavra ou esgotar tentativas
"""

print("\n" + "=" * 50)
print("EXERCÍCIO 9: Jogo da Forca")
print("=" * 50)

palavra_secreta = "python"

# Sua solução aqui:


# ========================================
# EXERCÍCIO 10: Gerador de Matriz
# ========================================
"""
Crie uma matriz que:
- Tenha 4 linhas e 4 colunas
- Elementos da diagonal principal sejam 1
- Elementos da diagonal secundária sejam 2
- Outros elementos sejam 0
"""

print("\n" + "=" * 50)
print("EXERCÍCIO 10: Gerador de Matriz")
print("=" * 50)

# Sua solução aqui:


# ========================================
# EXERCÍCIO 11: Sistema de Vendas
# ========================================
"""
Crie um sistema que:
- Processe uma lista de vendas
- Calcule o total de vendas
- Pare quando encontrar uma venda negativa
- Mostre estatísticas finais
"""

print("\n" + "=" * 50)
print("EXERCÍCIO 11: Sistema de Vendas")
print("=" * 50)

vendas = [100, 150, 200, -50, 300, 250, 180]

# Sua solução aqui:


# ========================================
# EXERCÍCIO 12: Gerador de Sequências
# ========================================
"""
Gere sequências numéricas que:
- Comecem em 1
- Incrementem de 2 em 2
- Parem quando o número for maior que 20
- Mostrem apenas números ímpares
"""

print("\n" + "=" * 50)
print("EXERCÍCIO 12: Gerador de Sequências")
print("=" * 50)

# Sua solução aqui:


# ========================================
# EXERCÍCIOS DESAFIO
# ========================================

# ========================================
# DESAFIO 1: Calculadora de Fibonacci
# ========================================
"""
Crie um programa que:
- Gere os primeiros N números da sequência de Fibonacci
- Pare quando o número for maior que 1000
- Use um loop while
"""

print("\n" + "=" * 50)
print("DESAFIO 1: Calculadora de Fibonacci")
print("=" * 50)

# Sua solução aqui:


# ========================================
# DESAFIO 2: Verificador de Números Primos
# ========================================
"""
Crie um programa que:
- Verifique se um número é primo
- Use loops para verificar divisibilidade
- Use break para otimizar a verificação
"""

print("\n" + "=" * 50)
print("DESAFIO 2: Verificador de Números Primos")
print("=" * 50)

numeros_teste = [2, 3, 4, 5, 11, 15, 17, 20, 23, 25]

# Sua solução aqui:


# ========================================
# DESAFIO 3: Sistema de Carrinho de Compras
# ========================================
"""
Crie um sistema que:
- Permita adicionar produtos ao carrinho
- Calcule o total da compra
- Aplique descontos conforme regras
- Use while True e break para controlar o menu
"""

print("\n" + "=" * 50)
print("DESAFIO 3: Sistema de Carrinho de Compras")
print("=" * 50)

# Sua solução aqui:


# ========================================
# DESAFIO 4: Jogo de Adivinhação Avançado
# ========================================
"""
Crie um jogo que:
- Gere um número aleatório entre 1 e 100
- Dê dicas (maior/menor)
- Conte tentativas
- Tenha limite de tentativas
- Permita jogar novamente
"""

print("\n" + "=" * 50)
print("DESAFIO 4: Jogo de Adivinhação Avançado")
print("=" * 50)

# Sua solução aqui:


# ========================================
# DESAFIO 5: Analisador de Texto
# ========================================
"""
Crie um programa que:
- Analise um texto
- Conte vogais, consoantes e números
- Use continue para pular espaços e pontuação
- Mostre estatísticas detalhadas
"""

print("\n" + "=" * 50)
print("DESAFIO 5: Analisador de Texto")
print("=" * 50)

texto = "Python é uma linguagem de programação incrível! Versão 3.12"

# Sua solução aqui:


print("\n" + "=" * 50)
print("FIM DOS EXERCÍCIOS")
print("=" * 50)
print("\nParabéns por completar os exercícios!")
print("Continue praticando para dominar estruturas de controle!")
print("Próxima aula: BEP-010 - Tratamento de Exceções")


