
def qtd_zumbis(rodada: int, kills=0, vivos=0):
    return (10*rodada + kills) - vivos

if __name__ == '__main__':
    total_rodadas = int(input())
    rodada = 1
    while rodada < total_rodadas:
        n_kills, n_vivos = input().split('-')
        n_kills = int(n_kills.strip())
        n_vivos = int(n_vivos.strip())

        print(f'Haverá {qtd_zumbis(rodada, n_kills, n_vivos)} inimigos na rodada {rodada}')
        rodada += 1
        