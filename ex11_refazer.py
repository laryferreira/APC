salario = float(input())
if salario>0 and  salario<=400:
    novo = salario * 1.15
    reajuste = novo - salario
print(f'Novo salário:{novo:.2f}')
print(f'Reajuste ganho: {reajuste}')
print("Em percentual: 15 %")
if salario>400 and  salario<800:
    novo = salario * 1.12
    reajuste = novo - salario
print(f'Novo salário:{novo:.2f}')
print(f'Reajuste ganho: {reajuste}')
print("Em percentual: 12 %")
if salario>800 and  salario<1200:
    novo = salario * 1.0
    reajuste = novo - salario
print(f'Novo salário:{novo:.2f}')
print(f'Reajuste ganho: {reajuste}')
print("Em percentual: 10 %")
if salario>1200 and  salario<2000:
    novo = salario * 1.07
    reajuste = novo - salario
print(f'Novo salário:{novo:.2f}')
print(f'Reajuste ganho: {reajuste}')
print("Em percentual: 7 %")
if salario>2000:
    novo = salario * 1.04
    reajuste = novo - salario
print(f'Novo salário:{novo:.2f}')
print(f'Reajuste ganho: {reajuste}')
print("Em percentual: 4 %")

def novo_salario(salario, p):
  novo = salario * p
  reajuste = novo - salario
    print(f'Novo salário:{novo:.2f}')
    print(f'Reajuste ganho: {reajuste}')
    print("Em percentual: {p} %")
    #BEECROWD
