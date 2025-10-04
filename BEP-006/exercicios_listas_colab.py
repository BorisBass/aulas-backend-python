# Exercícios Práticos: Trabalhando com Listas em Python

# Exercício 1: Lista de Compras
# Crie uma lista vazia chamada "compras" e adicione 5 itens usando o método append().

print("Exercício 1: Lista de Compras")
print("-" * 30)

# Solução:
compras = []
compras.append("pão")
compras.append("leite")
compras.append("ovos")
compras.append("açúcar")
compras.append("café")

print("Lista de compras:", compras)

print("\n" + "=" * 50 + "\n")

# Exercício 2: Inserir no Meio
# Dada a lista [1, 2, 4, 5], use insert() para adicionar o número 3 na posição correta.

print("Exercício 2: Inserir no Meio")
print("-" * 30)

# Solução:
numeros = [1, 2, 4, 5]
print("Lista original:", numeros)

numeros.insert(2, 3)  # Insere 3 na posição 2
print("Lista após inserir 3:", numeros)

print("\n" + "=" * 50 + "\n")

# Exercício 3: Remover Elemento
# Crie uma lista com frutas duplicadas e remova apenas a primeira ocorrência de "banana".

print("Exercício 3: Remover Elemento")
print("-" * 30)

# Solução:
frutas = ["maçã", "banana", "laranja", "banana", "uva"]
print("Lista original:", frutas)

frutas.remove("banana")  # Remove a primeira ocorrência
print("Lista após remover primeira 'banana':", frutas)

print("\n" + "=" * 50 + "\n")

# Exercício 4: Fatiamento Básico
# Dada a lista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], extraia os elementos do índice 3 ao 7.

print("Exercício 4: Fatiamento Básico")
print("-" * 30)

# Solução:
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Lista original:", numeros)

fatiamento = numeros[3:7]  # Do índice 3 ao 6 (7 exclusivo)
print("Fatiamento [3:7]:", fatiamento)

print("\n" + "=" * 50 + "\n")

# Exercício 5: Lista de Notas
# Crie uma lista com 5 notas, calcule a média e adicione a média na lista usando append().

print("Exercício 5: Lista de Notas")
print("-" * 30)

# Solução:
notas = [8.5, 7.0, 9.2, 6.8, 8.0]
print("Notas originais:", notas)

# Calculando a média
soma = sum(notas)
media = soma / len(notas)
print(f"Média calculada: {media:.2f}")

# Adicionando a média à lista
notas.append(media)
print("Lista com a média adicionada:", notas)

print("\n" + "=" * 50 + "\n")

# Exercício 6: Inserir no Início
# Dada uma lista de nomes, insira "Ana" no início da lista.

print("Exercício 6: Inserir no Início")
print("-" * 30)

# Solução:
nomes = ["João", "Maria", "Pedro"]
print("Lista original:", nomes)

nomes.insert(0, "Ana")  # Insere no início (índice 0)
print("Lista após inserir 'Ana' no início:", nomes)

print("\n" + "=" * 50 + "\n")

# Exercício 7: Fatiamento Avançado
# Dada a lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], extraia apenas os números pares usando fatiamento.

print("Exercício 7: Fatiamento Avançado")
print("-" * 30)

# Solução:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista original:", numeros)

# Usando fatiamento com passo 2 (começando do índice 1)
pares = numeros[1::2]  # Índices 1, 3, 5, 7, 9
print("Números pares usando fatiamento:", pares)

# Alternativa: usando range para criar lista de pares
pares_alt = list(range(2, 11, 2))
print("Números pares alternativo:", pares_alt)

print("\n" + "=" * 50 + "\n")

# Exercício 8: Lista Invertida
# Crie uma lista com 5 elementos e exiba ela invertida usando fatiamento.

print("Exercício 8: Lista Invertida")
print("-" * 30)

# Solução:
lista = ["A", "B", "C", "D", "E"]
print("Lista original:", lista)

invertida = lista[::-1]  # Fatiamento com passo -1
print("Lista invertida:", invertida)

print("\n" + "=" * 50 + "\n")

# Exercício 9: Manipulação Completa
# Crie uma lista vazia, adicione 3 elementos, insira um no meio, remova um e exiba o resultado.

print("Exercício 9: Manipulação Completa")
print("-" * 30)

# Solução:
lista = []
print("Lista vazia:", lista)

# Adicionando 3 elementos
lista.append("primeiro")
lista.append("segundo")
lista.append("terceiro")
print("Após adicionar 3 elementos:", lista)

# Inserindo no meio
lista.insert(1, "meio")
print("Após inserir 'meio' na posição 1:", lista)

# Removendo um elemento
lista.remove("segundo")
print("Após remover 'segundo':", lista)

print("\n" + "=" * 50 + "\n")

# Exercício 10: Análise de Lista
# Crie uma lista com números e mostre: o primeiro elemento, o último, o tamanho e uma fatia do meio.

print("Exercício 10: Análise de Lista")
print("-" * 30)

# Solução:
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Lista de números:", numeros)

print(f"Primeiro elemento: {numeros[0]}")
print(f"Último elemento: {numeros[-1]}")
print(f"Tamanho da lista: {len(numeros)}")
print(f"Fatia do meio (índices 3 a 7): {numeros[3:7]}")

print("\n" + "=" * 50 + "\n")

print("\n" + "=" * 50 + "\n")

# Exercício 11: Método pop()
# Crie uma lista com 5 elementos e use pop() para remover o último e o terceiro elemento.

print("Exercício 11: Método pop()")
print("-" * 30)

# Solução:
frutas = ["maçã", "banana", "laranja", "uva", "morango"]
print("Lista original:", frutas)

# Removendo o último elemento
ultima = frutas.pop()
print(f"Última fruta removida: {ultima}")
print("Após remover último:", frutas)

# Removendo o terceiro elemento (índice 2)
terceira = frutas.pop(2)
print(f"Terceira fruta removida: {terceira}")
print("Após remover terceira:", frutas)

print("\n" + "=" * 50 + "\n")

# Exercício 12: Métodos sort() e reverse()
# Crie uma lista com números desordenados, ordene-a e depois inverta.

print("Exercício 12: Métodos sort() e reverse()")
print("-" * 30)

# Solução:
numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", numeros)

# Ordenando
numeros.sort()
print("Após ordenar:", numeros)

# Invertendo
numeros.reverse()
print("Após inverter:", numeros)

print("\n" + "=" * 50 + "\n")

# Exercício 13: Métodos count() e index()
# Crie uma lista com elementos repetidos e encontre quantas vezes cada elemento aparece.

print("Exercício 13: Métodos count() e index()")
print("-" * 30)

# Solução:
letras = ["a", "b", "a", "c", "b", "a", "d"]
print("Lista de letras:", letras)

# Contando ocorrências
print(f"Quantidade de 'a': {letras.count('a')}")
print(f"Quantidade de 'b': {letras.count('b')}")
print(f"Quantidade de 'c': {letras.count('c')}")

# Encontrando índices
print(f"Primeira posição de 'a': {letras.index('a')}")
print(f"Primeira posição de 'b': {letras.index('b')}")

print("\n" + "=" * 50 + "\n")

# Exercício 14: Método extend()
# Crie duas listas e combine-as usando extend().

print("Exercício 14: Método extend()")
print("-" * 30)

# Solução:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print("Lista 1:", lista1)
print("Lista 2:", lista2)

# Estendendo lista1 com lista2
lista1.extend(lista2)
print("Após extend:", lista1)

# Estendendo com string
lista1.extend("abc")
print("Após extend com string:", lista1)

print("\n" + "=" * 50 + "\n")

# Exercício 15: Métodos clear() e copy()
# Crie uma lista, faça uma cópia, modifique a cópia e limpe a original.

print("Exercício 15: Métodos clear() e copy()")
print("-" * 30)

# Solução:
original = [10, 20, 30, 40]
print("Lista original:", original)

# Fazendo cópia
copia = original.copy()
print("Cópia:", copia)

# Modificando a cópia
copia.append(50)
copia.append(60)
print("Cópia modificada:", copia)
print("Original (não mudou):", original)

# Limpando a original
original.clear()
print("Original após clear:", original)
print("Cópia (não afetada):", copia)

print("\n" + "=" * 50 + "\n")

# Exercício 16: Funções len() e in
# Crie uma lista e use len() e in para analisá-la.

print("Exercício 16: Funções len() e in")
print("-" * 30)

# Solução:
cores = ["vermelho", "azul", "verde", "amarelo", "roxo"]
print("Lista de cores:", cores)

# Usando len()
print(f"Tamanho da lista: {len(cores)}")
print(f"Primeira cor: {cores[0]}")
print(f"Última cor: {cores[len(cores)-1]}")

# Usando in
print(f"'azul' está na lista: {'azul' in cores}")
print(f"'preto' está na lista: {'preto' in cores}")

# Aplicação prática
if "verde" in cores:
    print("Verde encontrado!")
    posicao = cores.index("verde")
    print(f"Posição do verde: {posicao}")

print("\n" + "=" * 50 + "\n")

# Exercício 17: Exercício Completo
# Crie uma lista com números, ordene, remova duplicatas, inverta e mostre estatísticas.

print("Exercício 17: Exercício Completo")
print("-" * 30)

# Solução:
numeros = [5, 2, 8, 2, 1, 5, 9, 3, 2, 7]
print("Lista original:", numeros)

# Ordenando
numeros.sort()
print("Após ordenar:", numeros)

# Removendo duplicatas (criando nova lista)
numeros_unicos = []
for num in numeros:
    if num not in numeros_unicos:
        numeros_unicos.append(num)

print("Sem duplicatas:", numeros_unicos)

# Invertendo
numeros_unicos.reverse()
print("Invertido:", numeros_unicos)

# Estatísticas
print(f"Tamanho final: {len(numeros_unicos)}")
print(f"Maior número: {max(numeros_unicos)}")
print(f"Menor número: {min(numeros_unicos)}")

print("\n" + "=" * 50 + "\n")

print("Fim dos exercícios! Continue praticando para dominar as listas em Python!")
