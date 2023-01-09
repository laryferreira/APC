#duas entradas no mesmo input, map
c,q = map(int, input().split())
#agora devemos definir os precos referentes aos codigos
if c == 1:
    preco = (4.00 * q)

elif c == 2:
    preco = (4.50 * q)

elif c == 3:
    preco = (5.00 * q)

elif c == 4:
    preco = (2.00 * q)

elif c == 5:
    preco = (1.50 * q)

print(f'Total: R$ {preco:.2f}')
