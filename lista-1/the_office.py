vendedor_1 = 'Jim Halpert'
vendedor_2 = 'Dwight Schrute'
vendedor_3 = 'Phyllis Vance'
vendedor_4 = 'Stanley Hudson'

nome = input()
semestre_1 = int(input())
semestre_2 = int(input())

verifica_nome = (nome != vendedor_1) and (nome != vendedor_2) and (nome != vendedor_3) and (nome != vendedor_4)
media = int((semestre_1 + semestre_2) / 12)

if verifica_nome:
    print('Sinto muito, mas so os vendedores eh que vao ganhar a viagem pra matriz.')
elif (media <= 50):
    print(f'{nome}, voce so vendeu {media} por mes? Voce ta demitido... Brincadeira!')
elif (media < 100):
    print(f'{nome}, voce mandou mal... Vai ter que pagar meu almoco.')
else:
    print(f'Parabens, {nome}! Voce foi promovido! kkkkk Brincadeira, a matriz que decide!')

