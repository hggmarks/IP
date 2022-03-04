filme_1, nota_1, duracao_1 = input().split('-')
filme_2, nota_2, duracao_2 = input().split('-')
filme_3, nota_3, duracao_3 = input().split('-')

melhor_filme = None
nota_min = 4
if (nota_1 < nota_min and nota_2 < nota_min and nota_3 < nota_min):
    print('Nota minima nao atingida')
else:

    if nota_1 > nota_2 and nota_1 > nota_3:
        melhor_filme = nota


