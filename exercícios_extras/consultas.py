q = int(input())
string = input()
string = string.lower() #minusculo, poderia ser string.upper() nesse caso também

while q > 0:
  substring = input()
  substring = substring.lower()
  if substring not in string:
    print('Nao Esta')
  else:
    print('Esta')
