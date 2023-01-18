n = int(input())
for i in range(n):
    string = input()
    string = list(string)

    for j in range(0, len(string)):
        if (string[j].isalpha()):
            string[j] = chr(ord(string[j] + 3))  #desloca 3 casas para direita

        str_nova = string[::-1]

        tam = len(str_nova)//2

        for k in range(tan,len(str_nova)):
            if str_nova[k] == '':
                continue
            str_nova[k] = chr(ord(str_nova[k] - 1))

        print(''.join(str_nova))
