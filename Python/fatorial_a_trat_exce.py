def fatorial(numero):
    total = 1
    for num in range(1, numero + 1):
        total *= num
    return total

try:
    numero = int(input('Digite um número inteiro para calcularmos o seu fatorial: '))
    if numero < 0:
        raise ValueError("O número digitado deve ser um número inteiro positivo.")
    resultado = fatorial(numero)
    print(f'O fatorial de {numero} é {resultado}.')
except ValueError as e:
   print(f"Entrada inválida: {e}")

'''
Este código é uma implementação da função fatorial em Python com manipulação de erros para números inválidos. Aqui estão os detalhes de cada linha:

1-5: A função fatorial é definida para calcular o fatorial de um número dado. Ele inicia com um total igual a 1, e então itera sobre a faixa de 1 a numero (inclusive), multiplicando total por cada número na faixa. Depois que todos os números foram multiplicados, ele retorna o total, que é o fatorial de numero.

7: Um bloco try é iniciado. Isso significa que o código dentro desse bloco será executado, e se qualquer erro ocorrer, em vez de o programa falhar, ele irá para o bloco except correspondente.

8: O código pede ao usuário para digitar um número. O input retorna uma string, então essa string é convertida em um número inteiro com int(). Esse valor é atribuído à variável numero.

9-10: O código verifica se o número é menor que 0. Se for, ele levanta uma exceção ValueError com uma mensagem informando que o número deve ser um número inteiro positivo. A função raise é usada para lançar uma exceção.

11: O código chama a função fatorial com "numero" como argumento, e atribui o resultado à variável resultado.

12: O código imprime o fatorial de numero.

13-14: Um bloco except que captura especificamente ValueError. Se um ValueError ocorrer no bloco try, este bloco será executado. Ele imprime "Entrada inválida:" seguido da mensagem de erro associada à exceção. O "as e" permite que você acesse a exceção que foi levantada e use suas propriedades, como a mensagem de erro.
'''   