s1, s2, s3 = input().split()

def duplica(f):
    f()
    f()
    f()

def duplica_o_duplicado(f):
    duplica(f)
    

def imprime_parte_linha1():
    print(" "+s1+s2+" " , end="")
    
def imprime_parte_linha1_fim():
    print("")
    
def imprime_parte_linha2():
    print(s1+2*s3+s2, end="")
    
def imprime_parte_linha2_fim():
    print(" ")
      
def imprime_linha1():
    duplica_o_duplicado(imprime_parte_linha1)
    imprime_parte_linha1_fim()

def imprime_linha2():
    duplica_o_duplicado(imprime_parte_linha2)
    imprime_parte_linha2_fim()
    
def imprime_parte_padrão():
    imprime_linha1()
    imprime-linha2()

def imprime_padrão():
    duplica_o_duplicado(imprime_parte_padrão)
    
imprime_padrão()
