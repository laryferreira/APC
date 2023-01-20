caracter = input()
inverte = caracter[::-1]

frase = input()

while frase != '':
    frase = frase.replace(caracter,'')
    frase = frase.replace(inverte,'')
    print(frase)
    frase = input()
