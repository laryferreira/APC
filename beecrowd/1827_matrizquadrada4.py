while True: #repetir 
    try: #requer umEOFError
        n = int(input()) #entrada
        condicao1 = n//3 #condiçao para o 1 definida no enunciado

        for i in range(0,n):
            linha = '' #para definir que i= linha e j= coluna
            for j in range(0,n): #a matriz inicia no 0 (no caso de 5, vai até 4)
                nmatriz = 0 #perceba que se não preencher nenhum dos requisitos abaixo será 0!
                if i == j: #linha e coluna iguais
                    nmatriz = 2
                if n-j-1 == i: #input - ncoluna - 1 deve ser igual ao numero da linha
                    nmatriz = 3
                if i>= condicao1 and i<=n-1-n//3 and j>= condicao1 and j<= n-1-condicao1: 
                    if i == n//2 and j == n//2: #perceba que o 4 deve ser prioridade
                        nmatriz = 4
                    else:
                        nmatriz = 1 #se não é 4 é 1

                linha+=str(nmatriz) #concatenação

            print(linha) #printar a matriz

        print() #print vazio requerido

    except EOFError:
        break
