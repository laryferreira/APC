''''Dr. Shoo Makra desenvolveu um jeito de checar se o sistema do painel de posições está funcionando corretamente. Dada a informação exibida no painel de posições, ele quer reconstruir o grid de largada da corrida. Se for possível reconstruir um grid de largada válido, ele planeja checar ele contra o grid de largada real. No entanto, se não for possível reconstruir um grid de largada valido, o sistema do painel de posições está mesmo defeituoso.

Você pode ajudar o Dr. Shoo Makra?

Entrada
O arquivo de entrada contém vários casos de teste. A primeira linha do teste contém um valor inteiro N indicando o número de carros na corrida (2 ≤ N ≤ 10³). As próximas N linhas contém dois inteiros C e P, separados por um espaço, representando o número do carro (1 ≤ C ≤ 104) e o número de posições que o carro ganhou ou perdeu relativo ao grid de largada (-106 ≤ P ≤ 106), de acordo com o painel de posições. Todos os carros na corrida tem números diferentes.

O último caso de teste é seguido por uma linha que contém apenas um número zero.

Saída
Para cada caso de teste da entrada seu programa deve imprimir apenas uma linha, contendo o grid de largada reconstruído, com o número dos carros separados por um espaço. Se não foi possível reconstruir um grid de largada válido, a linha deve conter -1.''''

#explicação:

N = int(input()) #número de carros na corrida

while N: #condição de loop para rodar enquanto a quantidade de carros estiver válida
  carro = [] #lista vazia para número do carro
  ganhou_pos = [] #lista vazia para quantas posições ganhadas(se ganhou)
  
  start = [0] * n #lista zerada para que todo mundo saia na largada junto
  flag = True 
  
  '''A variável "flag" está sendo usada como um indicador para determinar se uma solução válida foi encontrada para o problema. 
  Se a flag for definida como falsa (flag = False), significa que não há uma solução válida e o valor de saída será "-1". 
  Se a flag for verdadeira (flag = True), significa que uma solução válida foi encontrada e o valor de saída será uma string com os valores da lista "start".''''
  
  for i in range(0,N):
    c, p = (int(x) for x in input().split()) #tomando os valores da entrada (para carro e posição) separados e como inteiros
    
    carro.append(c)
    ganhou_pos.append(p) #cada lista recebe seus respectivos valores a cada loop for in
    
  for i in range(0,N): 
    if start[i] == 0: 
         flag = False #se alguma posição inicial não foi preenchida com um valor, a solução deve ser falsa
        
    if flag == False: #perceba a diferença entre = e ==
      ans = '-1' #não foi possivel construir um grid de largada válido
      else:
        ans = '' #cria string vazia
        for i in range(0,N-1):  
          ans+=str(start[i])+" " 
        ans+=str(start[N-1]) #último caso separado, sem o espaço adicional
    
    print(ans)
    N = int(input()) #se não colocar pra receber novamente os valores dá runtime error no beecrowd
   
      
    
 
