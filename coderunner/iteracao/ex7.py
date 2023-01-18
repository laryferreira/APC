'''Dado um número 𝑁 inteiro e positivo, faça um programa que imprima todos os números de 0 a 𝑁, incluindo o 0 e o 𝑁 que são divisíveis por 3 e 7.


A Entrada consiste de:
De um único caractere 𝑁 inteiro positivo.

A Saída deve apresentar:
Todos os números de 0 a 𝑁, incluindo o 0 e o 𝑁 que são divisíveis por 3 e 7, em uma única linha. Os números devem estar separados por espaços em branco.'''

n = int(input())
for i in range(n+1):
    if i % 3 == 0 and i % 7 == 0:
        print(i, end=' ')
