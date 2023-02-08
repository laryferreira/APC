''''Considerando a entrada de valores inteiros não negativos, ordene estes valores segundo o seguinte critério:

Primeiro os Pares
Depois os Ímpares
Sendo que deverão ser apresentados os pares em ordem crescente e depois os ímpares em ordem decrescente.

Entrada
A primeira linha de entrada contém um único inteiro positivo N (1 < N <= 105) Este é o número de linhas de entrada que vem logo a seguir. As próximas N linhas conterão, cada uma delas, um valor inteiro não negativo.

Saída
Apresente todos os valores lidos na entrada segundo a ordem apresentada acima. Cada número deve ser impresso em uma linha, conforme exemplo abaixo.'''''

#explicação:

N = int(input()) #número de linhas que virá a seguir

par = [] #lista vazia para par
impar = [] #lista vazia para ímpar

for i in range(0,N): 
  n = int(input()) #número 
  
  if n % 2 == 0: #condição para ser par
    par.append(n)
  else:
    impar.append(n)

par.sort() #ordenado em ordem crescente
impar.sort(reverse=True) #em ordem decrescente

#se imprimirmos agora, o resultado retornado será uma lista. logo, precisamos acessar cada elemento na lista e imprimí-lo
for elem in par:
  print(elem)
for elem in impar:
  print(elem)
