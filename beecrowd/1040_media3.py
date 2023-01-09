n1, n2, n3, n4 = map(float, input().split())
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print(f'Media: {media:.1f}')

if media >= 7.0:
    print(f'Aluno aprovado.')
elif media < 5.0:
    print(f'Aluno reprovado.')
else:
    print(f'Aluno em exame.')
    nota_exame = float(input())
    print(f'Nota do exame: {nota_exame:.1f}')
    nova_media = (media + nota_exame) / 2.0
    if nova_media >= 5.0:
        print(f'Aluno aprovado.')
    else:
        print(f'Aluno reprovado.')
    print(f'Media final: {nova_media:.1f}')
