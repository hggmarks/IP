def print_find_zelda():
    return print('Vamos embora daqui Princesa!!!')

def print_map(map: list):
    for item in map:
        print(''.join(item))

def move_link(map: list, coord_link: list, matrix_size: int):
    link_char =  'L'
    zelda_char = 'Z'

    if (coord_link[1] < matrix_size-1) and ((map[coord_link[0]+1][coord_link[1]] == '.') or (map[coord_link[0]+1][coord_link[1]] == zelda_char)):
        #baixo
        if (map[coord_link[0]+1][coord_link[1]] == zelda_char):
            map[coord_link[0]+1][coord_link[1]] = link_char
            coord_link[0] += 1
            print_map(map)
            return print_find_zelda()

        else:
            map[coord_link[0]+1][coord_link[1]] = link_char
            coord_link[0] += 1
            print_map(map)
            print('Caminharei pelo Sul e certamente irei encontrar-te, Zelda')
            return move_link(map, coord_link, matrix_size)

    elif (coord_link[0] < matrix_size-1) and ((map[coord_link[0]][coord_link[1]+1] == '.') or (map[coord_link[0]][coord_link[1]+1] == zelda_char)):
        #direita
        if (map[coord_link[0]][coord_link[1]+1] == zelda_char):
            map[coord_link[0]][coord_link[1]+1] = link_char
            coord_link[1] += 1
            print_map(map)
            return print_find_zelda()
        else:
            map[coord_link[0]][coord_link[1]+1] = link_char
            coord_link[1] += 1
            print_map(map)
            print('Caminharei pelo Leste e certamente irei encontrar-te, Zelda\n')
            return move_link(map, coord_link, matrix_size)
        

    elif (coord_link[1] > 0) and ((map[coord_link[0]-1][coord_link[1]] == '.') or (map[coord_link[0]-1][coord_link[1]] == zelda_char)):
        #cima
        if (map[coord_link[0]-1][coord_link[1]] == zelda_char):
            map[coord_link[0]-1][coord_link[1]] = link_char
            coord_link[0] -= 1
            print_map(map)
            return print_find_zelda()
        else:
            map[coord_link[0]-1][coord_link[1]] = link_char
            coord_link[0] -= 1
            print_map(map)
            print('Caminharei pelo Norte e certamente irei encontrar-te, Zelda\n')
            return move_link(map, coord_link, matrix_size) 

    elif (coord_link[0] > 0) and ((map[coord_link[0]][coord_link[1]-1] == '.') or (map[coord_link[0]][coord_link[1]-1] == zelda_char)):
        if (map[coord_link[0]][coord_link[1]-1] == zelda_char):
            map[coord_link[0]][coord_link[1]-1] = link_char
            coord_link[1] -= 1
            print_map(map)
            print('Caminharei pelo Oeste e certamente irei encontrar-te, Zelda\n')
            return print_find_zelda()
        else:
        #esquerda
            map[coord_link[0]][coord_link[1]-1] = link_char
            coord_link[1] -= 1
            print_map(map)
            return move_link(map, coord_link, matrix_size)
    else:
        print('HAHAHAHA você nunca irá resgatá-la, Link!!!')
        

if __name__ == '__main__':
    matrix_size = int(input())
    counter = matrix_size
    player_pos = [int(input()), int(input())]
    mapa = []
    while counter > 0:
        mapa.append(list(input()))
        counter -= 1
    
    
    move_link(mapa, player_pos, matrix_size)