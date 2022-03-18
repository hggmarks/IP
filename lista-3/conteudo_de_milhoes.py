num_tiktokers = int(input())
lista = []
qtd_categoria = [0, 0, 0]
media_seguidores = [0, 0, 0]
max_views = [0, 0, 0]

while num_tiktokers > 0:
    lista.append(input().split(', '))
    
    num_tiktokers -= 1

for item in lista:
    if item[3] == 'Lifestyle':
        qtd_categoria[0] += 1

    elif item[3] == 'Utilidades':
        qtd_categoria[1] += 1
    elif item[3] == 'Dancinhas':
        qtd_categorias[2] += 1

print('Lifestyle;')
print(f'Quantidade de Tiktokers: {qtd_categoria[0]}')
print(f'Media de seguidores: {media_seguidores[0]}')
print(f'Maximo de visualizações: {max_views[0]}\n')

print('Utilidades;')
print(f'Quantidade de Tiktokers: {qtd_categoria[1]}')
print(f'Media de seguidores: {media_seguidores[1]}')
print(f'Maximo de visualizações: {max_views[1]}\n')

print('Dancinhas;')
print(f'Quantidade de Tiktokers: {qtd_categoria[2]}')
print(f'Media de seguidores: {media_seguidores[2]}')
print(f'Maximo de visualizações: {max_views[2]}\n')
