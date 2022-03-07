numero_chefs = int(input())

media = 0
erro = False
chef_eliminado = ''
media_eliminado = 0

while numero_chefs > 0:
    chef = input()
    nota_1 = float(input())
    nota_2 = float(input())
    nota_3 = float(input())

    media = (nota_1 + nota_2 + nota_3) / 3 
    
    if media_eliminado == 0:
        media_eliminado = media
        chef_eliminado = chef

    elif media_eliminado > media:
        chef_eliminado = chef
        media_eliminado = media
        
    if media <= 0:
        erro = True
        
    numero_chefs -= 1 
    
if erro:
    print('Ocorreu um erro no sistema de notas, por favor insira notas validas')
else:
    print(f'O chef eliminado da vez é: {chef_eliminado} - {media_eliminado:.2f}')


