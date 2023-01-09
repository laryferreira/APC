
##
ind_recl = int(input())
perc_recl_resolvidas1 = int(input())
perc_clientes_cancelam = int(input())
iindisponibilidade = int(input())
cancelpproblm = int(input())

if (perc_recl_resolvidas1 >= 60):
    indicenovo = ind_recl - 5
else:
    indicenovo = ind_recl + 15
print(f'{indicenovo}')

if (perc_clientes_cancelam >= 10):
    if (cancelpproblm == 1):
        indicen = ind_recl - 30
else:
    if (cancelpproblm == 0):
        indicen = ind_recl + 80
        
if (perc_clientes_cancelam < 10):
    if (cancelpproblm == 1):
        indicen = ind_recl + 10
else:
    if (cancelpproblm == 0):
        indicen = ind_recl - 50
print(f'{indicen}')

if (iindisponibilidade >= 10):
    indiceindis = ind_recl + 70
else:
    indiceindis = ind_recl - 20
print(f'{indiceindis}')

