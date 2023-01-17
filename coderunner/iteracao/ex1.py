'''Onde está o fim?
Você recebeu uma lista com todos os colaboradores de uma empresa. A lista contém o nome do colaborador, um por linha. Você não sabe o tamanho da lista, mas sabe que ela acaba quando aparece no lugar do nome a palavra "Fim".

Elabore um programa que conte a quantidade de colaboradores da empresa.


A Entrada consiste de:
um número indefinido de linhas que termina com uma linha com a palavra "Fim";
cada linha contém a string do nome do colaborador.

A Saída deve apresentar:
Um número inteiro que é a quantidade de funcionários.'''

cont = 0
while True:
    id = str(input())
    if id == 'Fim':
        print(cont)
        break
    else:
        cont += 1
