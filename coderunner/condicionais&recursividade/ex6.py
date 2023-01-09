def imprimeTermos(n):
    if n <= 0:
        print (0)
        
    else:
        print(n)
        return imprimeTermos(n - 2)
    
    
