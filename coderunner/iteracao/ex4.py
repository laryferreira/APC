menor_salario = float("inf")
dono_menor_salario = ""
while True:
    entrada = input()
    if "Fim" in entrada:
        if dono_menor_salario=="":
            print("Não tem")
        else:
            print(dono_menor_salario)
        break
    nome, salario = entrada.split(",")
    salario = float(salario)
    if salario < menor_salario:
        menor_salario = salario
        dono_menor_salario = nome
