n, k = [int(i) for i in input().split()] #entrada e contagem
estudantes = [] #lista dos estudantes

while n:
    estudantes.append(input()) #passagem pela lista
    n -= 1

estudantes.sort() #ordena em ordem alfabética
print(estudantes[k-1]) #imprime 
