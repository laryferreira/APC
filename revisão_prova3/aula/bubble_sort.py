#ordenação
lista = [5,2,1,7,3]
n = len(lista)
trocas = 0 #para contabilizar as trocas(inversões) 
for i in range(0,n-1):
    for j in range(i+1,n):
        if lista[j] < lista[i]: #só entra se i for menor do que j
            trocas += 1 #bubble sort -> lento
            aux = lista[i] #variavel auxiliar para que não ocorra o erro de trocar variáveis iguais
            lista[i] = lista[j]
            lista[j] = aux

print(trocas)
