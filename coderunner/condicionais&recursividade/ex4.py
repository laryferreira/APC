n1, n2, n3 = map(float,input().split())
tipo = str(input())

if tipo == "A":
    mediaA = (n1 + n2 + n3) / 3
    print("Aritmetica")
    print (f'{mediaA:.2f}')

elif tipo == "H":
    mediaH = 3 / (1/n1 + 1/n2 + 1/n3)
    print("Harmonica")
    print (f'{mediaH:.2f}')

elif tipo == "P":
    p1, p2, p3 = map(float,input().split())
    mediaP = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)
    print("Ponderada")
    print (f'{mediaP:.2f}')
    
else:
    print("Operacao inexistente")
