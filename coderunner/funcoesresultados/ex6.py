def raizes(a,b,c):
    delta = b*b - 4*(a*c)
    if delta > 0:
        return 2
    elif delta == 0:
        return 1
    elif delta < 0:
        return -1
