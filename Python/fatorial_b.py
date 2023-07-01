def fatorial(n):
    # Caso base: fatorial de 0 é 1
    if n == 0:
        return 1
    else: 
        # Caso recursivo: n! = n * (n-1)!
        return n * fatorial(n-1)

n = int(input('Digite um número inteiro positivo: '))
resultado = fatorial(n)
print(f'O fatorial de {n} é {resultado}.')
