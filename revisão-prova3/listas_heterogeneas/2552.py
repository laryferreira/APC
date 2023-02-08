''''Está chegando a grande final do Campeonato Nlogonense de Surf Aquático, que este ano ocorrerá na cidade de Bonita Horeleninha (BH)! Nesta cidade, o jogo PãodeQueijoSweeper é bastante popular!

O tabuleiro do jogo consiste em uma matriz de N linhas e M colunas. Cada célula da matriz contém um pão de queijo ou o número de pães de queijo que existem nas celulas adjacentes a ela.
Uma célula é adjacente a outra se estiver imediatamente à esquerda, à direita, acima ou abaixo da célula. Note que, se não contiver um pão de queijo, uma célula deve obrigatoriamente conter um número entre 0 e 4, inclusive.

Dadas as posições dos pães de queijo, determine o tabuleiro do jogo!

Entrada
A entrada contém vários casos de teste. 
A primeira linha de cada caso contém os inteiros N e M (1 ≤ N, M ≤ 100). 
As próximas N linhas contém M inteiros cada, separados por espaços, descrevendo os pães de queijo no tabuleiro. 
O j-ésimo inteiro da i-ésima linha é 1 se existe um pão de queijo na linha i e coluna j do tabuleiro, ou 0 caso contrário.

A entrada termina com fim-de-arquivo (EOF).

Saída
Para cada caso de teste, imprima N linhas com M inteiros cada, não separados por espaços, descrevendo a configuração do tabuleiro. 
Se uma posição contém um pão de queijo, imprima 9 para ela; caso contrário, imprima o número cuja posição deve conter.''''

while True:
  
  try:
    N,M = (int(x) for x in input().split()) #n linhas, m inteiros
    matriz = ([0]*(M+2)) #m+2 representará as bordas da matriz
    for i in range(1, N+1): #loop exceto na 1º e ultima linhas, que são bordas
      lista = [0] #lista com elemento 0, ignora as bordas
      aux = [int(x) for x in input().split()] #lista auxiliar
      for x in aux:
        lista.append(x)
      lista.append(0) #ultimo elemento 0
      matriz.append(lista) #adiciona linha a matriz
      
    matriz.append([0]*(M+2)) #última linha da matriz é zerada
    
    for i in range(1, N+1): 
      s = '' #abre uma string vazia
      for j in range(1, M+1): #+1 sempre ignora as bordas
        if matriz[i][j] == 1: # cada linha e coluna
          s+='9' 
        else:
          soma = matriz[i+1][j]+matriz[i-1][j]+matriz[i][j-1]+matriz[i][j+1] #soma dos quatro elementos adjacentes
          s+=str(soma)
       print(s) 
  except EOFError:
    break
