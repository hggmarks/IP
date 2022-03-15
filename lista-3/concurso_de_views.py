nome_pessoa_1 = input()
notas_pessoa_1 = []
notas_pessoa_1.append(int(input()))
notas_pessoa_1.append(int(input()))
nome_pessoa_2 = input()
notas_pessoa_2 = []
notas_pessoa_2.append(int(input()))
notas_pessoa_2.append(int(input()))
nome_pessoa_3 = input()
notas_pessoa_3 = []
notas_pessoa_3.append(int(input()))
notas_pessoa_3.append(int(input()))

medias = []
media_1 = 0
media_2 = 0
media_3 = 0

for nota in notas_pessoa_1:
    media_1 += int(nota/2)
medias.append([nome_pessoa_1, media_1])

for nota in notas_pessoa_2:
    media_2 += int(nota/2)
medias.append([nome_pessoa_2, media_2])

for nota in notas_pessoa_3:
    media_3 += int(nota/2)
medias.append([nome_pessoa_3, media_3])

for item in medias:
    for index in range(len(medias)-1):
        if medias[index][1] < medias[index+1][1]:
            medias[index], medias[index+1] = medias[index+1], medias[index]

print(f'1º Lugar: {medias[0][0]} com a media de views: {medias[0][1]}\n2º Lugar: {medias[1][0]} com a media de views: {medias[1][1]}\n3º Lugar: {medias[2][0]} com a media de views: {medias[2][1]}')







letras = ['a', 'b', 'c']