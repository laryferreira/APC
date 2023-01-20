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
ncasos = 1 #iniciamos com caso 1 e não 0
while True:
    try: #try usado para depois utilizarmos except EOFError: break
        string_1 = input()
        string_2 = input()

        n1 = len(string_1) #retornando o numero de caracteres de uma string
        n2 = len(string_2)

        qnt_sub = 0 #quantidade de substrings
        pos = 0 #posição

        for i in range(0, n2): #range de 0 até o tamanho da string 
            tam = 0
            y = i #definindo variáveis pra incrementar posteriormente 
            x = 0 # y caractere na string 2, x caractere na string 1

            while x < n1 and y < n2 and string_1[x] == string_2[y]: #le-se enquanto x menor que numero de caracteres da string 1 e y menor que numero de caracteres da string 2 e o x caractere de string 1 = y caractere de string 2
                tam += 1 
                x += 1
                y += 1 #aqui está percorrendo as strings

            if tam == n1: #le-se se tamanho da string é igual a substring ("na mesma ordem e de forma contígua")
                qnt_sub += 1 #aumenta o numero de substrings
                pos = y - tam #posicao = caractere na string - tamanho da substring

        print(f'Caso #{ncasos}:') #formatação do output
        if qnt_sub > 0:
            print(f'Qtd.Subsequencias: {qnt_sub}')
            print(f'Pos: {pos+1}\n') #aqui eu realmente não sei pq adicionou 1, quem souber coloca um pull request aí!!
        else:
            print('Nao existe subsequencia\n') #\n serve pra pular a linha
#ps: Não se esqueça que o print tem que estar fora do for, senão ele imprimirá a cada caso e não no último caso apenas
        ncasos += 1 #numero de casos final

    except EOFError:
        break #finalizando o try 
