count = 0
soma = 0.0
for i in range(6):
    number = float(input())
    if number>0:
        soma = soma + number
        count += 1
        media = soma / count
print(f'{count} valores positivos')
print(f'{media:0.1f}')
