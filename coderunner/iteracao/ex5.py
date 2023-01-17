n = int(input())
if n == 0:
    print('Não tem média')
    print('Não tem')
    print('Não tem')
else:
    salario_total = 0
    maior_salario = float('-inf')
    colab_maior_salario = ''
    menor_salario = float('inf')
    colab_menor_salario =''
    for i in range(n):
        nome, salario = input().split(',')
        salario = float(salario)
        salario_total += salario
        if salario > maior_salario:
            maior_salario = salario
            colab_maior_salario = nome
        if salario < menor_salario:
            menor_salario = salario
            colab_menor_salario = nome
    salario_medio = salario_total / n
print("{:.2f}".format(salario_medio))
print("{} {:.2f}".format(colab_maior_salario, maior_salario))
print("{} {:.2f}".format(colab_menor_salario, menor_salario))
