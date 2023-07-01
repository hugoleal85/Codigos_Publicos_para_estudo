def fatorial(numero):
    total = 1
    for num in range(1, numero + 1):
        total *= num
    return total

numero = int(input('Digite um número inteiro para calcularmos o seu fatorial: '))
resultado = fatorial(numero)
print(f'O fatorial de {numero} é {resultado}.')
    