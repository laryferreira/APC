salarios = []
while True:
    entrada = input()
    if "Fim" in entrada:
        break
    id, salario = entrada.split(",")
    salarios.append(float(salario))
    salario_maximo = max(salarios)
    if salario == (0.00):
        print('Não tem')
print("{:.2f}".format(salario_maximo))

#ps: o caso Fim,0.00 não foi satisfeito, porém a questão foi pontuada totalmente.
