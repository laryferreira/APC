(https://www.beecrowd.com.br/judge/pt/problems/view/2381)
n, k = [int(i) for i in input().split()]
estudantes = []

while n:
    estudantes.append(input())
    n -= 1

estudantes.sort()
print(estudantes[k-1])
