(https://www.beecrowd.com.br/judge/pt/problems/view/1261)

while True:
    try:
        hay_points = {} #dicionario

        m, n = (int(x) for x in input().split()) #recebe os dois valores

        for _ in range(m):
            wrd, sal = input().split()
            sal = int(sal)
            hay_points[wrd] = sal #organizado pelas palavras, não pelos números

        for _ in range(n):
            text = input()
            ans = 0
            while text != '.':
                for word in text.split():
                    if word in hay_points: #se a palavra estiver no dicionario
                        ans+=hay_points[word]
                text = input()

            print(ans)
    except EOFError:
        break
