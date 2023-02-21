(https://www.beecrowd.com.br/judge/pt/problems/view/2552)

while True:
    try:
        n, m = (int(x) for x in input().split()) #n linhas e m colunas

        matriz = [[0]*(m+2)] #inicializa com coluna zerada + bordas

        for i in range(1, n+1): #as bordas não fazem parte do for
            lista = [0] #lista com elemento 0 (borda 1)
            aux = [int(x) for x in input().split()] #cria lista auxiliar
            for x in aux:
                lista.append(x)
            lista.append(0) #acrescenta borda 2
            matriz.append(lista) #adiciona a matriz

        matriz.append([0]*(m+2))

        for i in range(1,n+1):
            s = ''
            for j in range(1, m+1): #colunas exceto primeira e última
                if matriz[i][j] == 1:
                    s+='9'
                else:
                    soma = matriz[i+1][j]+matriz[i-1][j]+matriz[i][j-1]+matriz[i][j+1] #acima, abaixo, esq, direita
                    s+= str(soma)
            print(s)
    except EOFError:
