c = int(input())

while c>0:
  string = input()
  
  tam = len(string)
  substring = ''
  
for charactere in string[::-1]: #colocar ao contrário
  if ord(caractere) >= 97 and ord(caractere) <= 122: #minusculas
    substring += caractere
    
print(substring)

c -=1
