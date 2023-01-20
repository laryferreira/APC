string = input()
cont = 0
for i in string:
    if i.isnumeric() == True:
        cont += 1
print(cont)    
