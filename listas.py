# Criando uma lista de números pares usando a compreensão da lista
numeros_pares = [x for x in range(10) if x % 2 == 0]
print(numeros_pares)
# Output: [0, 2, 4, 6, 8]

# Criando uma lista de cubos usando a compreensão da lista
cubos = [x**3 for x in range(5)]
print(cubos)
# Output: [0, 1, 8, 27, 64]

# Criando uma lista de palavras em uma frase usando a compreensão da lista
frase = "o céu está azul"
palavras = [word for word in frase.split()]
print(palavras)
# Output: ['o', 'céu', 'está', 'azul']

a = list('abc')
print(a)
# Output: ['a', 'b', 'c']

b = [1, 2, [3, 4]]
print(b)
# Output: [1, 2, [3,4]]

