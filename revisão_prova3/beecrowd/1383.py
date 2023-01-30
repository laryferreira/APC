n = int(input())
inst = 1
while n > 0:
    print(f'Instancia {inst}')
    matriz = []
    for i in range(0,9):
        matriz.append([int(x) for x in input().split()])
    
    solucao_valida = True
    
    for i in range(0,9,3): #i = 0,3,6
        for j in range(0,9,3): #j = 0,3,6
        
            histograma = [0] * 9
            
            for x in range(i,i+3):
                for y in range(j,j+3):
                    num = matriz[x][y]
                    if histograma[num-1] == 1:
                        solucao_valida = False
                    else:
                        histograma[num-1]+=1
                    
    for i in range(0,9):
        histograma = [0]*9
        for j in range(0,9):
            num = matriz[i][j]     
            if histograma[num-1] == 1:
                solucao_valida = False
                
            else:
                histograma[num-1]+=1
    
    for j in range(0,9):
        histograma = [0]*9
        for i in range(0,9):
            num = matriz[i][j]
            if histograma[num-1] == 1:
                solucao_valida = False 
            else:
                histograma[num-1]+=1
                
               
    if solucao_valida == False:
        print('NAO\n')
    else:
        print('SIM\n')
        
    inst += 1
    n -=1  
