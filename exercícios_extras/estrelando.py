'''Estrelando 
Helena gosta de estrelas, principalmente das opostas ★ e ☆. Também gosta de vê-las variando, e pediu sua ajuda para criar uma função recursiva que, dada uma quantidade inicial de estrelas, gradativamente transforme as brancas em pretas e depois as pretas em brancas até voltar a situação original em ordem inversa!
A função deve receber dois argumentos inteiros: a quantidade de estrelas brancas e a de estrelas pretas a serem exibidas.
Entrada
Não há entrada explícita. A função é chamada automaticamente fornecendo os valores inteiros 0≤𝐵,𝑃≤100)0≤B,P≤100), que indicam, respectivamente, a quantidade inicial de estrelas brancas e a de estrelas pretas a serem exibidas.
Saída
A saída deve mostrar a variação da situação inicial de estrelas a cada linha, conforme os exemplos.
Observações:
• Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
• Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome
da função).
• Submeta SOMENTE o que foi solicitado.'''

def brilha(brancas, pretas): if brancas >= 0:
print('☆' * brancas + '★' * pretas) brilha(brancas - 1, pretas + 1)
if brancas:
print('★' * pretas + '☆' * brancas )
