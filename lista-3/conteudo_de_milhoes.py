num_tiktokers = int(input())
lista = []
qtd_categorias = [0, 0, 0]
media_seguidores = [0, 0, 0]
max_views = [0, 0, 0]
famosinho = ['', 0, '']
while num_tiktokers > 0:
    lista.append(input().split(', '))
    num_tiktokers -= 1

for item in lista:
    if item[3] == 'Lifestyle':
        qtd_categorias[0] += 1
        if item[2][-1] == 'M':
            if max_views[0] < float(item[2][:-1]):
                max_views[0] = float(item[2][:-1])
        else:
            if max_views[0] < float(item[2][:-1])/1000:
                max_views[0] = float(item[2][:-1])/1000
        
        if item[1][-1] == 'M':
            media_seguidores[0] += float(item[1][:-1])
        else:
            media_seguidores[0] += float(item[1][:-1])/1000

    elif item[3] == 'Utilidades':
        qtd_categorias[1] += 1
        if item[2][-1] == 'M':
            if max_views[1] < float(item[2][:-1]):
                max_views[1] = float(item[2][:-1])
        else:
            if max_views[1] < float(item[2][:-1])/1000:
                max_views[1] = float(item[2][:-1])/1000
                

        if item[1][-1] == 'M':
            media_seguidores[1] += float(item[1][:-1])
        else:
            media_seguidores[1] += float(item[1][:-1])/1000

    elif item[3] == 'Dancinhas':
        qtd_categorias[2] += 1
        if item[2][-1] == 'M':
            if max_views[2] < float(item[2][:-1]):
                max_views[2] = float(item[2][:-1])
        else:
            if max_views[2] < float(item[2][:-1])/1000:
                max_views[2] = float(item[2][:-1])/1000
        
        if item[1][-1] == 'M':
            media_seguidores[2] += float(item[1][:-1])
        else:
            media_seguidores[2] += float(item[1][:-1])/1000


print('Lifestyle;')
if qtd_categorias[0] == 0:
    print('Nao foram informados dados sobre esta categoria.\n')
else:  
    media_seguidores[0] = media_seguidores[0]/(qtd_categorias[0])
    print(f'Quantidade de Tiktokers: {qtd_categorias[0]}')
    print(f'Media de seguidores: {float(str(media_seguidores[0])[:str(media_seguidores[0]).index(".")+2]):.1f}M')
    print(f'Maximo de visualizações: {float(str(max_views[0])[:str(max_views[0]).index(".")+3]):.2f}M\n')

print('Utilidades;')
if qtd_categorias[1] == 0:
    print('Nao foram informados dados sobre esta categoria.\n')
else:
    media_seguidores[1] = media_seguidores[1]/(qtd_categorias[1]) 
    print(f'Quantidade de Tiktokers: {qtd_categorias[1]}')
    print(f'Media de seguidores: {float(str(media_seguidores[1])[:str(media_seguidores[1]).index(".")+2]):.1f}M')
    print(f'Maximo de visualizações: {float(str(max_views[1])[:str(max_views[1]).index(".")+3]):.2f}M\n')

print('Dancinhas;')
if qtd_categorias[2] == 0:
    print('Nao foram informados dados sobre esta categoria.\n')
else:
    media_seguidores[2] = media_seguidores[2]/(qtd_categorias[2])
    print(f'Quantidade de Tiktokers: {qtd_categorias[2]}')
    print(f'Media de seguidores: {float(str(media_seguidores[2])[:str(media_seguidores[2]).index(".")+2]):.1f}M')
    print(f'Maximo de visualizações: {float(str(max_views[2])[:str(max_views[2]).index(".")+3]):.2f}M\n')

for famoso in lista:
    if famoso[1][-1] == 'M':
        if float(famoso[1][:-1]) > famosinho[1]:
            famosinho[1] = float(famoso[1][:-1])
            famosinho[0] = famoso[0]
            famosinho[2] = famoso[3]
    else:
        if float(famoso[1][:-1])/1000 > famosinho[1]:
            famosinho[1] = float(famoso[1][:-1])/1000
            famosinho[0] = famoso[0]
            famosinho[2] = famoso[3]

print(f'Os olhares do mundo estao sobre {famosinho[0].upper()}, que conta com {float(str(famosinho[1])[:str(famosinho[1]).index(".")+2]):.1f}M de seguidores vendo seus videos diarios de {famosinho[2]}!')