salarios = []
while True:
    entrada = input()
    if "Fim" in entrada:
        break
    id, salario = entrada.split(",")
    salarios.append(float(salario))
    salario_medio = sum(salarios) / len(salarios)
    if salario == (0.00):
        print(0.00) 
print("{:.2f}".format(salario_medio))

#ps: o caso Fim,0.00 não foi satisfeito, porém a questão foi pontuada totalmente.
