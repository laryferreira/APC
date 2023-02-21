(https://www.beecrowd.com.br/judge/pt/problems/view/1375)

n = int(input())
while n:
    carro = [] #lista vazia recebe carros
    pos_ganha = [] #lista vazia recebe posicoes
    grid = [0]*n #zera lista de frequencia de posicoes, grid inicial
    valido = True #cria variável para checar se é válida

    for i in range(0,n):
        c, p = (int(x) for x in input().split()) #recebe c -> numero do carro e p-> numero de posicoes
        carro.append(c) #adiciona a lista
        pos_ganha.append(p) #adiciona a lista

    for i in range(0,n):
        if pos_ganha[i] == 0: #caso do 0, não ganha posição
            grid[i] = carro[i] #posição do grid inicial = carro, não muda
        elif i+pos_ganha[i] >= 0 and i+pos_ganha[i] < n: #verificando se valor +pos ganha > 0 e < n
            grid[i+pos_ganha[i]] = carro[i] #coloca no grid a posição ganha = indice do carro

    for i in range(0,n):
        if grid[i] == 0: # se a posição inicial é zero, após realocação, inválido. tem que ser 1, 2, 3...
           valido = False

    if valido == False:
        ans = '-1'
    else:
        ans = ''
        for i in range(0,n-1):
            ans+=str(grid[i])+" "
        ans += str(grid[n - 1]) #ultimo caso separado, sem espaço

    print(ans)
    n = int(input())
