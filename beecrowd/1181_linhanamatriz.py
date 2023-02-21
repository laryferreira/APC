(https://www.beecrowd.com.br/judge/pt/problems/view/1181)

l = int(input()) #linha da matriz
t = input() #soma ou media

n = 12
matriz = []
for i in range(0,n): #percorre as colunas
    lista = []
    for j in range(0,n): #percorre as colunas
        v = float(input()) #recebe cada valor
        lista.append(v) #adiciona v a lista de colunas
    matriz.append(lista) #matriz como lista de listas

soma = 0 #iniciou uma variável numérica
for j in range(0,n):
    soma+=matriz[l][j]

if t == "S":
    print(f'{soma:.1f}')
else:
    media = soma/n
    print(f'{media:.1f}')
