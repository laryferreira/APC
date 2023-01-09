def max2(a,b):
    if a>b:
        return a
    else:
        return b
def max3(a,b,c):
    if c>a and c>b:
        return c
    else: 
        return max2(a,b)
