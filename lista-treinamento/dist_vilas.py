coord_hog = (34, 110, 220)
coord_kak = (0, 64, 0)
coord_sol = (140, 200, 456)

dist_hog = 0
dist_kak = 0
dist_sol = 0

pos_x = int(input())
pos_z = int(input())

dist_hog = ((coord_hog[0] - pos_x)**2 + (coord_hog[2] - pos_z)**2) ** 0.5
dist_kak = ((coord_kak[0] - pos_x)**2 + (coord_kak[2] - pos_z)**2) ** 0.5
dist_sol = ((coord_sol[0] - pos_x)**2 + (coord_sol[2] - pos_z)**2) ** 0.5

print('Distancia para Hogsmeade: ', round(dist_hog, 2))
print(f'Distancia para Kakariko: ', round(dist_kak, 2))
print(f'Distancia para Solitude: ', round(dist_sol, 2))

