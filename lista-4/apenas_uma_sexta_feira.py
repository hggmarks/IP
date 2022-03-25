mapa = [['-', '-', '-', '-', '-', '-',],
        ['-', '-', '-', '-', '-', '-',],
        ['-', '-', '-', '-', '-', '-',],
        ['-', '-', '-', '-', '-', '-',],
        ['-', '-', '-', '-', '-', '-',],
        ['-', '-', '-', '-', '-', '-',]]

posicoes_iniciais = []
posicoes_player_jason = [[], []]
jason_win = False
player_win = False
got_gas = False

def set_initial_state(map: list):
    """Takes six inputs (must be numeric) and set as intial
    coordinates of Player, Jason, Gas and Car!"""
    i = 4

    while i > 0:
        posicoes_iniciais.append([int(input()), int(input())])
        i -= 1
    else:
        i = 6
    
    posicoes_player_jason[0], posicoes_player_jason[1], _, _ = posicoes_iniciais

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
            else:
                map[x][y] = '-'
    
    return map

def render_map(map: list):
    "Function that render the map"
    for row in mapa:
    
        print(*row)

    print()

def move_jason(pos_player: list, pos_jason: list, map: list):
    """Move jason position (with priority in Y-axis) to the player
     position, and update it's position in the map"""
    if pos_jason[0] > pos_player[0]:
        map[pos_jason[1]][pos_jason[0]] = '-'
        pos_jason[0] -= 1
        map[pos_jason[1]][pos_jason[0]] = 'J'

    elif pos_jason[0] < pos_player[0]:
        map[pos_jason[1]][pos_jason[0]] = '-'
        pos_jason[0] += 1
        map[pos_jason[1]][pos_jason[0]] = 'J'
    else:
        if pos_jason[1] > pos_player[1]:
            map[pos_jason[1]][pos_jason[0]] = '-'
            pos_jason[1] -= 1
            map[pos_jason[1]][pos_jason[0]] = 'J'
        elif pos_jason[1] < pos_player[1]:
            map[pos_jason[1]][pos_jason[0]] = '-'
            pos_jason[1] += 1
            map[pos_jason[1]][pos_jason[0]] = 'J'
    
    if pos_jason == pos_player:
        jason_win = True

def move_player(pos_player: list, pos_gas: list, pos_car: list, map: list):
    """Move player (with priority in Y-axis) to the gas
     position first, when the gas is taken, the player 
     moves to the car, and update it's position in the map"""
    if not got_gas:
        if pos_player[0] > pos_gas[0]:
            map[pos_player[1]][pos_player[0]] = '-'
            pos_player[0] -= 1
            map[pos_player[1]][pos_player[0]] = 'V'
        elif pos_player[0] < pos_gas[0]:
            map[pos_player[1]][pos_player[0]] = '-'
            pos_player[0] += 1
            map[pos_player[1]][pos_player[0]] = 'V'
        else:
            if pos_player[1] > pos_gas[1]:
                map[pos_player[1]][pos_player[0]] = '-'
                pos_player[1] -= 1
                map[pos_player[1]][pos_player[0]] = 'V'
            elif pos_player[1] < pos_gas[1]:
                map[pos_player[1]][pos_player[0]] = '-'
                pos_player[1] += 1
                map[pos_player[1]][pos_player[0]] = 'V'
        
    else:
        if pos_player[0] > pos_car[0]:
            map[pos_player[1]][pos_player[0]] = '-'
            pos_player[0] -= 1
            map[pos_player[1]][pos_player[0]] = 'V'
        elif pos_player[0] < pos_car[0]:
            map[pos_player[1]][pos_player[0]] = '-'
            pos_player[0] += 1
            map[pos_player[1]][pos_player[0]] = 'V'
        else:
            if pos_player[1] > pos_car[1]:
                map[pos_player[1]][pos_player[0]] = '-'
                pos_player[1] -= 1
                map[pos_player[1]][pos_player[0]] = 'V'
            elif pos_player[1] < pos_car[1]:
                map[pos_player[1]][pos_player[0]] = '-'
                pos_player[1] += 1
                map[pos_player[1]][pos_player[0]] = 'V'
    
    if pos_player == pos_gas:
        got_gas = True
    else:
        got_gas = False
    
    if pos_player == pos_car:
        player_win = True

if __name__ == '__main__':

    render_map(mapa)

    mapa = set_initial_state(mapa)
    render_map(mapa)

    move_jason(*posicoes_player_jason, mapa)
    move_player(posicoes_player_jason[1], posicoes_iniciais[2], posicoes_iniciais[3], mapa)

    render_map(mapa)

    move_jason(*posicoes_player_jason, mapa)
    move_player(posicoes_player_jason[1], posicoes_iniciais[2], posicoes_iniciais[3], mapa)
    
    render_map(mapa)

