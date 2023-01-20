''''print(s[::2]) # Imprime os caracteres nos índices pares
print(s[1::2]) # Imprime os caracteres nos índices ímpares''''

frase = input()
frase_sblank = frase
frase_sblank = frase_sblank[1::2]

frase_sblank = frase_sblank.replace(" ", "")

print(frase_sblank)
