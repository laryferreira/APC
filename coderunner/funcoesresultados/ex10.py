def mdc(a, b):
    if b == 0:
        return a
    resto = a % b
    a = b
    b = resto
    return mdc(a, b)  
