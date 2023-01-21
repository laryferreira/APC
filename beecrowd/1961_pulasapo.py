def pulinho(a1, a2, ap):
    if abs(a1 - a2) > ap:
        return True
    else:
        return False

def main():
    ap, nc = map(int, input().split()) #entradas
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    jogo = False
    for i in range(nc - 1):
        jogo = pulinho(a[i], a[i+1], ap)
        if jogo == True:
            print('GAME OVER')
            break
    if jogo == False:
        print('YOU WIN')

main()
