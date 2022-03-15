num_tiktokers = int(input())

nomes_e_seguidores = []

while num_tiktokers > 0:
    nome, qtd_seguidores = input().split('-')
    nomes_e_seguidores.append([nome, int(qtd_seguidores)])
    num_tiktokers -= 1


for item in nomes_e_seguidores:
    for index in range(len(nomes_e_seguidores)-1):
        if nomes_e_seguidores[index][1] > nomes_e_seguidores[index+1][1]:
            nomes_e_seguidores[index], nomes_e_seguidores[index+1] = nomes_e_seguidores[index+1], nomes_e_seguidores[index]
        elif nomes_e_seguidores[index][1] == nomes_e_seguidores[index+1][1]:
            if len(nomes_e_seguidores[index][0]) > len(nomes_e_seguidores[index+1][0]):
                nomes_e_seguidores[index], nomes_e_seguidores[index+1] = nomes_e_seguidores[index+1], nomes_e_seguidores[index]

for item in nomes_e_seguidores:
    print(f'{item[0]}-{item[1]}')