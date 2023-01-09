def multiplo3(n):
    if n == 0:
        return True
    elif n == 1 or n == 2:
        return False
    else:
        return multiplo3(n-3)
    
def não_multiplo3(n):
    if n==0:
        return False
    elif n==1 or n==2:
        return True
    else:
        return não_multiplo3(n-3)
