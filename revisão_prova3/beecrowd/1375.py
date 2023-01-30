'''Entrada
O arquivo de entrada contém vários casos de teste. A primeira linha do teste contém um valor inteiro N indicando o número de carros na corrida (2 ≤ N ≤ 10³). As próximas N linhas contém dois inteiros C e P, separados por um espaço, representando o número do carro (1 ≤ C ≤ 104) e o número de posições que o carro ganhou ou perdeu relativo ao grid de largada (-106 ≤ P ≤ 106), de acordo com o painel de posições. Todos os carros na corrida tem números diferentes.

O último caso de teste é seguido por uma linha que contém apenas um número zero.

Saída
Para cada caso de teste da entrada seu programa deve imprimir apenas uma linha, contendo o grid de largada reconstruído, com o número dos carros separados por um espaço. Se não foi possível reconstruir um grid de largada válido, a linha deve conter -1.''''
'''
exemplos:
4
1 0
3 1
2 -1
4 0

4
22 1
9 1
13 0
21 -2

'''
n = int(input()) #número de entradas

while n: #enquanto rodar nesses números de entradas
  
  carro = [] #lista vazia para os carros
  pos_ganhada = [] #lista vazia para as posições ganhadas
  start = [0] * n #lista zerada do início das posições
  verifica = True #dúvida: a bandeira é uma verificação?
  
  for i in range(0,n): #para i de 0 a n posições
    c, p = (int(x) for x in input().split()) #recebendo a entrada e dividindo em número do carro e posição 
    
    carro.append(c)
    pos_ganhada.append(p) #somando as entradas às listas vazias
  
  for i in range(0,n):
    if pos_ganhada[i] == 0:
      start[i] == carro[i] #não sai da posição
  elif i+pos_ganhada[i] >= 0 and i+pos_ganhada[i] < n:
    start[i+gained[i]] = car[i] #ganha ou perde posição
  
  for i in range(0,n):
    if start[i] == 0:
      verifica = False #não pode acontecer esse caso
      
  if verifica == False:
    ans = '-1'
  else:
    ans = ''
    for i in range(0,n-1):
      ans+=str(start[i])+'' #espaço vazio 
    ans+=str(start[n-1])
      
print(ans)
    
    

