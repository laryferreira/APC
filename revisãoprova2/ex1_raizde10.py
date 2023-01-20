def raizquadrada(a): #faremos essa questão por recursividade
    if a == 0: 
        return 0 
    else:
        frac = 1/(6 + raizquadrada(a-1)) #função da operacao
        return frac
    
n = int(input()) #numero de entrada
if n == 0:
    ans = 3 + 0
    print("{:.10f}".format(ans)) #caso definido no problema (veja outputs)
else:
    ans = 3 + raizquadrada(n)
    print("{:.10f}".format(ans)) #retornando a função
