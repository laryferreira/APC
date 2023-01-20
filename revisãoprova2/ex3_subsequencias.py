''''Dados dois números naturais N1 e N2, diz-se que N1 é subsequência contígua de N2 se todos os dígitos de N1 aparecem, na mesma ordem e de forma contígua, em N2. Crie uma aplicação que leia dois números naturais e diga se o primeiro é uma subsequência contígua do segundo.

Entrada
A entrada é composta por vários casos de teste e termina com final de arquivo (EOF). A primeira linha de cada entrada é composta por um valor natural N1(1 < N1 < 1010), a segunda linha é composta por um valor N2( N1 < N2 < 1032).
Saída
Para cada caso de teste imprima a quantidade de subsequências contíguas e a posição onde a subsequência é iniciada, caso exista mais de uma subsequência, imprima onde é iniciada a última subsequência. Caso não exista subsequência, imprima "Nao existe subsequencia". Mostre o resultado conforme o exemplo de saída.
Caso #1:
Qtd.Subsequencias: 6
Pos: 27
ou
Caso #2:
Nao existe subsequencia
'''''
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
