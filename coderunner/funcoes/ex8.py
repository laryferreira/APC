def cents(x, valor): 
        moedas = x//valor
        troco = x%valor
        return moedas, troco
def troco(x):
    qt50, troco = cents(x,50) 
    print(f'{qt50} moedas de 50 centavos')
    qt25, troco = cents(troco,25) 
    print(f'{qt25} moedas de 25 centavos')
    qt10, troco = cents(troco,10) 
    print(f'{qt10} moedas de 10 centavos')
    qt5, troco = cents(troco,5) 
    print(f'{qt5} moedas de cinco centavos')
    qt1, troco = cents(troco,1) 
    print(f'{qt1} moedas de 1 centavo')
