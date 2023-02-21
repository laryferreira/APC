(https://www.beecrowd.com.br/judge/pt/problems/view/2633)
while True:

    try:
        n = int(input())

        dic_carnes = {}

        for _ in range(n):
            carne, validade = input().split()
            validade = int(validade)
            dic_carnes[validade] = carne #por qual chave seu dicionário estará organizado? = validade

        ans = '' #abre string vazia
        for val in sorted(dic_carnes):
            ans+=dic_carnes[val]+" "
        print(ans[:-1])

    except EOFError:
        break
