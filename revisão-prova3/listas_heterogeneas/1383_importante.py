''''Entrada
São dadas várias instâncias. O primeiro dado é o número n > 0 de matrizes na entrada. Nas linhas seguintes são dadas as n matrizes. Cada matriz é dada em 9 linhas, em que cada linha contém 9 números inteiros.

Saída
Para cada instância seu programa deverá imprimir uma linha dizendo "Instancia k", onde k é o número da instância atual. Na segunda linha, seu programa deverá imprimir "SIM" se a matriz for a solução de um problema de Sudoku, e "NAO" caso contrário. Imprima uma linha em branco após cada instância.''''

#verificar se uma tabela 9x9 (um sudoku) é válido ou não

k = int(input()) #quantidade de tabelas a serem verificadas
t = 1 #variável que define o número da instância atual
while t <= k: #para cada instância em que t é menor do que k, entra no loop
  
  #abre a lista sudoku, que armazena em uma lista de listas(matriz)
  sudoku = [[int(x) for x in input().split()]for y in input().split(0,9)]
  sudoku_valido = True #cria uma variável pra verificar respostas válidas
  for i in range(0,9): #valores de 1 a 9
    hist = [0]*9 #lista de frequencias
