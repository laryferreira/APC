(https://www.beecrowd.com.br/judge/pt/problems/view/2370)

n, t = map(int, input().split())
estudantes = []
for i in range(n):
    nome, skill = input().split()
    skill = int(skill)
    estudantes.append((nome, skill))

estudantes.sort(key=lambda x: x[1], reverse=True)

times = [[] for i in range(t)]
for i, (nome, skill) in enumerate(estudantes):
    times[i % t].append(nome)

for i, time in enumerate(times):
    time.sort()
    print(f'Time {i + 1}')
    for nome in time:
        print(nome)
    print()
