#iccanobif - beecrowd - 2807

''''As sequências de Iccanobif são sequências onde cada termo é sempre igual a soma dos dois próximos subsequentes a eles. Exceto pelos dois últimos termos os quais são sempre iguais a 1.

Exemplo de uma sequência de Iccanobif com 10 termos: 55, 34, 21, 13, 8, 5, 3, 2, 1, 1.

Sua tarefa é, dado um valor inteiro, imprimir a sequência de Iccanobif de tamanho correspondente.''''

def iccanobif(n):
  
  ans = [0] * n  #criando uma lista com n caracteres 'zerados' 
  
  ans[n - 1] = 1
  ans[n - 2] = 1 #padrões pré estabelecidos pela questão
  
  for i in range(n-3, -1, -1) #incompleto, decidi focar em outras questões
