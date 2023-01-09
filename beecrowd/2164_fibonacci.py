n = int(input())

if n==1 or n==2:
    print(1.0)

else:
    fibpt1 = ((1 + 5**0.5)/2)**n
    fibpt2 = ((1 - 5**0.5)/2)**n
    fibtotal = (fibpt1 - fibpt2) / (5**0.5)
    print(f'{fibtotal:.1f}')
