h1, h2 = map(int, input().split())
if h1<h2:
    duracao = h2 - h1
else:
    duracao = h2 + 24 - h1
print(f'O JOGO DUROU {duracao} HORA(S)')
