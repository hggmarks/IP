qtd_videos = int(input())

usuarios = []
likes = []

while qtd_videos > 0:
    usuarios.append(input())
    likes.append(int(input()))

    qtd_videos -= 1

for item in likes:
    for index in range(len(likes)-1):
        if likes[index] < likes[index+1]:
            likes[index], likes[index+1] = likes[index+1], likes[index]
            usuarios[index], usuarios[index+1] = usuarios[index+1], usuarios[index]
    

print('O numero de curtidas dos videos que vao aparecer na For You segue a ordem:')

for item in likes:
    if item != likes[-1]:
        print(f'{item}, ', end='')
    else:
        print(f'{item}')

print(f'O primeiro usuario que vai aparecer na For You e {usuarios[0]}!')
