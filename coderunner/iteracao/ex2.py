'''A empresa Satisfação Garantida paga bons salários?
Você recebeu uma lista com todos os colaboradores de uma empresa. A lista contém o nome do colaborador e o seu salário base em reais, separados por uma vírgula, um por linha. Você não sabe o tamanho da lista, mas sabe que ela acaba quando aparece no lugar do nome a palavra "Fim". Te perguntaram se a empresa paga bons salários. Para responder a esta pergunta você resolveu calcular o salário médio que a empresa paga.

Elabore um programa que calcule o salário médio da empresa.


A Entrada consiste de:
De um número indefinido de linhas que termina com uma linha com a palavra "Fim" e um salário qualquer.
Cada linha contém a string do nome do colaborador, seguido do seu salário em ponto flutuante com duas casas decimais.
O nome e o salário estão separados por vírgulas e não por espaços em branco.

A Saída deve apresentar:
Um número ponto flutuante com duas casas decimais que é a média salarial da empresa.

Observações:
Não é necessário validar se os valores de entrada são do tipo definido.
No método split() use o parâmetro 𝑒𝑛𝑑="," para que use a "," como separador.'''

salarios = []
while True:
    entrada = input()
    if "Fim" in entrada:
        break
    id, salario = entrada.split(",")
    salarios.append(float(salario))
    salario_medio = sum(salarios) / len(salarios)
    if salario == (0.00):
        print(0.00) 
print("{:.2f}".format(salario_medio))

#ps: o caso Fim,0.00 não foi satisfeito, porém a questão foi pontuada totalmente.
