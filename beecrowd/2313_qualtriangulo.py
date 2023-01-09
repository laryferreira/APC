a,b,c = map(int, input().split())

def maior(a,b,c):
    if a>=b and a>=c:
        hip= a**2
        ls = b**2 + c**2
        if hip == ls:
            print('Retangulo: S')
        else:
            print('Retangulo: N')

    elif b>=a and b>=c:
        hip = b**2
        ls = a**2 + c**2
        if hip==ls:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
    elif c>=a and c>=b:
        hip = c**2
        ls = b**2 + a**2
        if hip==ls:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
        
    

if a + b <= c or a + c<= b or c + b <= a:
    print('Invalido')    

elif a==b and a==c and b==c:
    print('Valido-Equilatero')
    maior(a,b,c)
    
elif b==c or a==c or a==b:
    print('Valido-Isoceles')
    maior(a,b,c)

elif a!=b and a!=c and b!=c:
    print('Valido-Escaleno')
    maior(a,b,c)
