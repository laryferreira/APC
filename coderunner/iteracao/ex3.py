'''Qual o maior salário?
Você recebeu uma lista com todos os colaboradores de uma empresa. A lista contém o nome do colaborador e o seu salário base em reais, separados por uma vírgula, um por linha. Você não sabe o tamanho da lista, mas sabe que ela acaba quando aparece no lugar do nome a palavra "Fim". Te perguntaram qual maior salário na empresa. 

Elabore um programa que ache e imprima o maior salário da empresa. Não precisa usar listas ou dicionários para fazer esta questão.


A Entrada consiste de:
De um número indefinido de linhas que termina com uma linha com a palavra "Fim" e um salário qualquer.
Cada linha contém a string do nome do colaborador, seguido do seu salário, que é maior que zero, em ponto flutuante com duas casas decimais.
O nome e o salário estão separados por vírgulas e não por espaços em branco.

A Saída deve apresentar:
O valor do maior salário ou a string "Não tem", caso não haja o maior salário.

Observações:
Não é necessário validar se os valores de entrada são do tipo definido.
No método split() use o parâmetro 𝑠𝑒𝑝="," para que use a "," como separador.'''

salarios = []
while True:
    entrada = input()
    if "Fim" in entrada:
        break
    id, salario = entrada.split(",")
    salarios.append(float(salario))
    salario_maximo = max(salarios)
    if salario == (0.00):
        print('Não tem')
print("{:.2f}".format(salario_maximo))

#ps: o caso Fim,0.00 não foi satisfeito, porém a questão foi pontuada totalmente.
