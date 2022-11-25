def fahrenheit(t):
    fahrenheit = t * 1.8 + 32
    fahrenheit_print = print(f'Fahrenheit: {fahrenheit}')
    return fahrenheit_print
def kelvin(t):
    kelvin = t + 273.15
    kelvin_print = print(f'Kelvin: {kelvin}')
    return kelvin_print
#************************************************
#Dada uma temperatura 𝑇, em graus Celsius, crie uma função 𝑓𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡() que calcule e apresente a temperatura correspondente em graus Fahrenheit e uma função 𝑘𝑒𝑙𝑣𝑖𝑛() que calcule e apresente a temperatura correspondente em Kelvin.
#A Entrada consiste de:
#Chamada das duas funções, 𝑓𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡(𝑇) e 𝑘𝑒𝑙𝑣𝑖𝑛(𝑇), com o parâmetro 𝑇, um número inteiro, que representa a temperatura em graus Celsius.
#A Saída deve apresentar:
#Duas linhas que dispõem a temperatura em Fahrenheit e em Kelvin.
#Observações:
#Atente para o tipo de variável utilizado. Cálculos devem ser feitos com variáveis int ou float, já a impressão por meio do print, deve ser feito com string.
#Para correção correta, devem ser definidas duas funções, uma para cada conversão.
#Descrição dos Exemplos:
#No primeiro exemplo, a temperatura é de 32°C, que representa 89,6°F ou 305,15 K. O cálculo foi feito utilizando a conversão padrão entre temperaturas:
#fahrenheit = 1,8 * celsius + 32
#kelvin = celsius + 273,15 
