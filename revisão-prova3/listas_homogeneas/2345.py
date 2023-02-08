''''Four friends are playing table tennis. Each of them has a skill level which is represented by an integer number: the higher the number, the better the player is.

The four friends want to form two teams of two players each. For the game to be more exciting, they want the skill level of the teams to be as close as possible. The skill level of a team is the sum of the skill levels of the players in that team.

Although they are very good table tennis players, these friends are not so good at other things, like Math or Computing. Can you help them find the smallest possible difference between the teams’ skill levels?

Input
The input consists of a single line that contains four integers A, B, C and D, representing the skill levels of the four players (0 ≤ A ≤ B ≤ C  D ≤ 104).

Output
Output a line with an integer representing the smallest difference between the skill levels for both teams.''''

#explicação:

 #A, B, C, D representa o nivel de skill dos jogadores, devemos encontrar a menor diferença possível entre os níveis de skill dos dois times = soma dos skills dos jogadores
  
  #vamos pegar cada skill dentro do input como inteiro
  
  skills = [int(s) for s in input().split()]
  
  #perceba que, para que a diferença entre os times seja mínima nos casos de teste, a melhor combinação é:
    # 2 números das extremidades - 2 números restantes
  time1 = skills[0] + skills[3]
  time2 = skills[1] + skills[2] #lembre-se que o índice da lista inicia no 0
  
  #utilizaremos abs para retornar o valor absoluto da diferença entre os dois
  resp = abs(time1 - time2)
  
  print(resp)
   
    
