#problema com a calculadora
n = int(input())
for i in range(1, n+1):
    termos = input()
    
    ans1 = int(termos[2:4])
    ans2 = int(termos[5:8])
    ans3 = int(termos[11:13])

    anst = ans1 + ans2 + ans3
    print(anst)
