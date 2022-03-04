rating_beth = int(input())
rating_adv = int(input())
resultado_partida = input()

probabilidade = 1 / ( 1 + 10 ** ( (rating_adv - rating_beth) / 400 ) )

ponto_obtido = 0

if resultado_partida == 'vitoria':
    ponto_obtido = 1
elif resultado_partida == 'empate':
    ponto_obtido = 0.5

novo_rating = rating_beth + 40 * (ponto_obtido - probabilidade)

if resultado_partida == 'vitoria' or resultado_partida == 'derrota' or resultado_partida == 'empate':
    print(f'O novo rating da Beth Harmon é {int(novo_rating)}')
else:
    print('Resultado da partida invalido')
