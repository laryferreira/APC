'''Dêivis no show de rock
Dêivis e seus amigos estão se preparando para o próximo show de rock: Black Sabbath. A banda virá pela segunda e última vez ao Brasil, em dezembro de 2016. A situação é a seguinte: nem todos os amigos possuem dinheiro o suficiente para comprar o ingresso, mas alguns amigos possuem mais dinheiro do que o necessário. Como Dêivis e seus amigos são muito unidos e acreditam que a coisa mais importante da vida é não perder um show de rock com a galera, eles decidiram juntar todo o dinheiro que têm para tentarem comprar ingressos para todos. Dêivis se encarregou de fazer as contas. Mas o Dêivis é o Dêivis... É claro que sobrou para você.
Dada a quantidade de dinheiro de cada amigo e o valor 𝑖 do ingresso, Dêivis pediu a sua ajuda para calcular a parte inteira do dinheiro médio e determinar se todos poderão ir ao show.


A Entrada consiste de:
A primeira linha da entrada contém dois inteiros: quantidade de amigos 1≤𝑛≤109 e preço do ingresso 1≤𝑖≤109 separados por espaço.
Cada uma das próximas 𝑛 linhas contém um inteiro 0≤𝑎𝑖≤109 onde 1≤𝑖≤𝑛 representa o dinheiro do i-ésimo amigo.

A Saída deve apresentar:
A primeira linha da saída deve conter a parte inteira do dinheiro médio para cada amigo, conforme os exemplos.
A segunda linha deve conter a mensagem "o rock reinara mais uma vez" se houver dinheiro o suficiente para todos, ou a mensagem "rockeiros trabalhando ja" em caso contrário.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.

Descrição dos Exemplos:
No primeiro exemplo, existem 6 amigos e o preço do ingresso é de 300 dinheiros. A média de dinheiro que eles possuem é 313 dinheiros e este valor é suficiente para comprar 6 ingressos de 300 dinheiros cada.
No segundo exemplo, existem 3 amigos e o preço do ingresso é de 150 dinheiros. A média de dinheiro que eles possuem é 149 dinheiros e este valor não é suficiente para comprar 3 ingressos de 150 dinheiros cada.'''

n,ing = map(int, input().split())
dinheiro_total = 0
for i in range(n):
    dinheiro_total += int(input())
media_valor = int(dinheiro_total /n)
print (f'media: {media_valor}')
if media_valor >= ing:
    print('o rock reinara mais uma vez')
else:
    print('rockeiros trabalhando ja')
    
