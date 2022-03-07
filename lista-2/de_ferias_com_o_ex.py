n_festas = int(input())

total_cerveja = 0
total_caipirinha = 0
total_vodca = 0

while n_festas > 0:
    n_copos = int(input())

    festa_cerveja = 0
    festa_caipirinha = 0
    festa_vodca = 0
    while n_copos > 0:

        bebida = input()

        if bebida == 'cerveja':
            festa_cerveja += 1
            total_cerveja += 1
        elif bebida == 'caipirinha':
            festa_caipirinha += 1
            total_caipirinha += 1
        elif bebida == 'vodca':
            festa_vodca += 1
            total_vodca += 1

        n_copos -= 1
    
    if festa_cerveja > festa_caipirinha and festa_cerveja > festa_vodca:
        print('O que ele mais tomou nessa festa foi: cerveja')
    elif festa_caipirinha > festa_vodca and festa_caipirinha > festa_cerveja:
        print('O que ele mais tomou nessa festa foi: caipirinha')
    elif festa_vodca > festa_cerveja and festa_vodca > festa_caipirinha:
        print('O que ele mais tomou nessa festa foi: vodca')
    n_festas -= 1

print(f'cerveja - {total_cerveja}')
print(f'caipirinha - {total_caipirinha}')
print(f'vodca - {total_vodca}')
