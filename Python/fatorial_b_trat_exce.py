def fatorial(n):
    # Caso base: fatorial de 0 é 1
    if n == 0:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    else:
        return n * fatorial(n-1)

try:       
    n = int(input('Digite um número inteiro positivo: '))
    if n < 0:
        raise ValueError("O número digitado deve ser um número inteiro positivo.")
    resultado = fatorial(n)
    print(f'O fatorial de {n} é {resultado}.')
except ValueError as e:
   print(f"Entrada inválida: {e}")

"""
Este código define a função fatorial, recebe uma entrada do usuário, e imprime o fatorial da entrada. Ele também lida com erros de entrada. Aqui estão os detalhes de cada linha:

1: A função fatorial é definida. Ela recebe um argumento: "n".

2-4: Se n é igual a 0 (o caso base para o fatorial), a função retorna 1.

5-7: Se n não é 0, a função retorna n multiplicado pelo fatorial de n-1. Isso é o caso recursivo, onde a função chama a si mesma com um valor ligeiramente menor. Essa chamada recursiva continuará até que o caso base seja atingido.

9: O código começa um bloco try. O código dentro deste bloco será executado, e se algum erro ocorrer, o programa irá para o bloco except correspondente, em vez de parar.

10: O programa pede ao usuário para inserir um número inteiro. Se o usuário inserir algo que não seja um número inteiro, int() lançará um ValueError, que será tratado no bloco except.

11-12: Se o número inserido for menor que 0, o programa lançará um ValueError com uma mensagem especificando que o número deve ser um número inteiro positivo.

13: O programa calcula o fatorial do número inserido e o armazena na variável resultado.

14: O programa imprime o fatorial do número inserido.

15-16: Este é o bloco except que trata a exceção ValueError. Se um ValueError for lançado em qualquer lugar no bloco try, este bloco será executado. Ele imprime "Entrada inválida:" e a mensagem associada à exceção, que será "O número digitado deve ser um número inteiro positivo" se um número negativo for inserido, ou um erro padrão de int() se a entrada não puder ser convertida em um inteiro.    
"""