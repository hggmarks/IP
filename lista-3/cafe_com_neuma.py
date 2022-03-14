n_count = int(input())
entrada = ''
num_cafes = n_count
nomes_meninos = []
numero_meninos = 0
nomes_meninas = []


while n_count > 0:
    entrada = input()
    if entrada[-1] == 'M':
        nomes_meninos.append(entrada[:-4])
        numero_meninos += 1
    else:
        nomes_meninas.append(entrada[:-4])
    n_count -= 1
2
if nomes_meninas == []:
    for menino in nomes_meninos:
        print(f"{menino}, ", end='')
    print(f'Querem cafe?\nSerao necessarias {num_cafes} porcoes de cafe')
elif nomes_meninos == []:
    for menina in nomes_meninas:
        print(f"{menina}, ", end='')
    print('Desculpa, so pros meninos HAHAHAHAAHHAHAHA')
    print('Nao tem meninos na lista, nao precisa fazer cafe, Neuma')
else:
    for menino in nomes_meninos:
        print(f"{menino}, ", end='')

    print(f'Querem cafe?')

    for menina in nomes_meninas:
        print(f"{menina}, ", end='')
    print('Desculpa, so pros meninos HAHAHAHAAHHAHAHA')
    
    print(f'Serao necessarias {numero_meninos} porcoes de cafe')