raio_esfera_drag = 2

coord_bulma_x = int(input())
coord_bulma_y = int(input())
raio_bulma = int(input())

coord_esfera_drag_x = int(input())
coord_esfera_drag_y = int(input())

soma_raios = (raio_esfera_drag + raio_bulma)

distancia = ( ( (coord_bulma_x - coord_esfera_drag_x ) ** 2 ) + ( (coord_bulma_y - coord_esfera_drag_y) ** 2 )  ) ** 0.5

if raio_bulma > 0:
    if distancia < soma_raios:
        print('Esferas do dragao detectadas')
    else:
        print('Esferas fora do radar')
else:
    print('Sua amplitude esta baixa, nao conseguimos te localizar no radar')
