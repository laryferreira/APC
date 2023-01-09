x, y = map(int,input().split())
volta = 1
difabs = abs(x-y)
while difabs * volta < y:
    volta += 1
print(volta)
