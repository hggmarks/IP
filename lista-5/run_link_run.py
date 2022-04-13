def move_link(map: list, coord_link: list, matrix_size: int):
    link_char = 'L'
    if map[coord_link[0]+1][coord_link[1]] == '.':
        map[coord_link[0]+1][coord_link[1]] = link_char

    elif map[coord_link[0]][coord_link[1]+1] == '.':
        map[coord_link[0]][coord_link[1]+1] = link_char

    elif map[coord_link[0]-1][coord_link[1]] == '.':
        map[coord_link[0]-1][coord_link[1]] = link_char




if __name__ == '__main__':
    matrix_size = int(input())
    counter = matrix_size
    player_pos = [int(input()), int(input())]
    mapa = []
    while counter > 0:
        mapa.append(list(input()))
        counter -= 1
    
    print(*mapa, sep='\n')
        