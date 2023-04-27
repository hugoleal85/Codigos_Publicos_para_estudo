a = 1
b = 2

# troca de variáveis usando variável auxiliar ‘temp’
print(f"O valor inicial da variável a é: {a}")
print(f"O valor inicial da variável b é: {b}")
temp = a
a = b
b = temp
print(f"O novo valor da variável a é: {a}")
print(f"O novo valor da variável b é: {b}")

# troca de variáveis através de atribuição múltipla (desfazendo a troca anterior)
a, b = b, a
print(f"O valor final da variável a é: {a}")
print(f"O valor final da variável b é: {b}")

'''Este código em Python demonstra duas maneiras diferentes de trocar os valores das variáveis a e b.

A primeira maneira, usando uma variável auxiliar temp, consiste em armazenar o valor de a em temp, atribuir o valor de b a a e, em seguida, atribuir o valor de temp a b. Isso efetivamente troca os valores das variáveis a e b.

A segunda maneira de trocar os valores das variáveis é através de atribuição múltipla. Nesse caso, os valores das variáveis a e b são trocados em uma única linha, sem a necessidade de uma variável auxiliar.

A primeira maneira é mais útil em situações em que você não pode usar atribuição múltipla, como em linguagens de programação que não a suportam. A segunda maneira é mais conveniente e pode tornar o código mais legível em Python.'''