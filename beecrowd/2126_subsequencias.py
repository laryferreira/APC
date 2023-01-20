ncasos = 1
while True:
    try:
        string_1 = input()
        string_2 = input()

        n1 = len(string_1)
        n2 = len(string_2)

        qnt_sub = 0
        pos = 0

        for i in range(0, n2):
            y = i
            tam = 0
            x = 0

            while x < n1 and y < n2 and string_1[x] == string_2[y]:
                tam += 1
                x += 1
                y += 1

            if tam == n1:
                qnt_sub += 1
                pos = y - tam

        print(f'Caso #{ncasos}:')
        if qnt_sub > 0:
            print(f'Qtd.Subsequencias: {qnt_sub}')
            print(f'Pos: {pos+1}\n')
        else:
            print('Nao existe subsequencia\n')

        ncasos += 1

    except EOFError:
        break
