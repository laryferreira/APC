a, b, c = map(float, input().split())
if abs(b-c) < a < (b+c) and (a-c) < b < (a + c) and (a - b) < c < (a + b):
    p = a + b + c 
    print(f'Perimetro = {p:.1f}')
else:
    ar = ((a+b)*c)/2
    print(f'Area = {ar:.1f}')
