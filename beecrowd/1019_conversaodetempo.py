n = int(input())
h = n//3600
hresto = n%3600

m = hresto//60
s = hresto%60

print(f'{h}:{m}:{s}')
