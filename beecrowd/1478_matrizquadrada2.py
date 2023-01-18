n = int(input())

for i in range(1, n + 1):  # linhas

    string = ''

    for j in range(1, n + 1):  # colunas

        if i > j:
            matriz_ij = i - j + 1
        else:
            matriz_ij = j - i + 1

            string += str(matriz_ij) + " "

        print(string[0:2 * n - 1])
