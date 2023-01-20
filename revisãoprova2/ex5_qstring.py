def converter(word):
  num = '-1'
  if word == "zero":
    num = "0"
  if word == "um":
    num = "1"
  if word == "dois":
    num = "2"
  if word == "três":
    num = "3"
  if word == "quatro":
    num = "4"
  if word == "cinco":
    num = "5"
  if word == "seis":
    num = "6"
  if word == "sete":
    num = "7"
  if word == "oito":
    num = "8"
  if word == "nove":
    num = "9"
  return num

str = input()

num_extenso = ''
for word in str.split():
  for letter in word:
    num_extenso += letter
    if converter(num_extenso) != '-1':
      str = str.replace(num_extenso, converter(num_extenso))
      num_extenso = ''
  
  num_extenso = ''
print(str)
    #codigo feito com auxilio do colega Lurian
