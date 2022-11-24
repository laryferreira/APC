def money(x, value):
    notes = x//value
    exch = x%value
    return notes, exch

def cents(y, value):
    coins = y//value
    exch = y%value
    return coins, exch

def exch(x):
    v100, exch = money(x,100)
    

    v50, exch = money(x,50)
  

    v20, exch = money(x,20)
   

    v10, exch = money(x,10)
    

    v5, exch = money(x,5)
    

    v2, exch = money(x,2)
    
    
def exch(y):
    v1, exch = money(x,1)
    print(f'{v100} moedas de R$ 1.00')

    v50c, exch = money(x,50)
    print(f'{v50} moedas de R$ 0.50')

    v20c, exch = money(x,20)
    print(f'{v20} moedas de R$ 0.20')

    v10c, exch = money(x,10)
    print(f'{v10} moedas de R$ 0.10')

    v5c, exch = money(x,5)
    print(f'{v5} moedas de R$ 0.05')

    v1c, exch = money(x,1)
    print(f'{v2} moedas de R$ 0.01')

entrada = float(input())
print(f'{v100} notas de R$ 100')
print(f'{v50} notas de R$ 50')
print(f'{v20} notas de R$ 20')
print(f'{v10} notas de R$ 10')
print(f'{v5} notas de R$ 5')
print(f'{v2} notas de R$ 2')
