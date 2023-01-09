B = int(input())
T = int(input())
at = (B + T) * 35 
ar_t = 11200 - at
if at>ar_t:
    print(1)
elif ar_t>at:
    print(2)
else:
    print(0)
