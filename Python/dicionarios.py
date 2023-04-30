'''
Em Python, um dicionário é um tipo de coleção que permite armazenar pares de chave-valor, onde cada chave é
 única e associada a um valor correspondente. Os dicionários são implementados como tabelas de
 dispersão (hash tables) e são muito eficientes para recuperar valores a partir de suas chaves.
 Em outras palavras, os dicionários permitem que você associe uma chave a um valor e, em seguida,
 recupere esse valor rapidamente, mesmo para dicionários muito grandes.

Para criar um dicionário em Python, você pode usar chaves {} ou a função dict(). Aqui está um exemplo:
'''

# Criando um dicionário com chaves e valores
dicionario = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}

# Acessando o valor de uma chave
print(dicionario['nome'])
# Output: João

# Modificando o valor de uma chave
dicionario['idade'] = 30

# Adicionando um novo par chave-valor
dicionario['profissão'] = 'engenheiro'

# Removendo um par chave-valor
del dicionario['cidade']

# Imprimindo o dicionário completo
print(dicionario)
# Output: {'nome': 'João', 'idade': 30, 'profissão': 'engenheiro'}
