#programa para transformar dias de vida em anos, meses e dias. 

#usuário insere
dias_total = int(input("Dias de vida: "))

#anos
anos_in = dias_total//365
resto = dias_total%365

#meses
meses_in = resto//30

#dias
dias_in = resto%30

#print para o usário
anos_out = print(anos_in, "ano(s)")
meses_out = print(meses_in, "mes(es)")
dias_out = print(dias_in, "dia(s) de vida! Parabéns!")
