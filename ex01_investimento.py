#para criar uma reserva segura, 30% do salário deve ser investido
#devemos criar uma variável para os 30% investido a partir do salário (valor_original)
valor_original = float( input("Meu salário: R$" ))
novo_valor = valor_original * 0.30 
#o programa deve retornar o montante anual do valor investido
#devemos criar outra variável
anual_valor = novo_valor * 12
#o programa deve retornar o montante em 10 anos do valor investido
decada_valor = novo_valor * 120
#o programa deve perguntar ao usuário as informações necessárias para calcular a reserva:
print ('Devo investir: R$ ', novo_valor)
print ('No final do primeiro ano, terei o montante de R$', anual_valor)
print ('Em 10 anos, terei o montante de R$', decada_valor)
