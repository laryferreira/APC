def areas(a,b,c):
    retangulo = (a * b)
    triangulo = int((b * c) / 2)
    trapezio = int((a *(c+b))/ 2)
    print(retangulo)
    print(triangulo)
    print(trapezio)

# ***************************************    
#Crie uma função chamada 𝑎𝑟𝑒𝑎𝑠() que recebe 3 números inteiros (𝐴, 𝐵 e 𝐶) e calcula, em ordem:

#A área de um retângulo com lados 𝐴 e 𝐵;
#A área de um triângulo com base 𝐵 e altura 𝐶;
#A área de um trapézio de altura 𝐴, base menor 𝐵 e base maior 𝐶.
#Apresente os valores ignorando a parte decimal.

#A Entrada consiste de:
#A entrada compreende os parâmetros da função 𝑎𝑟𝑒𝑎𝑠(𝐴,𝐵,𝐶), que são três números inteiros, sendo 𝐶 maior que 𝐵.
#A Saída deve apresentar:
#Três linhas apresentando os valores solicitados. Para ignorar a parte decimal, pode-se utilizar a função int().
#Dica:
#Para ignorar a parte decimal, pode-se utilizar a função int() para mudar o tipo de ponto flutuante para inteiro.
