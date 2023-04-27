
def fatorial_recursivo(n):
    if n < 0:
        raise Exception('Erro: Não é possível fatorar números menores do que Zero.')
    if n > 1:
        return n * fatorial_recursivo(n - 1)
    else:
        n = 1
    return n


def fatorial_for(n):
    if n < 0:
        raise Exception('Erro: Não é possível fatorar números menores do que Zero.')
    if n > 1:
        for i in range(n - 1, 0, -1):
            n = n * i
    else:
        n = 1
    return n

n = int(input("Digite um número para calcularmos o fatorial dele: \n"))
print(f'O fatorial não recursivo de {n} é {fatorial_for(n)}')
print(f'O fatorial recursivo de {n} é {fatorial_recursivo(n)}')
