mapa = [['-', '-', '-', '-', '-', '-',],
        ['-', '-', '-', '-', '-', '-',],
        ['-', '-', '-', '-', '-', '-',],
        ['-', '-', '-', '-', '-', '-',],
        ['-', '-', '-', '-', '-', '-',],
        ['-', '-', '-', '-', '-', '-',]]



def set_initial_state(map: list):
    """Takes six inputs (must be numeric) and set as intial
    coordinates of Player, Jason, Gas and Car!"""
    i = 4
    posicoes_iniciais = []
    while i > 0:
        posicoes_iniciais.append([int(input()), int(input())])
        i -= 1
    else:
        i = 6

    for x in range(len(map)):
        for y in range(len(map)):
            if y == posicoes_iniciais[0][0] and x == posicoes_iniciais[0][1]:
                map[x][y] = 'V'
            elif y == posicoes_iniciais[1][0] and x == posicoes_iniciais[1][1]:
                map[x][y] = 'J'
            elif y == posicoes_iniciais[2][0] and x == posicoes_iniciais[2][1]:
                map[x][y] = 'G'
            elif y == posicoes_iniciais[3][0] and x == posicoes_iniciais [3][1]:
                map[x][y] = 'C'
            else
    

def render_map(map: list):
    "Function that render the map"
    for row in mapa:
    
        print(*row)

if __name__ == '__main__':
    render_map(mapa)
    set_initial_state(mapa)
    render_map(mapa)
    
    