cp1, np1, vp1 = map(float, input().split())
cp2, np2, vp2 = map(float, input().split())

valor = (np1 * vp1) + (np2 * vp2)
print(f'VALOR A PAGAR: R$ {valor:.2f}')
