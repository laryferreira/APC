s, t, f = map(int, input().split())

chegada = s + t + f

if chegada == 24:
    print(0)
elif chegada > 24:
    print(chegada - 24)
elif chegada < 0:
    print(chegada + 24)
else:
    print(chegada)
