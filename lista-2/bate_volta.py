n_rodadas = int(input())
jogador_1 = input()
jogador_2 = input()
jogador_3 = input()
jogador_final_1 = ''
jogador_final_2 = ''
pontos_jog_1 = 0
pontos_jog_2 = 0
pontos_jog_3 = 0
pontos_jog_final_1 = 0
pontos_jog_final_2 = 0

while (n_rodadas > 0) and (pontos_jog_1 < 200 or pontos_jog_2 < 200 or pontos_jog_3 < 200):
    jogada_1 = int(input())
    jogada_2 = int(input())
    jogada_3 = int(input())
    pontos_jog_1 += jogada_1
    pontos_jog_2 += jogada_2
    pontos_jog_3 += jogada_3



    n_rodadas -= 1

emparedado_1 = (jogador_1 * (pontos_jog_1 >= pontos_jog_2 and pontos_jog_1 >= pontos_jog_3)) + (jogador_2 * (pontos_jog_2 >= pontos_jog_1 and pontos_jog_2 >= pontos_jog_3)) + (jogador_3 * (pontos_jog_3 >= pontos_jog_1 and pontos_jog_3 >= pontos_jog_2))

print(f'{emparedado_1} ja esta confirmado no paredao')


if (jogador_1 == emparedado_1):
    jogador_final_1 = jogador_2
    jogador_final_2 = jogador_3
    if pontos_jog_2 > pontos_jog_3:
        print(f'1° - {jogador_2}')
        print(f'2° - {jogador_3}')
    else:
        print(f'1° - {jogador_3}')
        print(f'2° - {jogador_2}')
elif jogador_2 == emparedado_1:
    jogador_final_1 = jogador_1
    jogador_final_2 = jogador_3
    if pontos_jog_1 > pontos_jog_3:
        print(f'1° - {jogador_1}')
        print(f'2° - {jogador_3}')
    else:
        print(f'1° - {jogador_3}')
        print(f'2° - {jogador_1}')
else:
    jogador_final_1 = jogador_1
    jogador_final_2 = jogador_2
    if pontos_jog_1 > pontos_jog_2:
        print(f'1° - {jogador_1}')
        print(f'2° - {jogador_2}')
    else:
        print(f'1° - {jogador_2}')
        print(f'2° - {jogador_1}')


n_rodadas = int(input())

while (n_rodadas > 0):
    pontos_jog_final_1 += int(input())
    pontos_jog_final_2 += int(input())

    n_rodadas -= 1

emparedado_2 = (jogador_final_2 * (pontos_jog_final_1 > pontos_jog_final_2)) + (jogador_final_1 * (pontos_jog_final_2 > pontos_jog_final_1))

print(f'Nosso paredao sera entre {emparedado_1} e {emparedado_2}')