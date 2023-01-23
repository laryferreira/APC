n = int(input())
chamada = []

for i in range(n):
    chamada.append(input()+"\n")
    chamada.sort(reverse = True)
print("".join(chamada))
