(https://www.beecrowd.com.br/judge/pt/problems/view/1318)

n, m = (int(x) for x in input().split()) #entrada, n bilhetes, m pessoas
while n > 0 and m > 0:
    tickets = {}
    for i in range(1, n+1):
        tickets[i] = 0 #valor 0 do dicionario, como se fosse um histograma

    pessoas = [int(x) for x in input().split()] #recebeu as entradas como lista

    for i in range(0,m):
        ticket_entregue = pessoas[i]
        tickets[ticket_entregue]+=1

    ans = 0
    for t in tickets:
        if tickets[t]>1:
            ans+=1

    print(ans)
    n,m = (int(x) for x in input().split())
