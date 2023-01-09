#entrada com 3 dados, map
a, b, c = map(int, input().split())
if a + b == c or a == b + c or b == a + c or a == b or b == c or a == c:
    print(f'S')
else:
    print(f'N')
