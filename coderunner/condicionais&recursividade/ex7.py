n = int(input())
p = int(input())
#qual a regra da bomba? explodir! logo esse será o primeiro caso tratado
def bomba_explode(n):
    if n == 5:
        print(f'Seu tempo está acabando!')
        bomba_explode(n-1)
    elif n == 1:
        print(f'Seja rápido. Falta 1 segundo')
        bomba_explode(n-1)
    elif n<=0:
        print(f'Cabum!!!! Explodiu')
    else:
        print(f'Atenção faltam {n} segundos...')
        bomba_explode(n-1)
#agora partimos para as possibilidades
def bomba_desativada(n):
    if n == 5:
        print(f'Seu tempo está acabando!')
        bomba_desativada(n-1)
    elif n == 1:
        print(f'Bomba desativada automaticamente!')
    elif n<=0:
        print(f'Cabum!!!! Explodiu')   
    else:
        print(f'Atenção faltam {n} segundos...')
        bomba_desativada(n-1)

if p >= n:
    bomba_desativada(n)
else:
    bomba_explode(n)
