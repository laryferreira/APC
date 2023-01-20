def raizquadrada(a): #definiu função
    if a == 0:
        return 0 
    else:
        frac = 1/(6 + raizquadrada(a-1))
        return frac
    
n = int(input())
if n == 0:
    ans = 3 + 0
    print("{:.10f}".format(ans))
else:
    ans = 3 + raizquadrada(n)
    print("{:.10f}".format(ans))
