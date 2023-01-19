#Código do professor Vinícius:
''''while True:
	
	try:
	
		n = int(input())
		
		part1 = n//3
		
		for i in range(0,n):
		
			linha = ''
			for j in range(0,n):
				
				aij = 0
				
				if i == j:
					aij = 2
				
				if n-j-1 == i:
					aij = 3
				
				if i >= part1 and i <= n-1-part1 and j >= part1 and j <= n-1-part1:
					if i == n//2 and j == n//2:
						aij = 4
					else:
						aij = 1
				
				linha+=str(aij)
		
			print(linha)
		
		print()
	
	except EOFError:
		break''''
#Meu código original:
''''while True:
    try:
        n = int(input())
        if n == 0:
            break
        for i in range(0,n):
            for j in range(n):
                if i==j and i==n/2:
                    print(4, end='')
                elif i == n/3:
                    print(1,end='')
                elif i==j:
                    print(2,end='')
                elif i + j == n - 1:
                    print(3,end='')
                elif n - 1 - n/3:
                    print(0,end='')  
            print('')
    except EOFError:
        break''''

''''Neste programa seu trabalho é ler um valor inteiro que será o tamanho da matriz quadrada (largura e altura) que será preenchida da seguinte forma: a parte externa é preenchida com 0, a parte interna é preenchida com 1, a diagonal principal é preenchida com 2, a diagonal secundária é preenchida com 3 e o ponto central contém o valor 4, conforme os exemplos abaixo.

Obs: o quadrado com '1' sempre começa na posição tamanho/3, tanto na largura quanto quanto na altura. A linha e a coluna começam em zero (0).

Entrada
A entrada contém vários casos de teste e termina com EOF (fim de arquivo. Cada caso de teste consiste de um valor inteiro ímpar N (5 ≤ N ≤ 101) que é o tamanho da matriz.'''''

while True:
	try:
