''''Os estudantes da tua universidade recentemente adquiriram o desagradável hábito de cabular as aulas. Para enfrentar este problema o seu Conselho de Professores decidiu somente permitir que estudantes com ao menos 75% de presença prestem os exames. A partir de uma lista de nomes de estudantes e seus respectivos registros de frequência, imprima o nome dos estudantes que não obtiveram o mínimo de presença às aulas e que consequentemente não poderão prestar os exames.

Entrada
A entrada possui diversos casos de testes. A primeira linha da entrada contém um inteiro T, que indica o número de casos de testes que se seguem.

Cada caso de teste é composto por três linhas:

A primeira linha de um caso de teste irá conter um inteiro N (0 ≤ N ≤ 100) que indica o número de estudantes na turma.
A segunda linha conterá N nomes de estudantes com até 50 caracteres cada nome, separados por um único espaço. Todos os nomes irão conter somente letras maiúsculas e minúsculas (‘A’-‘Z’,‘a’-‘z’).
A terceira linha conterá N registros de frequência, correspondentes aos respectivos estudantes da linha anterior. Os registros virão separados por um único espaço, e contêm apenas os caracteres ‘A’, ‘P’ e ‘M’. Um ‘P’ indica que o estudante estava presente à aula, ‘A’ indica que ele estava ausente (ele cabulou à aula) e ‘M’ mostra que, apesar de não ir à aula, ele entregou um atestado médico, então esta aula não deverá ser considerada no cálculo da frequência do estudante. Registros de frequência conterão ao menos um caracter ‘A’ ou ‘P’.
Saída
Para cada caso de teste imprima os nomes de todos os estudantes que não cumpriram a presença mínima requerida, separados por um espaço. Não deixe espaços sobrando no final da linha. ''''

t = int(input()) #casos de teste
while t > 0: #entrada de casos de teste
  n = int(input())
  estudantes = input()
  frequencia = input()
  ncaract_est = len(estudantes) #aqui teremos o número de caracteres de cada entrada pedida
  ncaracte_freq = len(frequencia)
  
  i = 0 #definindo variaveis pra incrementar depois #casosAP
  total = 0 #totaldealunos
  resp = '' #string que receberá a resposta final com o nome dos estudantes
  e = 0 #casoestudantes
  
  for j in range(0,n):
    estudante = ''
    while e < ncaract_est and estudantes[e] != ' ': #le-se enquanto "e" é menor que numero de caracteres da string estudante e "e" é diferente de espaço vazio:
      estudante += estudantes[e] #adicionando o valor da string estudante com cada componente da lista estudantes
      e+=1 #para cada caso, adiciona-se um "e"
      
    A: 0 #variáveis estilo contador para cada caso de ausencia e presenca
    P: 0
    
    while i < ncaracte_freq and frequencia[i] != ' ': #desconsidera o espaço previso
      if frequencia[i] = A: #analisando e comparando os termos da string
        A+=1
      elif frequencia[i] = P:
        P+=1
      i+=1
      #O M não é considerado pois não afeta as frequencias
    
    if P/(A+P) < 0.75: #não cumpriu presença mínima
      resp+=estudante+" " #formatando resposta do nome dos estudantes
      total +=1
    
    e += 1 #estudantes #incrementando no while
    i += 1 #casos AP 
  
  if total>0: #definindo prints (imprimir apenas os estudantes que não cumpriram presença mínima)
    print(resp[:-1]) #retirar espaço sobrando
  else:
    print()
  
  t-=1 #loop 
